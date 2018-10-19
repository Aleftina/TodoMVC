class MyList:
    def __init__(self, l=[]):
        self._l = l.copy()
    def __repr__(self):
        return repr(self._l)
    def __len__(self):
        return len(self._l)
    def add(self, other):
        self._l.append(other)
    def __setitem__(self, key, value):
        self._l[key] = value
    def __getitem__(self, index):
        print("index = ",index)
        if isinstance(index, int):
            return self._l[index]
        elif isinstance(index, (int, slice)):
            return [self._l[index]]
        elif isinstance(index, tuple):
            return [self._l[i] for i in index]
        elif index == ... :
            return self._l.copy()
        else:
            raise IndexError
    def __contains__(self, item):
        return item in self._l
    def __iter__(self):
        # self._l = 0
        # return self
        return MyListIterator(self._l)


    # def __next__(self):
    #     if self._i == len(self._l):
    #         raise StopIteration
    #     self._l += 1
    #     return self._l[self._i - 1]

class MyListIterator(object):
    def __init__(self, l):
        self._l = l
        self._l = 0
    # def __iter__(self):
    #     return self

    def __iter__(self):
        for i in self._l:
            yield i

    def __next__(self):
        if self._i == len(self._l):
            raise StopIteration
        self._l += 1
        return self._l[self._i - 1]


l = MyList([1,2,3])
l1 = [1,2,3]
l = MyList(l1)
l1[0] = 0
print(l)
print(l1)
print(l[0])

print("#")

s= slice(1,3)
l1 = [1,2,3,4,5]
print(l1[s])
i = iter(l1)
#print("iter = ",i)
# a= next(i)
# b =next(i)
# c = next(i)
# print(a + " "+ b + " "+ c)

# print(next(i)

print(l[1, 2:3, 2])

####  created iterator

l = MyList([1,2,3])
print("iter = ", i)
print(next(i))
print(next(i))
print(next(i))
# next(i)
# next(i)
#print(a + " "+ b + " "+ c)

# for i in l:
#     print(i)

def f():
    for i in range(5):
        yield i
        print("I m here")

print(f)
print(f())

gen = f()
print(next(gen))
print(next(gen))
print(next(gen))