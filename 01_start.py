import pickle

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

#print(*data)

s = {}
# Создаем словарь, где содержится время начала курса каждого пользователя
for i in range(len(data)):
    if data[i][0] not in s.keys():
        s[data[i][0]] = data[i][3]
    else:
          if data[i][3] < s[data[i][0]]:
              s[data[i][0]] = data[i][3]

#Консервируем  словарь содержащий время начала курса для каждого пользователя
with open('dict_of_fist_steps.pickle', 'wb') as f:
    pickle.dump(s, f)

print('OK')


