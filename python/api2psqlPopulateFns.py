import statsapi
import psycopg2
import psycopg2.extras
import re
import requests

from api2psqlSupporting import *

####################### MAJOR LEAGUE FUNCTIONS #########################

def populateDivisionTable(dbConnection):
    """ Function to populate the divisions table in the major league 
            schema of a postgresql database. Code to construct the 
            database can be found at 
            https://github.com/Real-Karisch/Baseball_Data in the psql
            folder. This function pulls in division data from the 
            MLB stats API and uses psycopg2 to populate the database.
        Input:
            dbConnection: a psycopg2 connection instance to the database
        Notes:
            Does not commit changes after running. Requires the statsapi
            and psycopg2 libraries.
    """
    divisions = statsapi.get('divisions', {})['divisions']

    args = []

    # Loop over the first 7 divisions (i.e. MLB only) pulled and put data in format
    #   usable by psycopg2, storing each row in args
    for division in divisions[:6]:
        args.append(
            (
                division['id'],
                division['name'],
                division['nameShort'],
                division['abbreviation'],
                division['league']['id'],
                division['hasWildcard']
            )
        )

    with dbConnection.cursor() as cur:
        cur.execute("SET session_replication_role='replica';")

        psycopg2.extras.execute_batch(
            cur,
            """
            INSERT INTO major.divisions(
                id, 
                name,
                "nameShort",
                abbrev,
                "leagueId",
                "hasWildcard"
                )
                VALUES (%s, %s, %s, %s, %s, %s)
            """,
            args
        )
        cur.execute("SET session_replication_role='origin';")

def populateLeagueTable(dbConnection):
    """ Function to populate the leagues table in the major league 
            schema of a postgresql database. Code to construct the 
            database can be found at 
            https://github.com/Real-Karisch/Baseball_Data in the psql
            folder. This function pulls in league data from the 
            MLB stats API and uses psycopg2 to populate the database.
        Input:
            dbConnection: a psycopg2 connection instance to the database
        Notes:
            Does not commit changes after running. Requires the statsapi
            and psycopg2 libraries.
    """
    leagues = statsapi.get('league', {'sportId': 1})['leagues']

    args = []

    # Loop over the first 3 leagues (i.e. MLB) pulled and put data in format
    #   usable by psycopg2, storing each row in args
    for league in leagues[:2]:
        args.append(
            (
                league['id'],
                league['season'],
                league['name'],
                league['abbreviation'],
                league['nameShort']
            )
        )

    with dbConnection.cursor() as cur:
        cur.execute("SET session_replication_role='replica';")

        psycopg2.extras.execute_batch(
            cur,
            """
            INSERT INTO major.leagues(
                id, 
                season,
                name,
                abbrev,
                "nameShort"
                )
                VALUES (%s, %s, %s, %s, %s)
            """,
            args
        )
        cur.execute("SET session_replication_role='origin';")

def populatePlayerTable(dbConnection, startDate, endDate, playersPulled = []):
    """ Function to populate or update the players table in the major 
            league schema of a postgresql database. Code to construct 
            the database can be found at 
            https://github.com/Real-Karisch/Baseball_Data in the psql
            folder. This function pulls in player data from the 
            MLB stats API and uses psycopg2 to populate the database. It
            can be used to populate players based on years provided or
            to update the table by passing in player IDs already pulled
            (note that the function updateMajorTablesMaster defined
            below automates this process).
        Inputs:
            dbConnection: a psycopg2 connection instance to the database
            startDate: date from which to start populating players, 
                string representing date in format MM/DD/YYYY
            endDate: date at which to stop populating players, 
                string representing date in format MM/DD/YYYY
            playersPulled (default empty list): list containing player
                IDs already in database
        Notes:
            Does not commit changes after running. Requires the statsapi,
            psycopg2 and re libraries.
    """
    # Players pulled by season, between the first year and last year
    startYear = int(re.search('\d\d.\d\d.(\d\d\d\d)', startDate).group(1))
    endYear = int(re.search('\d\d.\d\d.(\d\d\d\d)', endDate).group(1))

    sports = statsapi.get('sports', {})['sports']

    seasons = list(range(startYear, endYear + 1))

    args = []
    playerIds = playersPulled

    # Loop through each sport (e.g. MLB, minor league, etc.) and each
    #   season, generating a row of data for each player and storing it
    #   in args
    for sport in sports:
        for season in seasons:
            players = statsapi.get(
                'sports_players', 
                {
                    'sportId': sport['id'],
                    'season': season
                }
            )['people']

            # Loop through each player for each season and level of play
            #   and check whether the player is already in args, adding
            #   him if not
            for player in players:
                if player['id'] not in playerIds:
                    playerIds.append(player['id'])
                    args.append(
                        (
                            dictTry(player, ['id']),
                            dictTry(player, ['fullName']),
                            dictTry(player, ['firstName']),
                            dictTry(player, ['lastName']), 
                            dictTry(player, ['primaryNumber']),
                            dictTry(player, ['birthDate']),
                            dictTry(player, ['birthCity']),
                            dictTry(player, ['birthCountry']),
                            dictTry(player, ['height']),
                            dictTry(player, ['weight']),
                            dictTry(player, ['primaryPosition','code']),
                            dictTry(player, ['primaryPosition','name']),
                            dictTry(player, ['primaryPosition','type']),
                            dictTry(player, ['primaryPosition','abbreviation']),
                            dictTry(player, ['useName']),
                            dictTry(player, ['middleName']),
                            dictTry(player, ['boxscoreName']),
                            dictTry(player, ['isPlayer']),
                            dictTry(player, ['mlbDebutDate']),
                            dictTry(player, ['batSide','code']),
                            dictTry(player, ['batSide','description']),
                            dictTry(player, ['pitchHand','code']),
                            dictTry(player, ['pitchHand','description']),
                            dictTry(player, ['strikeZoneTop']),
                            dictTry(player, ['strikeZoneBottom'])
                        )
                    )
                    playerIds.append(player['id'])

    with dbConnection.cursor() as cur:
        cur.execute("SET session_replication_role='replica';")
        psycopg2.extras.execute_batch(
            cur,
            """
            INSERT INTO major.players(
                id,
                "fullName",
                "firstName",
                "lastName",
                "primaryNumber",
                "birthDate",
                "birthCity",
                "birthCountry",
                height,
                weight,
                "positionCode",
                "positionName",
                "positionType",
                "positionAbbrev",
                "useName",
                "middleName",
                "boxscoreName",
                "isPlayer",
                "mlbDebutDate",
                "batSideCode",
                "batSideDesc",
                "pitchHandCode",
                "pitchHandDesc",
                "szTop",
                "szBottom"

                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            args
        )
        cur.execute("SET session_replication_role='origin';")

def populateSeasonTable(dbConnection, startDate, endDate, seasonsPulled = []):
    """ Function to populate or update the seasons table in the major 
            league schema of a postgresql database. Code to construct 
            the database can be found at 
            https://github.com/Real-Karisch/Baseball_Data in the psql
            folder. This function pulls in season date info from the 
            MLB stats API and uses psycopg2 to populate the database. It
            provides basic dates for pre-, post- and regular seasons. It
            can also be used to update the table by passing in a list of
            seasons already in the database.
        Inputs:
            dbConnection: a psycopg2 connection instance to the database
            startDate: date from which to start populating seasons, 
                string representing date in format MM/DD/YYYY
            endDate: date at which to stop populating seasons, 
                string representing date in format MM/DD/YYYY
            seasonsPulled (default empty list): list containing seasons
                already in database
        Notes:
            Does not commit changes after running. Requires the statsapi,
            psycopg2 and re libraries.
    """
    # Dates pulled by season, between the first year and last year
    startYear = int(re.search('\d\d.\d\d.(\d\d\d\d)', startDate).group(1))
    endYear = int(re.search('\d\d.\d\d.(\d\d\d\d)', endDate).group(1))

    args = []

    # Loop through each year and pull season date info for that year,
    #   putting the info for each year in args
    for year in range(startYear, endYear + 1):
        seasons = statsapi.get('season', {'seasonId': year, 'sportId': 1})['seasons']

        for season in seasons:
            if season['seasonId'] not in seasonsPulled:
                args.append(
                    (
                        season['seasonId'],
                        season['regularSeasonStartDate'],
                        season['regularSeasonEndDate'],
                        dictTry(season, ['preSeasonStartDate']),
                        dictTry(season, ['preSeasonEndDate']),
                        season['postSeasonStartDate'],
                        season['postSeasonEndDate'],
                        dictTry(season, ['lastDate1stHalf']),
                        dictTry(season, ['firstDate2ndHalf']),
                        dictTry(season, ['allStarDate'])
                    )
                )
                seasonsPulled.append(season['seasonId'])

    with dbConnection.cursor() as cur:
        cur.execute("SET session_replication_role='replica';")

        psycopg2.extras.execute_batch(
            cur,
            """
            INSERT INTO major.seasons(
                "seasonId", 
                "regSeasStartDate",
                "regSeasEndDate",
                "preSeasStartDate",
                "preSeasEndDate",
                "postSeasStartDate",
                "postSeasEndDate",
                "lastDate1stHalf",
                "firstDate2ndHalf",
                "allStarDate"
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            args
        )
        cur.execute("SET session_replication_role='origin';")

def populateTeamTable(dbConnection, startDate, endDate, teamsPulled = []):
    """ Function to populate or update the teams table in the major 
            league schema of a postgresql database. Code to construct 
            the database can be found at 
            https://github.com/Real-Karisch/Baseball_Data in the psql
            folder. This function pulls in team info by season from the 
            MLB stats API and uses psycopg2 to populate the database. It
            can also be used to update the table by passing in a list of
            teams already in the database.
        Inputs:
            dbConnection: a psycopg2 connection instance to the database
            startDate: date from which to start populating teams, 
                string representing date in format MM/DD/YYYY
            endDate: date at which to stop populating teams, 
                string representing date in format MM/DD/YYYY
            teamsPulled (default empty list): list containing team IDs
                already in database
        Notes:
            Does not commit changes after running. Requires the statsapi,
            psycopg2 and re libraries.
    """
    # Teams pulled by season, between the first year and last year
    startYear = int(re.search('\d\d.\d\d.(\d\d\d\d)', startDate).group(1))
    endYear = int(re.search('\d\d.\d\d.(\d\d\d\d)', endDate).group(1))

    years = range(startYear, endYear + 1)

    args = []

    # Loop through each year and pull team info for that year, putting 
    #   the info for each team in args
    for year in years:

        teams = statsapi.get('teams', {'season' : year})['teams']

        teams = [x for x in teams if 'division' in x.keys() and 'league' in x.keys()]
        teams = [x for x in teams if 'id' in x['league'].keys()]

        for team in teams:
            if (team['id'], team['season']) not in teamsPulled:
                args.append(
                    (
                        dictTry(team,['id']),
                        dictTry(team, ['name']),
                        dictTry(team,['season']),
                        dictTry(team,['venue','id']),
                        dictTry(team,['teamCode']),
                        dictTry(team,['fileCode']),
                        dictTry(team, ['abbreviation']),
                        dictTry(team,['teamName']),
                        dictTry(team,['locationName']),
                        dictTry(team,['firstYearOfPlay']),
                        dictTry(team,['league','id']),
                        dictTry(team,['division','id']),
                        dictTry(team,['shortName'])
                    )
                )
                teamsPulled.append((team['id'], team['season']))

    with dbConnection.cursor() as cur:
        cur.execute("SET session_replication_role='replica';")
        psycopg2.extras.execute_batch(
            cur,
            """
            INSERT INTO major.teams(
                id, 
                name,
                season,
                "venueID",
                "teamCode",
                "fileCode",
                abbrev,
                "teamName",
                "locationName",
                "firstYearOfPlay",
                "leagueID",
                "divisionID",
                "shortName"
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            args
        )
        cur.execute("SET session_replication_role='origin';")

def populateVenueTable(dbConnection, venueArgs):
    """ Function to populate the venues table in the major league 
            schema of a postgresql database. Code to construct the 
            database can be found at 
            https://github.com/Real-Karisch/Baseball_Data in the psql
            folder. This function takes venue data defined in 
            api2psqlSupporting.venueArgs from the MLB stats API and uses
            psycopg2 to populate the database.
        Inputs:
            dbConnection: a psycopg2 connection instance to the database
            venueArgs: a list containing the rows for each venue
        Notes:
            Does not commit changes after running. Requires the statsapi
            and psycopg2 libraries.
    """
    with dbConnection.cursor() as cur:
        cur.execute("SET session_replication_role='replica';")
        psycopg2.extras.execute_batch(
            cur,
            """
            INSERT INTO major.venues(
                id, 
                name,
                city,
                state,
                latitude,
                longitude,
                "tzOffset",
                "tzName",
                capacity,
                "turfType",
                "roofType",
                "leftLine",
                "leftCenter",
                center,
                "rightCenter",
                "rightLine"
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            venueArgs
        )
        cur.execute("SET session_replication_role='origin';")

def populateGamesTablesMaster(dbConnection, schema, startDate, endDate, pathListListDict, 
    commandDict, gamesPulled = []):
    """ Function to populate or update the games, atbats, actions, 
            pitches and runners tables in the major OR minor schema of a 
            postgresql database. Code to construct the database can be 
            found at https://github.com/Real-Karisch/Baseball_Data in 
            the psql folder. This function pulls in game info from the
            MLB stats API and populates each table with psycopg2. It can
            also be used to update the tables by passing in a list of
            game pk's of games already in the database.
        Inputs:
            dbConnection: a psycopg2 connection instance to the database
            schema: should be either 'major' or 'minor'
            startDate: date from which to start populating tables, 
                string representing date in format MM/DD/YYYY
            endDate: date at which to stop populating tables, 
                string representing date in format MM/DD/YYYY
            pathListListDict: a dictionary with keys for each table,
                each pointing to a list of key paths to navigate the 
                game JSON pulled from the API to get the item
            commandDict: a dictionary with keys for each table,
                each pointing to a string with the sql command to 
                populate that table
            gamesPulled (default empty list): list containing game pks
                already in database
        Notes:
            Does not commit changes after running. Requires the statsapi
            and psycopg2 libraries.
    """
    # Loop to add correct schema to sql commands
    for key, value in commandDict.items():
        commandDict[key] = value.format(schema = schema)

    if schema == 'major':
        gamePks = generateGamePksFromDates(startDate=startDate, endDate=endDate)
    else:
        sports = [11,12,13,14,15,16,5442] # Minor league sport id's
        gamePks = []
        for sport in sports:
            gamePks += generateGamePksFromDates(startDate, endDate, sportId = sport)

    argsDict = {
        'games': [],
        'atBats': [],
        'actions': [],
        'pitches': [],
        'runners': []
    }

    # Loop through the games and append rows for each item for each
    #   table to its respective args list
    for gamePk in gamePks:
        if gamePk not in gamesPulled:
            try:
                game = statsapi.get('game', {'gamePk': gamePk})
            except ConnectionError:
                print('ConnectionError on game:', gamePk)
                continue
            except requests.HTTPError:
                print('HTTPError on game:', gamePk)
            
            # All of these pull multiple rows per game except 'games'
            argsDict['games'].append(generateGameArgs(game, pathListListDict['games']))
            argsDict['atBats'] += generateAtBatArgs(game, pathListListDict['atBats'])
            argsDict['actions'] += generateActionArgs(game, pathListListDict['actions'])
            argsDict['pitches'] += generatePitchArgs(game, pathListListDict['pitches'])
            argsDict['runners'] += generateRunnerArgs(game, pathListListDict['runners'])

            gamesPulled.append(gamePk)

    with dbConnection.cursor() as cur:
        cur.execute("SET session_replication_role='replica';")
        for key in argsDict.keys():
            psycopg2.extras.execute_batch(
                cur,
                commandDict[key],
                argsDict[key]
            )

        cur.execute("SET session_replication_role='origin';")

def populateMajorTablesMaster(dbConnection):
    """ Function to drive populating all tables in major league schema 
            of a postgresql database. Code to construct the database can 
            be found at https://github.com/Real-Karisch/Baseball_Data in 
            the psql folder. Calls all the other populate functions
            defined above. Dates pulled can be changed, but default to
            full seasons 2015 - 2020. 
        Inputs:
            dbConnection: a psycopg2 connection instance to the database
        Notes:
            Commits changes after running. Requires the statsapi, re
            and psycopg2 libraries.

    """
    startDate = '01/01/2015'
    endDate = '12/31/2020'
    schema = 'major'

    populateDivisionTable(dbConnection)
    populateLeagueTable(dbConnection)
    populatePlayerTable(dbConnection, startDate, endDate)
    populateSeasonTable(dbConnection, startDate, endDate)
    populateTeamTable(dbConnection, startDate, endDate)
    populateVenueTable(dbConnection, venueArgs)
    populateGamesTablesMaster(dbConnection, schema, startDate, endDate, pathListListDict, commandDict)

    dbConnection.commit()

def updateMajorTablesMaster(dbConnection, startDate, endDate):
    """ Function to drive updating all tables in major league schema 
            of a postgresql database. Code to construct the database can 
            be found at https://github.com/Real-Karisch/Baseball_Data in 
            the psql folder. Calls all the other populate functions
            defined above after pulling row id's already in the
            database.  
        Inputs:
            dbConnection: a psycopg2 connection instance to the database
            startDate: date from which to start updating, string in
                format MM/DD/YYYY
            endDate: date at which to start updating, string in format 
                MM/DD/YYYY
        Notes:
            Commits changes after running. Requires the statsapi, re
            and psycopg2 libraries.
    """
    # Pull pk's for each table of items already in the database
    with dbConnection.cursor() as cur:
        cur.execute("SELECT pk FROM major.games;")
        gamesPulled = [x[0] for x in cur.fetchall()]
        cur.execute("""SELECT "seasonId" FROM major.seasons;""")
        seasonsPulled = [x[0] for x in cur.fetchall()]
        cur.execute("""SELECT id FROM major.players;""")
        playersPulled = [x[0] for x in cur.fetchall()]
        cur.execute("""SELECT id, season FROM teams;""")
        teamsPulled = cur.fetchall()

    schema = 'major'

    populatePlayerTable(dbConnection, startDate, endDate, playersPulled)
    populateSeasonTable(dbConnection, startDate, endDate, seasonsPulled)
    populateTeamTable(dbConnection, startDate, endDate, teamsPulled)
    populateGamesTablesMaster(
        dbConnection, 
        schema, 
        startDate, 
        endDate, 
        pathListListDict, 
        commandDict, 
        gamesPulled
    )
    
    dbConnection.commit()

####################### MINOR LEAGUE FUNCTIONS #########################

def populateMinorSeasonTable(dbConnection, startDate, endDate, seasonsPulled = []):
    """ Function to populate or update the seasons table in the minor 
            league schema of a postgresql database. Code to construct 
            the database can be found at 
            https://github.com/Real-Karisch/Baseball_Data in the psql
            folder. This function pulls in season date info by minor 
            league sport from the MLB stats API and uses psycopg2 to 
            populate the database. It provides basic dates for post- and
            regular season. It can also be used to update the table by 
            passing in a list of seasons already in the database.
        Inputs:
            dbConnection: a psycopg2 connection instance to the database
            startDate: date from which to start populating seasons, 
                string representing date in format MM/DD/YYYY
            endDate: date at which to stop populating seasons, 
                string representing date in format MM/DD/YYYY
            seasonsPulled (default empty list): list containing seasons
                already in database
        Notes:
            Does not commit changes after running. Requires the statsapi,
            psycopg2 and re libraries.
    """
    # Dates pulled by season, between the first year and last year
    startYear = int(re.search('\d\d.\d\d.(\d\d\d\d)', startDate).group(1))
    endYear = int(re.search('\d\d.\d\d.(\d\d\d\d)', endDate).group(1))

    sports = statsapi.get('sports', {})['sports']

    args = []
    # Loop through each year and minor league sport and pull season date
    #   info for that year, putting the info for each year in args
    for sport in sports:
        for year in range(startYear, endYear + 1):
            seasons = statsapi.get('season', {'seasonId': year, 'sportId': sport['id']})['seasons']

            for season in seasons:
                if (int(season['seasonId']), sport['id']) not in seasonsPulled:
                    args.append(
                        (
                            int(season['seasonId']),
                            sport['id'],
                            dictTry(season,['regularSeasonStartDate']),
                            dictTry(season,['regularSeasonEndDate']),
                            dictTry(season,['postSeasonStartDate']),
                            dictTry(season,['postSeasonEndDate'])
                        )
                    )
                    seasonsPulled.append((int(season['seasonId']), sport['id']))

    with dbConnection.cursor() as cur:
        cur.execute("SET session_replication_role='replica';")

        psycopg2.extras.execute_batch(
            cur,
            """
            INSERT INTO minor.seasons(
                "seasonId", 
                "sportId",
                "regSeasStartDate",
                "regSeasEndDate",
                "postSeasStartDate",
                "postSeasEndDate"
                )
                VALUES (%s, %s, %s, %s, %s, %s)
            """,
            args
        )
        cur.execute("SET session_replication_role='origin';")

def populateMinorSportsTable(dbConnection):
    """ Function to populate or update the sports table in the minor 
            league schema of a postgresql database. Code to construct 
            the database can be found at 
            https://github.com/Real-Karisch/Baseball_Data in the psql
            folder. This function pulls in minor league sports info from 
            the MLB stats API and uses psycopg2 to populate the 
            database. 
        Input:
            dbConnection: a psycopg2 connection instance to the database
        Notes:
            Does not commit changes after running. Requires the statsapi
            and psycopg2 libraries.
    """
    sports = statsapi.get('sports', {})['sports']

    args = []

    # Loop through each minor league sport and add a row for each to
    #   args
    for sport in sports:
        args.append(
            (
                str(sport['id']),
                sport['code'],
                sport['name'],
                sport['abbreviation']
            )
        )
    
    with dbConnection.cursor() as cur:
        cur.execute("SET session_replication_role='replica';")

        psycopg2.extras.execute_batch(
            cur,
            """
            INSERT INTO minor.sports(
                "sportId",
                code,
                name,
                abbrev
                )
                VALUES (%s, %s, %s, %s)
            """,
            args
        )
        cur.execute("SET session_replication_role='origin';")

def populateMinorTablesMaster(dbConnection):
    """ Function to drive populating all tables in minor league schema 
            of a postgresql database. Code to construct the database can 
            be found at https://github.com/Real-Karisch/Baseball_Data in 
            the psql folder. Calls other populate functions defined 
            above. Dates can be changed, but defaults to seasons 2019 - 
            2020.
        Input:
            dbConnection: a psycopg2 connection instance to the database
        Notes:
            Commits changes after running. Requires the statsapi, re
            and psycopg2 libraries.
    """
    startDate = '01/01/2020'
    endDate = '12/31/2020'
    schema = 'minor'

    populateMinorSeasonTable(dbConnection, startDate, endDate)
    populateMinorSportsTable(dbConnection)
    populateGamesTablesMaster(dbConnection, schema, startDate, endDate, pathListListDictMinor, commandDictMinor)

    dbConnection.commit()

def updateMinorTablesMaster(dbConnection, startDate, endDate):
    """ Function to drive updating tables in minor league schema 
            of a postgresql database. Code to construct the database can 
            be found at https://github.com/Real-Karisch/Baseball_Data in 
            the psql folder. Calls the other populate functions defined 
            above after pulling row id's already in the database. 
        Inputs:
            dbConnection: a psycopg2 connection instance to the database
            startDate: date from which to start updating, string in
                format MM/DD/YYYY
            endDate: date at which to start updating, string in format 
                MM/DD/YYYY

        Notes:
            Commits changes after running. Requires the statsapi, re
            and psycopg2 libraries.
    """
    # Pull pk's for each table of items already in the database
    with dbConnection.cursor() as cur:
        cur.execute("SELECT pk FROM minor.games;")
        gamesPulled = [x[0] for x in cur.fetchall()]
        cur.execute("""SELECT "seasonId", "sportId" FROM minor.seasons;""")
        seasonsPulled = cur.fetchall()

    schema = 'minor'

    populateMinorSeasonTable(dbConnection, startDate, endDate, seasonsPulled)
    populateGamesTablesMaster(
        dbConnection, 
        schema, 
        startDate, 
        endDate, 
        pathListListDictMinor, 
        commandDictMinor, 
        gamesPulled
    )
    
    dbConnection.commit()