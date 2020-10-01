
from functools import reduce

def f(x):
    return x**2


def map_test():
    L1=[1,2,3,4,5,6,7,8,9]
    L2=map(f,L1)
    print(list(L2))


def add(x,y):
    return x+y

def fn(x,y):
    return x*10+y

def reduce_test():
    print(reduce(add,[1,2,3,4,5,6]))
    print(reduce(fn,[1,3,4,8]))




# map_test()
reduce_test()
