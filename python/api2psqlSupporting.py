import psycopg2
import statsapi
import re

conn = psycopg2.connect(
    host = "localhost",
    database = "baseball",
    user = "karisch",
    password = "cocacola",
    port = 5432
)

pathListListDict = {
    'games': [
        ['gameData','game','pk'],
        ['gameData','game','type'],
        ['gameData','game','doubleHeader'],
        ['gameData','game','id'],
        ['gameData','game','gamedayType'],
        ['gameData','game','tiebreaker'],
        ['gameData','game','calendarEventID'],
        ['gameData','game','season'],
        ['gameData','game','seasonDisplay'],
        ['gameData','datetime','datetime'],
        ['gameData','datetime','originalDate'],
        ['gameData','datetime','dayNight'],
        ['gameData','datetime','time'],
        ['gameData','datetime','ampm'],
        ['gameData','teams','away','record','gamesPlayed'],
        ['gameData','teams','away','record','wins'],
        ['gameData','teams','away','record','losses'],
        ['gameData','teams','away','record','divisionLeader'],
        ['gameData','teams','home','record','gamesPlayed'],
        ['gameData','teams','home','record','wins'],
        ['gameData','teams','home','record','losses'],
        ['gameData','teams','home','record','divisionLeader'],
        ['gameData','venue','id'],
        ['gameData','weather','condition'],
        ['gameData','weather','temp'],
        ['gameData','weather','wind'],
        ['gameData','flags','noHitter'],
        ['gameData','flags','perfectGame'],
        ['gameData','teams','away','id'],
        ['gameData','teams','home','id']
    ],
    'actions': [
        ['gameData','game','pk'],
        ['liveData','plays','allPlays','atBatIndex'],
        ['liveData','plays','allPlays','playEvents','index'],
        ['liveData','plays','allPlays','playEvents','details','event'],
        ['liveData','plays','allPlays','playEvents','details','awayScore'],
        ['liveData','plays','allPlays','playEvents','details','homeScore'],
        ['liveData','plays','allPlays','playEvents','details','isScoringPlay'],
        ['liveData','plays','allPlays','playEvents','count','balls'],
        ['liveData','plays','allPlays','playEvents','count','strikes'],
        ['liveData','plays','allPlays','playEvents','count','outs'],
        ['liveData','plays','allPlays','playEvents','isPitch'],
        ['liveData','plays','allPlays','playEvents','player','id'],
        ['liveData','plays','allPlays','playEvents','details','description']
    ],
    'atBats': [
        ['gameData','game','pk'],
        ['liveData','plays','allPlays','about','atBatIndex'],
        ['liveData','plays','allPlays','result','event'],
        ['liveData','plays','allPlays','result','eventType'],
        ['liveData','plays','allPlays','result','description'],
        ['liveData','plays','allPlays','result','rbi'],
        ['liveData','plays','allPlays','result','awayScore'],
        ['liveData','plays','allPlays','result','homeScore'],
        ['liveData','plays','allPlays','about','halfInning'],
        ['liveData','plays','allPlays','about','inning'],
        ['liveData','plays','allPlays','about','isScoringPlay'],
        ['liveData','plays','allPlays','about','hasReview'],
        ['liveData','plays','allPlays','about','hasOut'],
        ['liveData','plays','allPlays','about','captivatingIndex'],
        ['liveData','plays','allPlays','matchup','batter','id'],
        ['liveData','plays','allPlays','matchup','batSide','code'],
        ['liveData','plays','allPlays','matchup','batSide','description'],
        ['liveData','plays','allPlays','matchup','pitcher','id']
    ],
    'pitches': [
        ['gameData','game','pk'],
        ['liveData','plays','allPlays','about','atBatIndex'],
        ['liveData','plays','allPlays','playEvents','index'],
        ['liveData','plays','allPlays','playEvents','details','code'],
        ['liveData','plays','allPlays','playEvents','details','description'],
        ['liveData','plays','allPlays','playEvents','details','isInPlay'],
        ['liveData','plays','allPlays','playEvents','details','isStrike'],
        ['liveData','plays','allPlays','playEvents','details','isBall'],
        ['liveData','plays','allPlays','playEvents','details','type','code'],
        ['liveData','plays','allPlays','playEvents','details','type','description'],
        ['liveData','plays','allPlays','playEvents','details','hasReview'],
        ['liveData','plays','allPlays','playEvents','count','balls'],
        ['liveData','plays','allPlays','playEvents','count','strikes'],
        ['liveData','plays','allPlays','playEvents','pitchData','startSpeed'],
        ['liveData','plays','allPlays','playEvents','pitchData','endSpeed'],
        ['liveData','plays','allPlays','playEvents','pitchData','strikeZoneTop'],
        ['liveData','plays','allPlays','playEvents','pitchData','strikeZoneBottom'],
        ['liveData','plays','allPlays','playEvents','pitchData','coordinates','aX'],
        ['liveData','plays','allPlays','playEvents','pitchData','coordinates','aY'],
        ['liveData','plays','allPlays','playEvents','pitchData','coordinates','aZ'],
        ['liveData','plays','allPlays','playEvents','pitchData','coordinates','pfxX'],
        ['liveData','plays','allPlays','playEvents','pitchData','coordinates','pfxZ'],
        ['liveData','plays','allPlays','playEvents','pitchData','coordinates','pX'],
        ['liveData','plays','allPlays','playEvents','pitchData','coordinates','pZ'],
        ['liveData','plays','allPlays','playEvents','pitchData','coordinates','vX0'],
        ['liveData','plays','allPlays','playEvents','pitchData','coordinates','vY0'],
        ['liveData','plays','allPlays','playEvents','pitchData','coordinates','vZ0'],
        ['liveData','plays','allPlays','playEvents','pitchData','coordinates','x'],
        ['liveData','plays','allPlays','playEvents','pitchData','coordinates','y'],
        ['liveData','plays','allPlays','playEvents','pitchData','coordinates','x0'],
        ['liveData','plays','allPlays','playEvents','pitchData','coordinates','y0'],
        ['liveData','plays','allPlays','playEvents','pitchData','coordinates','z0'],
        ['liveData','plays','allPlays','playEvents','pitchData','breaks','breakAngle'],
        ['liveData','plays','allPlays','playEvents','pitchData','breaks','breakLength'],
        ['liveData','plays','allPlays','playEvents','pitchData','breaks','breakY'],
        ['liveData','plays','allPlays','playEvents','pitchData','breaks','spinRate'],
        ['liveData','plays','allPlays','playEvents','pitchData','breaks','spinDirection'],
        ['liveData','plays','allPlays','playEvents','pitchData','zone'],
        ['liveData','plays','allPlays','playEvents','pitchData','typeConfidence'],
        ['liveData','plays','allPlays','playEvents','pitchData','plateTime'],
        ['liveData','plays','allPlays','playEvents','pitchData','extension'],
        ['liveData','plays','allPlays','playEvents','pitchNumber'],
        ['liveData','plays','allPlays','playEvents','hitData','launchSpeed'],
        ['liveData','plays','allPlays','playEvents','hitData','launchAngle'],
        ['liveData','plays','allPlays','playEvents','hitData','totalDistance'],
        ['liveData','plays','allPlays','playEvents','hitData','trajectory'],
        ['liveData','plays','allPlays','playEvents','hitData','hardness'],
        ['liveData','plays','allPlays','playEvents','hitData','location'],
        ['liveData','plays','allPlays','playEvents','hitData','coordinates','coordX'],
        ['liveData','plays','allPlays','playEvents','hitData','coordinates','coordY']
    ],
    'runners': [
        ['gameData','game','pk'],
        ['liveData','plays','allPlays','about','atBatIndex'],
        ['liveData','plays','allPlays','runners','details','playIndex'],
        ['liveData','plays','allPlays','runners','movement','start'],
        ['liveData','plays','allPlays','runners','movement','end'],
        ['liveData','plays','allPlays','runners','movement','isOut'],
        ['liveData','plays','allPlays','runners','movement','outNumber'],
        ['liveData','plays','allPlays','runners','details','eventType'],
        ['liveData','plays','allPlays','runners','details','movementReason'],
        ['liveData','plays','allPlays','runners','details','runner','id'],
        ['liveData','plays','allPlays','runners','details','isScoringEvent'],
        ['liveData','plays','allPlays','runners','details','rbi'],
        ['liveData','plays','allPlays','runners','details','earned'],
        ['liveData','plays','allPlays','runners','movement','outBase']
    ]
}

venueArgs = [
    (2526, 'McKechnie Field', 'Bradenton', 'Florida', 27.48535, -82.57076, -4, 'EDT', 6562, 'Grass', 'Open', 335, None, 400, None, 335),
    (2511, 'Joker Marchant Stadium', 'Lakeland', 'Florida', 28.07437, -81.95113, -4, 'EDT', 8500, 'Grass', 'Open', 340, None, 420, None, 340),
    (2856, 'Digital Domain Park', 'Port St. Lucie', 'Florida', 27.32478, -80.40471, -4, 'EDT', 7347, 'Grass', 'Open', 338, None, 410, None, 338),
    (2508, 'Ed Smith Stadium', 'Sarasota', 'Florida', 27.34795, -82.5174, -4, 'EDT', 7500, 'Grass', 'Open', 340, None, 400, None, 340),
    (2536, 'Dunedin Stadium', 'Dunedin', 'Florida', 28.00401, -82.78695, -4, 'EDT', 5509, 'Grass', 'Open', 335, None, 400, None, 327),
    (2504, 'Champion Stadium', 'Lake Buena Vista', 'Florida', 28.33725, -81.55613, -4, 'EDT', 9500, 'Grass', 'Open', 340, None, 400, None, 330),
    (2523, 'George M. Steinbrenner Field', 'Tampa', 'Florida', 27.97997, -82.50702, -4, 'EDT', 10387, 'Grass', 'Open', 318, None, 408, None, 314),
    (2506, 'City of Palms Park', 'Ft. Myers', 'Florida', None, None, None, None, 7431, 'Grass', 'Open', 330, None, 410, None, 330),
    (2530, 'Peoria Stadium', 'Peoria', 'Arizona', 33.63187, -112.23359, -7, 'MST', 10000, 'Grass', 'Open', 340, None, 410, None, 340),
    (2520, 'Roger Dean Stadium', 'Jupiter', 'Florida', 26.89084, -80.11677, -4, 'EDT', 6864, 'Grass', 'Open', 335, None, 400, None, 375),
    (2700, 'Bright House Networks Field', 'Clearwater', 'Florida', 27.97136, -82.73199, -4, 'EDT', 8500, 'Grass', 'Open', 329, None, 401, None, 330),
    (2514, 'Osceola County Stadium', 'Kissimmee', 'Florida', None, None, -4, 'EDT', 5300, 'Grass', 'Open', 330, None, 410, None, 330),
    (2534, 'Charlotte Sports Park', 'Port Charlotte', 'Florida', 26.99888, -82.18212, -4, 'EDT', 6000, 'Grass', 'Open', 343, None, 414, None, 343),
    (2501, 'Tucson Electric Park', 'Tucson', 'Arizona', None, None, -7, 'MST', 11578, 'Grass', 'Open', 340, None, 405, None, 340),
    (2507, 'Hohokam Park', 'Mesa', 'Arizona', 33.43831, -111.82973, -7, 'MST', 12575, 'Grass', 'Open', 340, None, 410, None, 350),
    (2603, 'Surprise Stadium', 'Surprise', 'Arizona', 33.62762, -112.37849, -7, 'MST', 10714, 'Grass', 'Open', 350, None, 400, None, 350),
    (2532, 'Scottsdale Stadium', 'Scottsdale', 'Arizona', 33.48869, -111.92099, -7, 'MST', 11500, 'Grass', 'Open', 360, None, 430, None, 330),
    (2500, 'Tempe Diablo Stadium', 'Tempe', 'Arizona', 33.40092, -111.9707, -7, 'MST', 9808, 'Grass', 'Open', 340, None, 420, None, 360),
    (2862, 'Hammond Stadium', 'Fort Myers', 'Florida', 26.53789, -81.84202, -4, 'EDT', 7500, 'Grass', 'Open', 330, None, 405, None, 330),
    (3834, 'Goodyear Ballpark', 'Goodyear', 'Arizona', 33.42892, -112.39027, -7, 'MST', None, 'Grass', 'Open', 340, None, 400, None, 340),
    (3809, 'Camelback Ranch', 'Glendale', 'Arizona', 33.51434, -112.29612, -7, 'MST', 13000, 'Grass', 'Open', 345, None, 410, None, 345),
    (2524, 'Phoenix Municipal Stadium', 'Phoenix', 'Arizona', None, None, None, None, 8776, 'Grass', 'Open', 345, None, 410, None, 345),
    (2513, 'Space Coast Stadium', 'Viera', 'Florida', None, None, None, None, 7200, 'Grass', 'Open', 340, None, 404, None, 340),
    (2518, 'Maryvale Baseball Park', 'Phoenix', 'Arizona', 33.49202, -112.1727, -7, 'MST', 7000, 'Grass', 'Open', 350, None, 400, None, 340),
    (2538, 'US West Sports Complex, Hi Corbett Field', 'Tucson', 'Arizona', None, None, None, None, 8665, 'Grass', 'Open', 366, None, 392, None, 348),
    (4189, 'Tianmu Baseball Stadium', 'Taipei', None, None, None, None, None, 10500, 'Grass', 'Open', 325, None, 400, None, 325),
    (2503, 'Cashman Field', 'Las Vegas', 'Nevada', None, None, -7, 'PDT', 9334, 'Grass', 'Open', 328, None, 433, None, 328),
    (4190, 'Chengcing Lake Baseball Stadium', 'Kaohsiung', None, None, None, None, None, 20000, 'Grass', 'Open', 328, None, 400, None, 328),
    (3070, 'Hector Espino', 'Hermosillo', None, None, None, None, None, None, 'Grass', 'Open', None, None, None, None, None),
    (2521, 'Knights Stadium', 'Charlotte', 'North Carolina', None, None, None, None, 10002, 'Grass', 'Open', 325, None, 400, None, 325),
    (1, 'Angel Stadium of Anaheim', 'Anaheim', 'California', 33.80019044, -117.8823996, -7, 'PDT', 45389, 'Grass', 'Open', 330, 387, 400, 370, 330),
    (22, 'Dodger Stadium', 'Los Angeles', 'California', 34.07368, -118.24053, -7, 'PDT', 56000, 'Grass', 'Open', 330, 385, 395, 385, 330),
    (2395, 'AT&T Park', 'San Francisco', 'California', 37.778383, -122.389448, -7, 'PDT', 41915, 'Grass', 'Open', 339, 364, 399, 421, 309),
    (12, 'Tropicana Field', 'St. Petersburg', 'Florida', 27.767778, -82.6525, -4, 'EDT', 36973, 'Artificial', 'Dome', 315, 410, 404, 404, 322),
    (3312, 'Target Field', 'Minneapolis', 'Minnesota', 44.981829, -93.277891, -5, 'CDT', 39504, 'Grass', 'Open', 339, 377, 404, 367, 328),
    (2683, 'Isotopes Park', 'Albuquerque', 'New Mexico', None, None, -6, 'MDT', 11124, 'Grass', 'Open', 360, None, 410, None, 340),
    (2681, 'Citizens Bank Park', 'Philadelphia', 'Pennsylvania', 39.90539086, -75.16716957, -4, 'EDT', 43647, 'Grass', 'Open', 329, 381, 401, 398, 330),
    (16, 'Turner Field', 'Atlanta', 'Georgia', None, None, None, None, 50062, 'Grass', 'Open', 335, 380, 401, 390, 330),
    (2852, 'The Baseball Grounds of Jacksonville', 'Jacksonville', 'Florida', None, None, -4, 'EDT', 11000, 'Grass', 'Open', 321, None, 420, None, 317),
    (13, 'Rangers Ballpark in Arlington', 'Arlington', 'Texas', 32.751321, -97.082682, -5, 'CDT', 49170, 'Grass', 'Open', 332, 390, 400, 407, 325),
    (2392, 'Minute Maid Park', 'Houston', 'Texas', 29.756967, -95.355509, -5, 'CDT', 40976, 'Grass', 'Retractable', 315, 362, 435, 373, 326),
    (32, 'Miller Park', 'Milwaukee', 'Wisconsin', 43.02838, -87.97099, -5, 'CDT', 41900, 'Grass', 'Retractable', 344, 371, 400, 374, 345),
    (2516, 'The Diamond', 'Lake Elsinore', 'California', None, None, -7, 'PDT', 7866, 'Grass', 'Open', 330, None, 400, None, 310),
    (15, 'Chase Field', 'Phoenix', 'Arizona', 33.445302, -112.066687, -7, 'MST', 48652, 'Grass', 'Retractable', 328, 412, 407, 414, 335),
    (2755, 'Dr. Pepper Ballpark', 'Frisco', 'Texas', None, None, -5, 'CDT', 10000, 'Grass', 'Open', 335, None, 409, None, 335),
    (2541, 'Durham Bulls Athletic Park', 'Durham', 'North Carolina', None, None, -4, 'EDT', 10000, 'Grass', 'Open', 305, None, 400, None, 327),
    (2723, 'NewBridge Bank Park', 'Greensboro', 'North Carolina', None, None, -4, 'EDT', 8000, 'Grass', 'Open', None, None, None, None, None),
    (3309, 'Nationals Park', 'Washington', 'District of Columbia', 38.872861, -77.007501, -4, 'EDT', 41888, 'Grass', 'Open', 336, 377, 403, 370, 335),
    (10, 'Oakland Coliseum', 'Oakland', 'California', 37.751511, -122.200698, -7, 'PDT', 35067, 'Grass', 'Open', 330, 388, 400, 388, 330),
    (3, 'Fenway Park', 'Boston', 'Massachusetts', 42.346456, -71.097441, -4, 'EDT', 37294, 'Grass', 'Open', 310, 390, 420, 380, 302),
    (2602, 'Great American Ball Park', 'Cincinnati', 'Ohio', 39.097389, -84.506611, -4, 'EDT', 42319, 'Grass', 'Open', 328, 379, 404, 370, 325),
    (3289, 'Citi Field', 'Flushing', 'New York', 40.75753012, -73.84559155, -4, 'EDT', 45000, 'Grass', 'Open', 335, 379, 408, 383, 330),
    (31, 'PNC Park', 'Pittsburgh', 'Pennsylvania', 40.446904, -80.005753, -4, 'EDT', 38362, 'Grass', 'Open', 325, 410, 399, 375, 320),
    (4, 'U.S. Cellular Field', 'Chicago', 'Illinois', 41.83, -87.634167, -5, 'CDT', 40615, 'Grass', 'Open', 330, 377, 400, 372, 335),
    (7, 'Kauffman Stadium', 'Kansas City', 'Missouri', 39.051567, -94.480483, -5, 'CDT', 37903, 'Grass', 'Open', 330, 385, 410, 385, 330),
    (2394, 'Comerica Park', 'Detroit', 'Michigan', 42.3391151, -83.048695, -4, 'EDT', 41255, 'Grass', 'Open', 345, 370, 420, 365, 330),
    (2, 'Oriole Park at Camden Yards', 'Baltimore', 'Maryland', 39.283787, -76.621689, -4, 'EDT', 48290, 'Grass', 'Open', 333, 410, 400, 373, 318),
    (19, 'Coors Field', 'Denver', 'Colorado', 39.756042, -104.994136, -6, 'MDT', 50445, 'Grass', 'Open', 347, 420, 415, 424, 350),
    (20, 'Sun Life Stadium', 'Miami', 'Florida', None, None, None, None, 36331, 'Grass', 'Open', 330, 385, 434, 385, 345),
    (17, 'Wrigley Field', 'Chicago', 'Illinois', 41.948171, -87.655503, -5, 'CDT', 41210, 'Grass', 'Open', 355, 368, 400, 368, 353),
    (5, 'Progressive Field', 'Cleveland', 'Ohio', 41.495861, -81.685255, -4, 'EDT', 45569, 'Grass', 'Open', 325, 410, 405, 375, 325),
    (2889, 'Busch Stadium', 'St. Louis', 'Missouri', 38.62256667, -90.19286667, -5, 'CDT', 43975, 'Grass', 'Open', 336, 390, 400, 390, 335),
    (2680, 'PETCO Park', 'San Diego', 'California', 32.707861, -117.157278, -7, 'PDT', 42691, 'Grass', 'Open', 334, 402, 396, 411, 322),
    (680, 'Safeco Field', 'Seattle', 'Washington', 47.591333, -122.33251, -7, 'PDT', 47878, 'Grass', 'Retractable', 331, 390, 405, 387, 327),
    (14, 'Rogers Centre', 'Toronto', None, 43.64155, -79.38915, -4, 'EDT', 49539, 'Artificial', 'Retractable', 328, 375, 404, 375, 328),
    (3313, 'Yankee Stadium', 'Bronx', 'New York', 40.82919482, -73.9264977, -4, 'EDT', 50287, 'Grass', 'Open', 318, 399, 408, 385, 314),
    (2535, 'Hiram Bithorn Stadium', 'San Juan', None, 18.41666, -66.072817, -4, 'AST', 19778, 'Artificial', 'Open', 325, 375, 404, 375, 325)
]

commandDict = {
        'games': """
            INSERT INTO {schema}.games(
                pk,
                type,
                "doubleHeader",
                id,
                "gamedayType",
                "tieBreaker",
                "calendarEventID",
                season,
                "seasonDisplay",
                datetime,
                "originalDate",
                "dayNight",
                time,
                ampm,
                "awayGamesPlayed",
                "awayWins",
                "awayLosses",
                "awayDivisionLeader",
                "homeGamesPlayed",
                "homeWins",
                "homeLosses",
                "homeDivisionLeader",
                "venueID",
                "weatherConditions",
                temp,
                wind,
                "noHitter",
                "perfectGame",
                "awayId",
                "homeId")
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
        'actions': """
            INSERT INTO {schema}.actions(
                "gamePk",
                "atBatIndex",
                "actionIndex",
                "eventType",
                "awayScore",
                "homeScore",
                "isScoringPlay",
                balls,
                strikes,
                outs,
                "isPitch",
                "playerId",
                "eventDescription"
                )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
        'atBats': """
            INSERT INTO {schema}.atbats(
                "gamePk",
                "atBatIndex",
                result,
                "resultType",
                "resultDesc",
                rbi,
                "awayScore",
                "homeScore",
                "isTopInning",
                inning,
                "isScoringPlay",
                "hasReview",
                "hasOut",
                "captivatingIndex",
                "batterID",
                "batSideCode",
                "batSideDesc",
                "pitcherID"
                )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
        'pitches': """
            INSERT INTO {schema}.pitches(
                "gamePk",
                "atBatIndex",
                "pitchIndex",
                "callCode",
                "callDesc",
                "isInPlay",
                "isStrike",
                "isBall",
                "typeCode",
                "typeDesc",
                "hasReview",
                "countBalls",
                "countStrikes",
                "startSpeed",
                "endSpeed",
                "szTop",
                "szBottom",
                "aX",
                "aY",
                "aZ",
                "pfxX",
                "pfxZ",
                "pX",
                "pZ",
                "vX0",
                "vY0",
                "vZ0",
                x,
                y,
                "x0",
                "y0",
                "z0",
                "breakAngle",
                "breakLength",
                "breakY",
                "spinRate",
                "spinDirection",
                zone,
                "typeConfidence",
                "plateTime",
                extension,
                "pitchNumber",
                "launchSpeed",
                "launchAngle",
                "totalDistance",
                trajectory,
                hardness,
                location,
                "coordX",
                "coordY"
                )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
        'runners': """
            INSERT INTO {schema}.runners(
                "gamePk",
                "atBatIndex",
                "playIndex",
                "startBase",
                "endBase",
                "isOut",
                "outNumber",
                "eventType",
                "movementReason",
                "runnerId",
                "isScoringEvent",
                rbi,
                earned,
                "outBase",
                "runnerIndex"
                )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
    }

def dictTry(dict, keyList):
    active = dict
    for i in range(len(keyList)):
        if keyList[i] not in active.keys():
            return None
        elif i == len(keyList) - 1:
            return active[keyList[i]]
        else:
            active = active[keyList[i]]

#function to generate the unique game pk (ID) for each game played between the dates provided (inclusive)
#inputs: startDate is the beginning of the period of games to be pulled ('mm/dd/yyyy' string format)
#        endDate is the last day of the period ('mm/dd/yyyy' string format)
#output: a list of game pks
def generateGamePksFromDates(startDate, endDate):
    firstDateSearch = re.search('(\d\d).(\d\d).(\d\d\d\d)', startDate)
    lastDateSearch = re.search('(\d\d).(\d\d).(\d\d\d\d)', endDate)

    firstDateYear = int(firstDateSearch.group(3))
    lastDateYear = int(lastDateSearch.group(3))

    years = list(range(firstDateYear, lastDateYear + 1))

    if len(years) == 1:
        sched = statsapi.schedule(start_date=startDate, end_date=endDate)
    else:

        activeStart = startDate
        
        sched = []
        for year in years:
            if year == years[-1]:
                activeEnd = endDate
            else:
                activeEnd = '12/31/' + str(year)

            sched += statsapi.schedule(start_date = activeStart, end_date = activeEnd)

            activeStart = '01/01/' + str(year + 1)

    gamePks = [x['game_id'] for x in sched] #list comp to pull the gamePk from each game scraped (come through in JSON format)
    return list(set(gamePks))
    #return gamePks

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
            return None #return 'NA' to be processed later
        temp = temp[path[i]] #move to next dictionary/list

    return(temp)

def generateGameArgs(gameJson, pathListList):
    outputList = []
    for pathList in pathListList:
        outputList.append(jsonFind(gameJson, pathList, []))
    
    return tuple(outputList)

def generateAtBatArgs(gameJson, pathListList):
    atBatList = jsonFind(gameJson, ['liveData','plays','allPlays'], [])

    outputList = []
    cnt = 0

    for atBat in atBatList:
        activeItems = []
        for pathList in pathListList:
            activeItems.append(jsonFind(gameJson, pathList, [cnt]))
            
        outputList.append(tuple(activeItems))

        cnt += 1

    return outputList

def generateActionArgs(gameJson, pathListList):
    atBatList = jsonFind(gameJson, ['liveData','plays','allPlays'], [])

    outputList = []
    cnt = 0

    for atBat in atBatList:
        for i in atBat['actionIndex']:
            activeItems = []
            for pathList in pathListList:
                activeItems.append(jsonFind(gameJson, pathList, [cnt, i]))

            if activeItems != []:
                outputList.append(tuple(activeItems))

        cnt += 1

    return outputList

def generatePitchArgs(gameJson, pathListList):
    atBatList = jsonFind(gameJson, ['liveData','plays','allPlays'], [])

    outputList = []
    cnt = 0

    for atBat in atBatList:
        for i in atBat['pitchIndex']:
            activeItems = []
            for pathList in pathListList:
                activeItems.append(jsonFind(gameJson, pathList, [cnt, i]))

            if activeItems != []:
                outputList.append(tuple(activeItems))

        cnt += 1

    return outputList

def generateRunnerArgs(gameJson, pathListList):
    atBatList = jsonFind(gameJson, ['liveData','plays','allPlays'], [])

    outputList = []
    cnt = 0

    for atBat in atBatList:
        for i in atBat['runnerIndex']:
            activeItems = []
            for pathList in pathListList:
                activeItems.append(jsonFind(gameJson, pathList, [cnt, i]))
            activeItems.append(i)

            if activeItems != []:
                outputList.append(tuple(activeItems))

        cnt += 1

    return outputList