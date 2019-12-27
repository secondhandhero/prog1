# program testowy 1

import matplotlib.pyplot as pl

class CSzyfrant:

    klucz=0
    def szyfruj(self,data):

            if data < 0:
                data = data+256
            return ((data+self.klucz) % 256)

szyfrant=CSzyfrant()

for szyfrant.klucz in range(100, 220, 40):

    x = []
    y = []

    for a in range(-255, 256, 1):
           x.append(a)
           y.append(szyfrant.szyfruj(a))

    pl.plot(x, y, label=k)

pl.grid()
pl.legend(loc='best')
pl.show()
