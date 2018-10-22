## 2 tasks run simultanoiusly (switching) in one thread
# def g():
#     yield 0
#
# print(dir(g()))

#############
###########  2 tasks - main() and f()

def coroutine(f):
    gen = f()
    next(gen)
    return gen

#@async de
@coroutine
def f():
   i = yield
   print("f: ", i)

   print(id(i))

   i = yield + 1
   print("f: ", i)

   print(id(i))

   yield i + 1


@coroutine
def g():
    while True:
        try:
            i = yield
        except ValueError:
            print('Value Eror ###')
        else:
            print("g_i <{}>) : ", format(i))



def main():
    i = f.send(1)
    print("main: ",i)
    i = f.send(i + 1)
    print("main: ", i)

main()

###  main() calls f()
#   main <= callback form f()

g.send(1)
g.throw(ValueError)
g.close()
g.send(1)



