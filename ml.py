# KNN alg

import math
import matplotlib.pyplot as plt
import csvRead

#calc euclidian distance
def edistance(point1, point2, labels):
    d = 0
    for i in labels:
        d += (point1[i] - point2[i])**2
    return math.sqrt(d)

def entropy(S):
    s = sum(S)
    ret = 0
    for i in S:
        ret -= (float(i)/s)*math.log(float(i)/s, 2)
    return ret


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


def average(d, k):
    sum = 0
    for i in d:
        sum += float(i[k])
    return sum / len(d)

# gets a set for all properties
def toDict(data):
    return {x:[y[x] for y in data] for x in data[0]}


data = csvRead.read_csv2('insects.csv')
labels = [(x, type(data[0][x])) for x in data[0]]
print labels
print data
d2 = toDict(filter(lambda x:x['c'] == 'k', data))
dg = toDict(filter(lambda x:x['c'] == 'g', data))
print d2
# s3 = {x:[(y['x'], y['y']) for y in filter(lambda i: i['c'] == x, data)] for x in set(d2['c'])}
# plt.scatter(s3['k'], s3['g'])
# plt.show()
# print s3
print set(d2['c'])
print entropy([5,9])
# print filter(lambda x: x['c'] == 'k', data)
# print average(data, 'x')
# print toSet(data)['c']


#new value to predict for
# X = {'c': None, 'x': 1.942, 'y':6.43}
#
# a = guess(X, data, 10)
#
# print a


