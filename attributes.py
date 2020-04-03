defaultEvent = {
    'balls': ['liveData', 'plays', 'allPlays', 'playEvents', 'count', 'balls'], #after the event
    'strikes': ['liveData', 'plays', 'allPlays', 'playEvents', 'count', 'strikes'], #after the event
    'isPitch': ['liveData', 'plays', 'allPlays', 'playEvents', 'isPitch'],
    'eventType': ['liveData', 'plays', 'allPlays', 'playEvents', 'details', 'eventType'],
    'pitchCount': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchNumber'],
    'pitchType': ['liveData', 'plays', 'allPlays', 'playEvents', 'details', 'type', 'code'],
    'inPlay': ['liveData', 'plays', 'allPlays', 'playEvents', 'details', 'isInPlay'],
    'pitchResult': ['liveData', 'plays', 'allPlays', 'playEvents', 'details', 'code'],
    'isBall': ['liveData', 'plays', 'allPlays', 'playEvents', 'details', 'isBall'],
    'eventType': ['liveData', 'plays', 'allPlays', 'playEvents', 'details', 'eventType'],
    'pitchZone': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'zone'],
    'extension': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'extension'],
    'startSpeed': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'startSpeed'],
    'szTop': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'strikeZoneTop'],
    'szBottom': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'strikeZoneBottom'],
    'aX': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'coordinates', 'aX'],
    'aY': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'coordinates', 'aY'],
    'aZ': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'coordinates', 'aZ'],
    'pfxX': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'coordinates', 'pfxX'],
    'pfxZ': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'coordinates', 'pfxZ'],
    'pX': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'coordinates', 'pX'],
    'pZ': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'coordinates', 'pZ'],
    'vX0': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'coordinates', 'vX0'],
    'vY0': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'coordinates', 'vY0'],
    'vZ0': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'coordinates', 'vZ0'],
    'x': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'coordinates', 'x'],
    'y': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'coordinates', 'y'],
    'x0': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'coordinates', 'x0'],
    'y0': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'coordinates', 'y0'],
    'z0': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'coordinates', 'z0'],
    'breakAngle': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'breaks', 'breakAngle'],
    'breakLength': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'breaks', 'breakLength'],
    'breakY': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'breaks', 'breakY'],
    'spinRate': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'breaks', 'spinRate'],
    'spinDirection': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'breaks', 'spinDirection'],
    'plateTime': ['liveData', 'plays', 'allPlays', 'playEvents', 'pitchData', 'plateTime'],
    'launchSpeed': ['liveData', 'plays', 'allPlays', 'playEvents', 'hitData', 'launchSpeed'],
    'launchAngle': ['liveData', 'plays', 'allPlays', 'playEvents', 'hitData', 'launchAngle'],
    'totalDistance': ['liveData', 'plays', 'allPlays', 'playEvents', 'hitData', 'totalDistance'],
    'trajectory': ['liveData', 'plays', 'allPlays', 'playEvents', 'hitData', 'trajectory'],
    'hardness': ['liveData', 'plays', 'allPlays', 'playEvents', 'hitData', 'hardness'],
    'hitLocation': ['liveData', 'plays', 'allPlays', 'playEvents', 'hitData', 'location'],
    'hitCoordX': ['liveData', 'plays', 'allPlays', 'playEvents', 'hitData', 'coordinates', 'coordX'],
    'hitCoordY': ['liveData', 'plays', 'allPlays', 'playEvents', 'hitData', 'coordinates', 'coordY'],
}

defaultAtBat = {
    'pitcher': ['liveData', 'plays', 'allPlays', 'matchup', 'pitcher', 'id'],
    'pitchHand': ['liveData', 'plays', 'allPlays', 'matchup', 'pitchHand', 'code'],
    'batter': ['liveData', 'plays', 'allPlays', 'matchup', 'batter', 'id'],
    'batSide': ['liveData', 'plays', 'allPlays', 'matchup', 'batSide','code'],
    'homeScore': ['liveData', 'plays', 'allPlays', 'result', 'homeScore'], #after the at bat
    'awayScore': ['liveData', 'plays', 'allPlays', 'result', 'awayScore'], #after the at bat
    'outs': ['liveData', 'plays', 'allPlays', 'count', 'outs'], #after the at bat
    'inning': ['liveData', 'plays', 'allPlays', 'about', 'inning'],
    'halfInning': ['liveData', 'plays', 'allPlays', 'about', 'halfInning'],
    'atBat': ['liveData', 'plays', 'allPlays', 'about', 'atBatIndex'],
    'numOutsAtBat': ['liveData', 'plays', 'allPlays', 'count', 'outs'],
    'rbis': ['liveData', 'plays', 'allPlays', 'result', 'rbi'],
}

defaultGame = {
    'gamePk': ['gamePk'],
    'date': ['gameData', 'datetime', 'originalDate'],
    'homeTeam': ['gameData', 'teams', 'home', 'abbreviation'],
    'awayTeam': ['gameData', 'teams', 'away', 'abbreviation'],
}