def powtorz(n):
    def powtorz_nrazy(f):
        def opakowanie(*args, **kwds):
            for i in range(n):
                ret = f(*args, **kwds)
            return ret
        return opakowanie
    return powtorz_nrazy




@powtorz(5)
def bar():
    print('Funkcja bar')

bar()
