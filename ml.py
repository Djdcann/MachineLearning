#KNN alg

import math

#calc euclidian distance
def edistance(point1, point2, labels):
    d = 0
    for i in labels:
        d += (point1[i] - point2[i])**2
    return math.sqrt(d)

#return list of length k of close points
def guess(inX, dataset, k):
    solve_for = None
    for i in inX:
        if inX[i] == None:
            solve_for = i
            break

    ed = []
    for i in dataset:
        ed.append([edistance(inX, i, ['x', 'y']), i[solve_for]])
    ed.sort()
    vals = {}
    for i in ed[:k]:
        if i[1] not in vals:
            vals[i[1]] = 1
        else:
            vals[i[1]]+=1
    return {kk: float(v) / k for kk, v in vals.items()}


#open csv to read
csv = open("insects.csv", "r")

data = []
keys = []

#collect keys from 1st line and init data
for i in csv.readline().rstrip().split(','):
    keys.append(i)

#fill data with values
for i in csv.readlines():
    obj = {}
    for key, val in zip(keys, i.rstrip().split(',')):
        if key != 'c':
            obj[key] = float(val)
        else:
            obj[key] = val
    data.append(obj)

#print data
csv.close()

#new value to predict for
X = {'c': None, 'x': 1.942, 'y':6.43}

a = guess(X, data, 10)

print a


