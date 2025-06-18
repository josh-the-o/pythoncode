"""lambda function"""
from functools import reduce

goat = 'lambda homework'
print(goat)

print('=============map=============')

list_ = (49, 97, 84, 76, 87, 49, 39)
_list = list(map(lambda x: list, list_))
print(_list)

print('==============reduce=============')
red_list = (13, 23, 11, 8, 10, 12)
_reduce = reduce((lambda x, y: x * y), red_list)
print(_reduce)

print('==============filter===========')
_filter = (54, 86, 12, 45, 30, 58, 96, 87, 34)
filter_ = list(filter(lambda x: (x % 3 == 0), _filter))
print('Numbers divisible by 3 are', filter_)
