import csv
import runtime_efficiency
import re

@runtime_efficiency.profile
def read_csv(path):
    with open(path) as csvfile:
        return [i for i in csv.DictReader(csvfile)]

# OLD METHOD
@runtime_efficiency.profile
def read_csv2(path):
    csv = open(path, 'r')
    data = []
    keys = []
    # collect keys from 1st line and init data
    for i in csv.readline().rstrip().split(','):
        keys.append(i)
    # fill data with values
    for i in csv.readlines():
        obj = {}
        for key, val in zip(keys, i.rstrip().split(',')):
            if re.match(r'\d*\.?\d+', val):
                obj[key] = float(val)
            else:
                obj[key] = val
        data.append(obj)

    return data


def __test():
    for i in xrange(500):
        d1 = read_csv('insects.csv')
        d2 = read_csv2('insects.csv')
    print d1
    print d2
    runtime_efficiency.print_prof_data()
