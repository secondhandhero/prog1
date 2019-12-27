# program testowy 1

import matplotlib.pyplot as pl


class CSzyfrant:

     def __init__(self,key):
        self.klucz=key

     def szyfruj(self, data):
        if data < 0:
            data = data + 256
        return ((data + self.klucz) % 256)


for k in range(100, 220, 40):
    szyfrant = CSzyfrant(k)
    x = []
    y = []

    for a in range(-255, 256, 1):
        x.append(a)
        y.append(szyfrant.szyfruj(a))

    pl.plot(x, y, label=szyfrant.klucz)

pl.grid()
pl.legend(loc='best')
pl.show()
