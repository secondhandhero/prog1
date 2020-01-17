class pr:
    def fun(self,x):
        return 2 * x


print(pr().fun(2)) # wywołanie metody bez zainicjowania obiektu



p=pr()
g=p.fun(2)
print(g)

class tr:
    def fff(x):
        return 3 * x

tr.f=staticmethod(tr.fff)

print(tr.f(4))