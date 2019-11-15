import statsapi
import numpy as np

jack = {'penis': 69, 'cock': 420}

for i, j in jack.items():
    print(i)
    print(j)

penis = statsapi.get('game', {'gamePk': 415239})

lenPenis = len(penis['liveData']['plays']['allPlays'])

for i in range(lenPenis):
    print(penis['liveData']['plays']['allPlays'][i]['result']['type'])