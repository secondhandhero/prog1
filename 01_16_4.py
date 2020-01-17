
def foo(x,y):
    print('jakis komunikat ',x,y)

def pokaz_wywolanie(f):
    def opakowanie(*args, **kwds):
        print('Wywoluje:', f.__name__, 'i argumenty:', args)
        return f(*args, **kwds)
    opakowanie.__name__ = f.__name__
    opakowanie.__doc__ = f.__doc__
    opakowanie.__module__ = f.__module__
    opakowanie.__dict__.update(f.__dict__)
    return opakowanie

foo = pokaz_wywolanie(foo)
foo(2,5)

@pokaz_wywolanie

def bar(x):
    print("inny komunikat %d" %x)

bar(1)
