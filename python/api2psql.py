import statsapi
import psycopg2
from baseball_data import generateGamePksFromDates
import psycopg2.extras
import time

conn = psycopg2.connect(
    host = "localhost",
    database = "baseball",
    user = "karisch",
    password = "cocacola",
    port = 5432
)

def dictTry(dict, keyList):
    active = dict
    for i in range(len(keyList)):
        if keyList[i] not in active.keys():
            return None
        elif i == len(keyList) - 1:
            return active[keyList[i]]
        else:
            active = active[keyList[i]]

def populateVenueTable(dbConnection, schema):
    teams = statsapi.get('teams', {})

    venueIds = []
    manyList = []
    for team in teams['teams']:
        activeVenue = team['venue']['id']
        if activeVenue not in venueIds:
            venueIds.append(team['venue']['id'])
            manyList.append((team['venue']['id'], team['venue']['name']))
    
    command = """
                INSERT INTO {schema}.venues(id, name)
                    VALUES (%s, %s)
                """

    with dbConnection.cursor() as cur:
        psycopg2.extras.execute_batch(
            cur,
            command.format(schema = schema),
            manyList
        )

def populateTeamTable(dbConnection):
    teams = statsapi.get('teams', {})['teams']

    teams = [x for x in teams if 'division' in x.keys() and 'league' in x.keys()]
    teams = [x for x in teams if 'id' in x['league'].keys()]

    args = []
    for team in teams:
        args.append(
            (
                team['id'],
                team['name'],
                team['season'],
                team['venue']['id'],
                team['teamCode'],
                team['fileCode'],
                team['abbreviation'],
                team['teamName'],
                team['locationName'],
                team['firstYearOfPlay'],
                team['league']['id'],
                team['division']['id'],
                team['shortName']
            )
        )
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

def populatePlayerTable(dbConnection):
    sports = statsapi.get('sports', {})['sports']

    seasons = list(range(2010, 2025))

    args = []
    playerIds = []

    for sport in sports:
        for season in seasons:
            players = statsapi.get('sports_players', {'sportId': sport['id'], 'season': season})['people']
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
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            args
        )
        cur.execute("SET session_replication_role='origin';")