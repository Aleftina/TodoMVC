def f_a():
    print('A')
def f_b():
    print('B')
def f_c():
    print('C')

class Observable:

    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    # def event(self):
    #     print('Event')
    #     for observer in self.observers:
    #         observer()

    def notify(self, f):
        def wrapper(*args, **kwargs):
            result = f(*args, **kwargs)
            for observer in self.observers:
                return result
        return wrapper

o = Observable()

@o.notify
def event():
    print('Event')

o.attach(f_a)
o.attach(f_b)
event()
o.detach(f_a)
o.attach(f_c)
event()


# attach(f_a)
# attach(f_b)
# event()
# detach(f_b)
# attach(f_c)
# event()
