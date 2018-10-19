class NullObject:
    def __getattr__(self, name):
        return lambda *args, **kwargs: self

n = NullObject()
n.f()
n.g(2,3, a =5)
n.a

# try:
#     main()
# except
#     pass