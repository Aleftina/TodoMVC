import numbers

class Number:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return "Number(%s)" % self.value
    def __add__(self, other):
        if isinstance(other, numbers.Number):
            return Number(self.value + other)
        if isinstance(other, Number):
            return Number(self.value + other.value)




n = Number(5) + Number(2)
print(n)
print(n +4)
# print(Number(1) + 2)  - - error

print(isinstance(1,int))
print(isinstance(1.,(int, float)))
