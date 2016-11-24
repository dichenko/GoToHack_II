#открываем файл, читаем мего построчно
with open('events_02.csv') as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i].strip()
    data[i] = data[i].split(',')
    for k in range(len(data[i])):
        if k != 1:
            data[i][k] = int(data[i][k])
'''*  data = [
[49, 'viewed', 39715, 1464945243],
[148, 'passed', 42384, 1464945152],
[148, 'discovered', 42384, 1464945152],
     ]  '''

print(data)