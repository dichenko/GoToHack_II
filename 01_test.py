
start_time = {}

a = [[1, 234], [1, 238], [1, 28], [2, 234], [5, 234], [5, 222] ]


for el in a:
    if el[0] not in start_time.keys():
        start_time[el[0]] = el[1]
    else:
        if  el[1] <  start_time[el[0]] :
            start_time[el[0]] = el[1]
print(start_time)
