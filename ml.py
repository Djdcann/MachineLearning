import math

def edistance(point1, point2, labels):
    d = 0
    for i in labels:
        d += (point1[i] - point2[i])**2
    return math.sqrt(d)


def guess(inX, dataset, k):
    ed = []
    for i in dataset:
        ed.append([edistance(inX, i, ['x', 'y']), i])
    ed.sort()
    return ed[:k]



csv = open("insects.csv", "r")

data = []
keys = []

#collect keys from 1st line and init data
for i in csv.readline()[:-1].split(','):
    keys.append(i)

#fill data with values
for i in csv.readlines():
    obj = {}
    for key, val in zip(keys, i[:-1].split(',')):
        if key != 'c':
            obj[key] = float(val)
        else:
            obj[key] = val
    data.append(obj)

#print data
csv.close()

X = {'c': None, 'x': 5.258, 'y':5.068520}

a = guess(X, data, 5)

print a


