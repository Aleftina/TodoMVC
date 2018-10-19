class A:
    def __getattribute__(self, name):
        print("Get attribute", name)
    def __setattr__(self, name, value):
        print("Sett attribute", name, value)
    def __delattr__(self, name):
        print("Dell attribute", name)
