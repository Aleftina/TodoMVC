class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return "Person('{}', {})".format(self.name, self.age)
    def __eq__(self, other):
        return self.name == other.name  #and self.age == other.age
    def __lt__(self, other):
        return self.name < other.name
    def __hash__(self):
        return hash(self.name)





p = Person('Bill', 24)
#p
str(p)
print(p)

p1 = Person('Phill', 28)
print(p == p1)
print(id(p))
print(id(p1))

## sort
p2 = Person('George', 24)
l = [p2, p1, p]
print(l)
l.sort()
print(l)

## creat dict
d={}
d[p] = 1
d[p1] = 2
print('\n',d)
print(hash(p1))
print(hash('a'))
print(hash('a'))
#d[Person('Olga', 27)] = 32

# functools total_ordering