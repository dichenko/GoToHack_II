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
for i in range(1,len(data)):
    for k in range(len(data[0])):
        if k == 0 or k == 3:
            data[i][k] = int(data[i][k])

print(data)

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

print(strukture)

