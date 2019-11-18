import statsapi
import numpy as np
import pandas as pd

#function to generate the unique game pk (ID) for each game played between the dates provided (inclusive)
#inputs: startDate is the beginning of the period of games to be pulled ('mm/dd/yyyy' format)
#        endDate is the last day of the period ('mm/dd/yyyy' format)
#output: a list of game pks
def generateGamePksFromDates(startDate, endDate):
    sched = statsapi.schedule(start_date = startDate, end_date = endDate) #call to the mlb website to scrape the raw data
    gamePks = [x['game_id'] for x in sched] #list comp to pull the gamePk from each game scraped (come through in JSON format)
    return(gamePks)

#function to run the master dataframe that is a concatenation of each game dataframe from the provided gamePks
#inputs: gamePks is a list of gamePks
#        eventLocations is a dictionary in which each key is the title of a column/feature in the output dataframe and each value is a list of strings
#           that maps to the location of the item in question within the MLB raw game JSON. These items to be pulled are at the 'event' level (most granular,
#           e.g. a single pitch/play or a stolen base)
#        atBatLocations is a dictionary like eventLocations, except it includes items at the at bat level (e.g. pitcher, batter, result of at bat, etc.)
#        gameLocations is a dictionary like the two above, except it includes items at the game level (e.g. home team/away team, date, lineups, etc.)
#output: a single dataframe with every feature in the dictionaries provided (one row per event), from every gamePk provided
def pitchDatasetCreateMaster(gamePks, eventLocations, atBatLocations, gameLocations):
    ind = list(eventLocations.keys()) #making index for column names of output dataframe
    ind.extend(list(atBatLocations.keys()))
    ind.extend(list(gameLocations.keys()))

    outDF = pd.DataFrame(columns = ind) #setting up empty output dataframe

    #loop to generate raw data for each game, then turn the raw game data into a dataframe and append it to the master dataframe
    for i in gamePks:
        activeGame = statsapi.get('game', {'gamePk': i}) #call to mlb site to scrape raw game data as JSON file
        activeDF = pitchDatasetCreateGame(activeGame, eventLocations, atBatLocations, gameLocations, ind) #generate dataframe from game JSON file
        outDF = outDF.append(activeDF) #concatenate the latest game with the master dataframe

    return(outDF)

#function to oversee the creation of a dataframe from the raw JSON file of a particular game
#inputs: gameJson is the raw JSON file of a particular game provided as a dictionary of dictionaries and lists
#        eventLocations is passed directly from pitchDatasetCreateMaster, see definition above
#        atBatLocations is passed directly from pitchDatasetCreateMaster, see definition above
#        gameLocations is passed directly from pitchDatasetCreateMaster, see definition above
#        index is a list of strings that is used as the column names of the output dataframe
#output: a dataframe that includes the features from the three input dictionaries for a particular game
def pitchDatasetCreateGame(gameJson, eventLocations, atBatLocations, gameLocations, index):
    outDF = pd.DataFrame(columns = index) #setting up empty output dataframe

    atBats = gameJson['liveData']['plays']['allPlays'] #accessing a list of data for each at bat in the game

    iCnt = 0 #counter for at bat index

    #loop to access data for each at bat
    for i in atBats:
        atBatIndex = [iCnt] #the current at bat
        jCnt = 0 #counter for event index

        #loop to access data for each event within the current at at bat
        for j in i['playEvents']: 
            outDF.append(pd.Series(), ignore_index = True) #append empty row to output dataframe
            nrow, _ = outDF.shape
            eventIndex = [iCnt, jCnt] #current at bat and event within that at bat

            #loop to populate the output dataframe with game-level attributes
            for keyGame, valGame in gameLocations.items():
                index = [] #empty index, since game does not need to access at bat- or event-level information
                outDF.loc[nrow, keyGame] = jsonFind(gameJson, valGame, index) 

            #loop to populate output dataframe with at bat-level attributes
            for keyAtBat, valAtBat in atBatLocations.items():
                outDF.loc[nrow, keyAtBat] = jsonFind(gameJson, valAtBat, atBatIndex) #atBatIndex (created above) is a list with the current at bat

            #loop to populate output dataframe with event-level attributes
            for keyEvent, valEvent in eventLocations.items(): #eventIndex (created above) is a list with the current at bat and the current event
                outDF.loc[nrow, keyEvent] = jsonFind(gameJson, valEvent, eventIndex)

            jCnt += 1
        
        iCnt += 1

    return(outDF)

#function to locate a particular item within a JSON object (formatted as dictionary of dictionaries and lists by python)
#inputs: jsonObj is a dictionary that is derived directly from a JSON file. It contains a number of sub and sub-sub dictionaries and lists
#        path is a list of strings that are the keys to navigate the JSON dictionary
#        index is a list of indices to be used whenever a list is encountered during navigation. If the current path key hits a list, the function
#           goes to the next item in index it has not yet accessed and uses the value it finds to access that element of the list it has encountered.
#           Basically, if the number of lists to be encountered is known beforehand, index is a way of navigating to a particular element within those lists
#output: the value found by the last key in the path list
def jsonFind(jsonObj, path, index):
    temp = jsonObj[path[0]] #initiating temporary variable to navigate through dictionary
    cnt = 0 #counter of lists encountered during navigation

    #loop to navigate the dictionaries/lists of the JSON object
    for i in range(1, len(path)):
        if type(temp) == list: #if a list is encountered
            temp = temp[index[cnt]] #access the element given by index
            cnt += 1 #increment counter for next list to be encountered
        if path[i] not in temp: #if the next key is not in the value of the current dictionary
            return('NA') #return 'NA' to be processed later
        temp = temp[path[i]] #move to next dictionary/list

    return(temp)