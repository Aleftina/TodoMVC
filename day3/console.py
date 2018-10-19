Python
3.7
.0(v3
.7
.0: 1
bf9cc5093, Jun
27
2018, 04: 59:51) [MSC v.1914 64 bit(AMD64)]
on
win32
Type
"copyright", "credits" or "license()"
for more information.
    >> >

    class Olga:


        pass

>> > Olga
<

class '__main__.Olga'>

>> > dir(Olga)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>> > B = Olga
>> > id(Olga)
43302072
>> > id(B)
43302072
>> > C = Olga()
>> > C
< __main__.Olga
object
at
0x0000000002C79E80 >
>> > D = A()
Traceback(most
recent
call
last):
File
"<pyshell#10>", line
1, in < module >
D = A()
NameError: name
'A' is not defined
>> > d = Olga()
>> > d
< __main__.Olga
object
at
0x0000000002C8C0B8 >
>> > C.x = 42
>> > x
Traceback(most
recent
call
last):
File
"<pyshell#14>", line
1, in < module >
x
NameError: name
'x' is not defined
>> > C.x
42
>> >  ##  duck typing
>> > vars(C)
{'x': 42}
>> > C.__dict_['y'] = 2
Traceback(most
recent
call
last):
File
"<pyshell#18>", line
1, in < module >
C.__dict_['y'] = 2
AttributeError: 'Olga'
object
has
no
attribute
'__dict_'
>> > C.__dict__['y'] = 2
>> > C.y
2
>> > C.__dict__
{'x': 42, 'y': 2}
>> > D = A()
Traceback(most
recent
call
last):
File
"<pyshell#22>", line
1, in < module >
D = A()
NameError: name
'A' is not defined
>> > D = Olga()
>> > vars(b)
Traceback(most
recent
call
last):
File
"<pyshell#24>", line
1, in < module >
vars(b)
NameError: name
'b' is not defined
>> > dir(Olga)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>> > D = C()
Traceback(most
recent
call
last):
File
"<pyshell#26>", line
1, in < module >
D = C()
TypeError: 'Olga'
object is not callable
>> > D.__class__
<

class '__main__.Olga'>

>> > D.__dict__
{}
>> > Olga.__dict__
mappingproxy({'__module__': '__main__', '__dict__': < attribute
'__dict__'
of
'Olga'
objects >, '__weakref__': < attribute
'__weakref__'
of
'Olga'
objects >, '__doc__': None})
>> > mappingproxy({'__module__': '__main__', '__dict__': < attribute
'__dict__'
of
'Olga'
objects >, '__weakref__': < attribute
'__weakref__'
of
'Olga'
objects >, '__doc__': None})
SyntaxError: invalid
syntax
>> >

class A:

    def f(self, x):
        print(self)
        self.x = x

>> > a = A()
>> > A.f
< function
A.f
at
0x0000000002D15400 >
>> > a.f
< bound
method
A.f
of < __main__.A
object
at
0x0000000002D067F0 >>
>> > a
< __main__.A
object
at
0x0000000002D067F0 >
>> > a.f(42)
< __main__.A
object
at
0x0000000002D067F0 >
>> > vars(a)
{'x': 42}
>> >
>> >

class B:
    pass


b = B()
SyntaxError: invalid
syntax
>> >

class B:
    pass

>> > b = B()
>> > A.f(b, 2)
< __main__.B
object
at
0x0000000002D069E8 >
>> > b
< __main__.B
object
at
0x0000000002D069E8 >
>> > b.f
Traceback(most
recent
call
last):
File
"<pyshell#49>", line
1, in < module >
b.f
AttributeError: 'B'
object
has
no
attribute
'f'
>> >
>> >
>> >

>> >
>> >
>> >

class A:
    def f(self):
        print('A')

>> > a = A()
>> > a.f()
A
>> >
>> > vars(a)
{}
>> > a.x = 42
>> >
>> > vars(a)
{'x': 42}
>> >
>> >

class B:
    def g(self):
        print('B')

>> > a.__class__ = B
>> > vars(a)
{'x': 42}
>> > a.f()
Traceback(most
recent
call
last):
File
"<pyshell#73>", line
1, in < module >
a.f()
AttributeError: 'B'
object
has
no
attribute
'f'
>> >
>> > a.g()
B
>> >

def f(self):
    print('B')

>> > B.f = f
>> > a.f()
B
>> >
>> >
>> >
>> > A.__bases__
(<


class 'object'>, )
>> >
>> >
>> >


class A:
    pass

class A(object):
    pass

dir(A)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#  '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
#  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']


 # inheritance
A.__bases__

        C.__bases__
'__bases__'
B = A
B.__bases__



class B(A):
    pass

B.__bases__

 # c3 algorithm to resolve multiple inheritance



class C(A): pass

class E(A): pass

class C(B): pass

class D(B): pass

class F(C, D, E): pass

>> > F.mro()
[ <


class '__main__.F'>, < class '__main__.C' >, < class '__main__.D' >, < class '__main__.B' >, < class '__main__.E' >, < class '__main__.A' >, < class 'object' >]
>> >