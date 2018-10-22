## generators
## lazy run
## itertools

def f():
    for i in range(5):
        #yeld = return
        yield i

gen = f()
print(list(gen))

################  receive numbers: n^2 < 100

import itertools
inf_list = itertools.count(0)

l1 = list(itertools.takewhile(lambda x: x*x< 100, inf_list))
print(l1)

####  groupby  - to save stack of pixels

data = [0]*10 + [1]*1 + [0]*4
list01 = list(itertools.groupby(data))
print(list01)
#[(value, len(list01))] itertools.groupby(data))


##  combinatorika point 2d, receive all combinatoions of naibours

list = list(itertools.product([-1, 0, 1], repeat=2))
print(list)
list(itertools.combinations([-1, 0, 1], 2))
print("comb = ",list)

#  resheto eratosphena - find simple numbers
# find 10 simple numbers



