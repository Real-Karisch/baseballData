import statsapi

astros = statsapi.lookup_team(117)
astros = statsapi.lookup_team('hou')

altuve = statsapi.lookup_player('Jose Altuve')

sched_2019 = statsapi.schedule(start_date = '03/28/2019', end_date = '09/29/2019')

#print(type(altuve[0]))
#print('$$$$$$$$$$$$$$$$$')
#print(altuve[0]['nickName'])

print(len(sched_2019))
gamepk = [sched_2019[0]['game_id']]

for i in range(1, len(sched_2019)):
    gamepk.append(sched_2019[i]['game_id'])

print(gamepk)
print(len(gamepk))

#print(statsapi.get('team',{'teamId':143}))

#penis
#cuck
#testicles

