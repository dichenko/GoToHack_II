
with open('course-217-events.csv') as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i].strip()
    data[i] = data[i].split(',')
    for k in range(len(data[i])):
        if k != 1:
            data[i][k] = int(data[i][k])
'''  data = [
[49, 'viewed', 39715, 1464945243],
[148, 'passed', 42384, 1464945152],
[148, 'discovered', 42384, 1464945152],
     ]  '''

with open('course-217-structure.csv') as f:
    struk = f.readlines()

for i in range(len(struk)):
    struk[i] = struk[i].strip()
    struk[i] = struk[i].split(',')
    for k in range(len(struk[i])):
        if k != 7:
            struk[i][k] = int(struk[i][k])
'''struk = [
[217, 614, 2, 13228, 2, 38842, 1, 'text', 0],
[217, 614, 2, 13228, 2, 39715, 6, 'code', 1],
[217, 614, 2, 13228, 2, 39716, 7, 'code', 1]   ]'''

step_cost = {}

for el in struk:
    step_cost[el[5]] =  el[8]

'''step_cost = {
step_id:cost
41478: 1,
53255: 0,
41480: 1,
41481: 1,
41482: 0,
40459: 0   }
 '''

for el in data:
    el.append(step_cost[el[2]])

'''  data = [
[49, 'viewed', 39715, 1464945243, 1],
[148, 'passed', 42384, 1464945152, 0],
[148, 'discovered', 42384, 1464945152, 1],
     ]  '''

dict_of_users = {}

for el in data:
    if el[0] in dict_of_users.keys():
        dict_of_users[el[0]] += [el]
    else:
        dict_of_users[el[0]] =[el]

'''
dict_of_users = {
662: [
    [662, 'viewed', 41101, 1463626917, 1]
    [662, 'viewed', 44393, 1463626897, 0]
    [662, 'viewed', 44392, 1463626871, 0]
    [662, 'viewed', 44391, 1463626849, 0]
    ]
}
    '''


#Отсортирим историю каждого юзера по времени
for user in dict_of_users:
    dict_of_users[user].sort(key = lambda x: x[3])


start_time = {}

for user in dict_of_users:
    start_time[user] = dict_of_users[user][0][3]


'''
start_time = {
1 : 1463664235
2 : 1463630591
3 : 1463625716
}
'''

finish_time = {}

for user in dict_of_users:
    sum = 0
    x = dict_of_users[user] ## list of lists
    i = 0
    while sum < 24 and i < len(x):
        sum += x[i][4]
        i += 1
    if sum == 24:
        finish_time[user] = x[i-1][3]


'''
finish_time = {
1 : 1463664235
2 : 1463630591
3 : 1463625716
}
'''

delta_time = {}
for key in finish_time:
    delta_time[key] = finish_time[key] - start_time[key]

delta_time_list = []

for key in delta_time:
    delta_time_list.append([key, delta_time[key]])

delta_time_list.sort(key = lambda x: x[1])

for i in range(10):
    print(delta_time_list[i][0], end = ',', sep = '')



