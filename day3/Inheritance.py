## userdict - todo

class MyList(list):
    def sum(self):
        s= 0
        for item in self:
            s+=item
        return s

l = MyList([1,2,3])
print(dir(l))
print(l.__add__(l))
print(l.sum())

