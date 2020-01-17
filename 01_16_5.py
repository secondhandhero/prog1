
def foo(x,y):
    print('jakis komunikat ',x,y)


from functools import wraps
def pokaz_wywolanie(f):
    @wraps(f)
    def opakowanie(*args, **kwds):
        print('Wywoluje:', f.__name__, 'i argumenty:', args)
        return f(*args, **kwds)
    return opakowanie

foo = pokaz_wywolanie(foo)
foo(2,5)

@pokaz_wywolanie

def bar(x):
    print("inny komunikat %d" %x)

bar(1)


