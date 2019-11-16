import statsapi
import numpy as np
import pandas as pd

defaultEvent = {
    'isPitch': ['liveData', 'plays', 'allPlays', 'playEvents', 'isPitch'],
    'eventType': ['liveData', 'plays', 'allPlays', 'playEvents', 'details', 'eventType'],

}
defaultAtBat = {
    'pitchHand': ['liveData', 'plays', 'allPlays', 'matchup', 'pitchHand', 'code']
}

defaultGame = {
    'gamePk': ['gamePk'],
    'date': ['gameData', 'datetime', 'originalDate'],
}

def pitchDatasetCreateMaster(gamePks, eventLocations, atBatLocations, gameLocations):
    ind = list(eventLocations.keys())
    ind.extend(list(atBatLocations.keys()))
    ind.extend(list(gameLocations.keys()))

    outDF = pd.DataFrame(columns = ind)

    games = []

    for i in gamePks:
        activeGame = statsapi.get('game', {'gamePk': i})
        games.append(activeGame)

    for i in games:
        activeDF = pitchDatasetCreateGame(i, eventLocations, atBatLocations, gameLocations, ind)
        outDF = outDF.append(activeDF)
    
    return(outDF)

def pitchDatasetCreateGame(gameJson, eventLocations, atBatLocations, gameLocations, index):
    outDF = pd.DataFrame(columns = index)

    atBats = gameJson['liveData']['plays']['allPlays']

    iCnt = 0

    for i in atBats:
        atBatIndex = [iCnt]
        jCnt = 0
        for j in i['playEvents']:
            outDF.append(pd.Series(), ignore_index = True)
            nrow, _ = outDF.shape
            eventIndex = [iCnt, jCnt]

            #game data populate
            for keyGame, valGame in defaultGame.items():
                index = []
                outDF.loc[nrow, keyGame] = jsonFind(gameJson, valGame, index)

            #at bat data populate
            for keyAtBat, valAtBat in defaultAtBat.items():
                outDF.loc[nrow, keyAtBat] = jsonFind(gameJson, valAtBat, atBatIndex) #### need to address routing for at bat number (using index to control)

            #event data populate
            for keyEvent, valEvent in defaultEvent.items(): #### need to address routing for at bat AND event number, as above
                outDF.loc[nrow, keyEvent] = jsonFind(gameJson, valEvent, eventIndex)

            jCnt += 1
        
        iCnt += 1

    return(outDF)

def jsonFind(jsonObj, path, index):
    tempMaster = jsonObj[path[0]]
    cnt = 0
    for i in range(1, len(path)):
        if type(tempMaster) == list:
            tempMaster = tempMaster[index[cnt]]
            cnt += 1
        if path[i] not in tempMaster:
            return('NA')
        tempMaster = tempMaster[path[i]]

    return(tempMaster)
