import numpy
import math

def entropy(x):
    total = 0
    for i in x:
        total -= i*math.log(i, 2)

    return total

def gini(x):
    total = 1
    for i in x:
        total -= i**2

    return total


p1 = 5.0/8
p2 = 3.0/8

p3 = 3.0/5.0
p4 = 2.0/5.0

p5 = 1.0/3
p6 = 2.0/3
list = [p1,p2]

H = entropy(list)
print H
issmooth = H - 0.5*(entropy([0.75, 0.25]) + entropy([0.5,0.5]))
print gini(list)

H2 = entropy([0.75, 0.25])
print 'Is Heavy: ', H2 - 0.5*entropy([1.0]) - 0.5*entropy([0.5,0.5])
print 'Is Smelly: ', H2 - 0.25*entropy([1.0]) - 0.75*entropy([1.0])
print 'Is Spotted: ', H2 - 0.75*entropy([1.0/3,2.0/3]) - 0.25*entropy([1.0])
#choose is smooth first

