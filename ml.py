# KNN alg

import math
import csvRead

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


def average(d, k):
    sum = 0
    for i in d:
        sum += float(i[k])
    return sum / len(d)

# gets a set for all properties
def toSet(d):
    ret = {}
    for i in d:
        for k in i:
            if k not in ret:
                ret[k] = set()
            ret[k].add(i[k])

    return ret


data = csvRead.read_csv2('insects.csv')
print filter(lambda x: x['c'] == 'k', data)
print average(data, 'x')
print toSet(data)['c']


#new value to predict for
# X = {'c': None, 'x': 1.942, 'y':6.43}
#
# a = guess(X, data, 10)
#
# print a


