def a():
    print('a() start')
    b()
    d()
def b():
    print('b() starts')
    c()
    print('b() returns')
    
def c():
    print('c() starts')
    print('c() returns')
    
def d():
    print('d() start')
    print('d() returns')
    
a()