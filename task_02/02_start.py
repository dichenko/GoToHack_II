#открываем файл, читаем мего построчно
with open('events_01.csv') as f:
    data = f.readlines()

#отрезаем от каждой строки символ переноса строки
for i in range(len(data)):
    data[i] = data[i][:-1]


#делим строку по запятым, получаем список вместо строки
for i in range(len(data)):
    data[i] = list(data[i].split(','))


#Превращаем все значения в целочисленные
for i in range(len(data)):
    for k in range(len(data[0])):
        if k != 1:
            data[i][k] = int(data[i][k])


#Создаем новый словарь, состоящий из ключа - User_ID и значений - словарь словарей step_fake_id: [time1, time2]
#открываем новый файл

with open('course-217-structure_fake_id.CSV') as f:
    strukture = f.readlines()

#отрезаем от каждой строки символ переноса строки
for i in range(len(strukture)):
    strukture[i] = strukture[i][:-1]


#делим строку по запятым, получаем список вместо строки
for i in range(len(strukture)):
    strukture[i] = list(strukture[i].split(';'))


#Превращаем все значения в целочисленные
for i in range(1,len(strukture)):
    for k in range(len(strukture[0])):
        if k != 7:
            strukture[i][k] = int(strukture[i][k])


struk_new = {}

#В новый словарь struk_new сохраняем только [step_id, fake_step_id]
for i in range(1,len(strukture)):
    struk_new[strukture[i][5]] = strukture[i][9]


#В список событий data заносим в каждую строчку дополнительный параметр fake_step_id

for i in range( len(data)):
    data[i].append(struk_new[data[i][2]])


#Из data создаем  словарь со значениями user_id {user_id:[[step1, time1, ...]}

user_dict = {}
for i in range(len(data)):
    if data[i][0] in user_dict.keys():
        user_dict[data[i][0]].append(data[i][1:])
    else:
        user_dict[data[i][0]] = [data[i][1:]]

for key in user_dict:
    print(key, user_dict[key])




