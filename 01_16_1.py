
def foo():
    print('jakis komunikat')



def pokaz_wywolanie(f):
    print('Wywoluje:', f.__name__)
    return f

foo = pokaz_wywolanie(foo)
foo()




@pokaz_wywolanie
def bar(x):
    print('inny komunikat',x)

bar(1)
