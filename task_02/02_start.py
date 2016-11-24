#открываем файл, читаем его построчно
with open('course-217-events.csv') as f:
    data = f.readlines()

#отрезаем от каждой строки символ переноса
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

#словарь соответствия step_id и fake_step_id
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


#Сортируем список событий каждого пользователя по времени
for key in user_dict:
    user_dict[key].sort(key=lambda x: x[2])

#Проходим по каждому списку событий и удаляем из него события с одинаковым временем
for key in user_dict:
    for i in range(len(user_dict[key]) - 1):
        if user_dict[key][i] == user_dict[key][i+1]:
            user_dict[key][i] = "nop"

for key in user_dict:
    z = user_dict[key]
    for i in range(z.count('nop')):
        z.remove('nop')




# Создаем словарь, где для каждого fake_step_id будет значением количество пользователей,
#которое сделало возврат к этому степу vozvrat = {fake_step_id: val}
vozvrat = {}


#для каждого пользователя ищем степы с возвратом
#
for key in user_dict:  #Для каждого пользователя

    w = user_dict[key]
    passed_step_id = []  #Заводим список
    for i in range(len(w)): #По количеству записей
        q = w[i]
        fid = q[3]
        if fid not in passed_step_id:  #Если ещё не находили такой возвратный fid, работаем
            #Проходим по всему списку и ищем следующий степ
            for j in range(len(w)):
                p = w[j]
                #Если мы нашли следующий степ с бОльшим временем
                if (p[3] == fid + 1) and (p[2] > q[2]):
                    #Ищем fid с ещё бОльшим временем
                    for z in range(len(w)):
                        m = w[z]

                        if m[3] == fid and m[2] > p[2]:

                            if fid not in passed_step_id:
                                #print('user:', key, 'f_step_id:', fid)
                                passed_step_id.append(fid) #Добавляем fid  в список рассмотренных
                                if fid in vozvrat.keys():  #добавляем fid в список возвратных ++
                                    vozvrat[fid] += 1
                                else:
                                    vozvrat[fid] = 1


# Создаем словарь, где для каждого fake_step_id будет значением количество пользователей,
#которые приступали хоть раз к этому степу pristupali = {fake_step_id: val}
pristupali = {}

for key in user_dict:
    d = user_dict[key] #list of events
    passed_step_id = []
    for i in range(len(d)):
        event = d[i] #list, event
        fid = event[3]
        if fid not in passed_step_id:
            passed_step_id.append(fid)
            if fid in pristupali.keys():
                pristupali[fid] += 1
            else:
                pristupali[fid] = 1


#Для каждого возвратного степа находим долю пользователей  приступали/возвращались
#И заносим в новый словарь dolya
dolya = {}

for key in vozvrat:
    dolya[key] = vozvrat[key] / pristupali[key]

print(dolya)
dol = []
for key in dolya:
    dol.append([key, dolya[key]])

dol.sort(key = lambda x: x[1], reverse = True)
print (dol[:10])



