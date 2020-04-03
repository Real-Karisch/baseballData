import statsapi
import numpy as np
import pandas as pd
from baseball_data import *
from attributes import *


pkfire = [599371, 415239]

#jack = pitchDatasetCreateMaster(pkfire, defaultEvent, defaultAtBat, defaultGame)

#jack.to_pickle(path = "testDataFramePickle.pkl")

jack = pd.read_pickle("testDataFramePickle.pkl")

#print(jack.pitchHand.unique())

penis = generateGamePksFromDates('06/04/2018', '06/04/2018')

cock = pitchDatasetCreateMaster(penis, defaultEvent, defaultAtBat, defaultGame)

#print(cock)

cock.to_csv(path_or_buf = 'test.csv', index = False)

"""
gameTest = statsapi.get('game', {'gamePk': 599371})

jack = jsonFind(gameTest, defaultGame['date'], [])

penis = jsonFind(gameTest, defaultEvent['eventType'], [40, 0])

print(jack)

print(penis)

jack = statsapi.get('game', {'gamePk': [599371, 415239]})

print(defaultEvent.keys())

ind = list(defaultEvent.keys())
ind.extend(list(defaultAtBat.keys()))
ind.extend(list(defaultGame.keys()))

outDF = pd.DataFrame(columns=ind)

jack = pitchDatasetCreateGame(gameTest, defaultEvent, defaultAtBat, defaultGame, ind)

print(jack)


astros = statsapi.lookup_team(117)
astros = statsapi.lookup_team('hou')

altuve = statsapi.lookup_player('Jose Altuve')

sched_2019 = statsapi.schedule(start_date='09/29/2019', end_date='09/29/2019')
wsgame1 = statsapi.schedule(start_date='10/22/2019', end_date='10/22/2019')

gamepk = [sched_2019[0]['game_id']]
wspk = wsgame1[0]['game_id']

for i in range(1, len(sched_2019)):
    gamepk.append(sched_2019[i]['game_id'])

gameTest = statsapi.get('game', {'gamePk': gamepk})

print(len(sched_2019[0]))

print(sched_2019[0]['copyright'])

jack = {'penis': 69, 'cock': 420}

for i, j in jack.items():
    print(i)
    print(j)

penis = statsapi.get('game', {'gamePk': 415239})

lenPenis = len(penis['liveData']['plays']['allPlays'])

for i in range(lenPenis):
    print(penis['liveData']['plays']['allPlays'][i]['result']['type'])
    """
    
