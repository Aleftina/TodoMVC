## throw()  -


@coroutine
def g():
    while True:
        try:
            i = yield
        except ValueError:
            print('Value Eror ###')
        else:
            print("g_i <{}) : ", format(i))