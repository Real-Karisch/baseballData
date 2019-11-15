import statsapi
import numpy as np
import pandas as pd

astros = statsapi.lookup_team(117)
astros = statsapi.lookup_team('hou')

altuve = statsapi.lookup_player('Jose Altuve')

sched_2019 = statsapi.schedule(start_date = '09/29/2019', end_date = '09/29/2019')
wsgame1 = statsapi.schedule(start_date = '10/22/2019', end_date = '10/22/2019')

gamepk = [sched_2019[0]['game_id']]
wspk = wsgame1[0]['game_id']

for i in range(1, len(sched_2019)):
    gamepk.append(sched_2019[i]['game_id'])

gameTest = statsapi.get('game', {'gamePk': 567139})

print(len(sched_2019[0]))

print(sched_2019[0]['copyright'])

def pitchDatasetCreateMaster(gamePks, additionalLocations = {}):
    defaultEvent = {
        'isPitch': ['liveData', 'plays', 'allPlays', 'playEvents', 'isPitch'],
        'eventType': ['liveData', 'plays', 'allPlays', 'playEvents', 'details', 'eventType'],
        
    }
    defaultAtBat = {
        
    }

    defaultGame = {
        'gamePk': ['gamePk'],
        'date': ['gameData', 'datetime', 'originalDate'],
    }

    ind = list(defaultEvent.keys())
    ind.extend(list(defaultAtBat.keys()))
    ind.extend(list(defaultGame.keys()))

    outDF = pd.DataFrame(columns = ind)

    #atbat count

    atBatCnt = len()

    #gameData

    #for keyGame, valueGame in defaultEvent.items():
    #    outDF[keyGame] = 1

def pitchDatasetCreateGame(gameJson, defaultEvent, defaultAtBat, defaultGame, additionalLocations, index):
    outDF = pd.DataFrame(columns = index)

    atBats = gameJson['liveData']['plays']['allPlays']

    #at bat count
    #atBatCnt = len(atBats)

    iCnt = 0

    for i in atBats:
        #eventCnt = len(gameJson['liveData']['plays']['allPlays'][i]['playEvents'])
        atBatIndex = [iCnt]
        jCnt = 0
        for j in i['playEvents']:
            outDF.append(pd.Series(), ignore_index = True)
            nrow, _ = outDF.shape
            eventIndex = [iCnt, jCnt]

            #game data populate
            for keyGame, valGame in defaultGame.items():
                index = []
                outDF[keyGame][nrow] = jsonFind(gameJson, valGame, index)

            #at bat data populate
            for keyAtBat, valAtBat in defaultAtBat.items():
                outDF[keyAtBat][nrow] = jsonFind(gameJson, valAtBat, atBatIndex) #### need to address routing for at bat number (using index to control)

            #event data populate
            for keyEvent, valEvent in defaultEvent.items(): #### need to address routing for at bat AND event number, as above
                outDF[keyEvent][nrow] = jsonFind(gameJson, valEvent, eventIndex)

            jCnt += 1
        
        iCnt += 1

def jsonFind(jsonObj, path, index):
    tempMaster = jsonObj[path[0]]
    cnt = 0
    for i in range(1, len(path)):
        if type(tempMaster) == list:
            tempMaster = tempMaster[index[cnt]]
            cnt += 1
        tempMaster = tempMaster[path[i]]

    return(tempMaster)