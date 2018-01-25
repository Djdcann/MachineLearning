import csv

def read_csv(path):
    with open(path) as csvfile:
        return csv.DictReader(csvfile)

# OLD METHOD
# @runtime_efficiency.profile
# def read_csv2(path):
#     csv = open(path, 'r')
#     data = []
#     keys = []
#     # collect keys from 1st line and init data
#     for i in csv.readline().rstrip().split(','):
#         keys.append(i)
#     # fill data with values
#     for i in csv.readlines():
#         obj = {}
#         for key, val in zip(keys, i.rstrip().split(',')):
#             obj[key] = val
#         data.append(obj)
#
#     return data


#runtime_efficiency.print_prof_data()