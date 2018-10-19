class A:
    def __init__(self, x, **kwargs):
        print('A')
        self.x = x
        super().__init__(**kwargs)

class B(A):
    def __init__(self, y, **kwargs):
        print('B')
        self.y= y
        super.__init__(**kwargs)

class C(A):
    def __init__(self, z, **kwargs):
        print('C')
        self.z =z
        super.__init__(**kwargs)

class D( B, C):
    def __init__(self, x ,y, z, **kwargs ):
        print('D')
        super.__init__()




