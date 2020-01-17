# program testowy 1

import matplotlib.pyplot as pl

from modul_szfruj import kooder

for k in range(100, 220, 40):
    kkkod = kooder(k)
    x,y=kkkod.wykres()
    pl.plot(x,y, label=k)

pl.grid()
pl.legend(loc='best')
pl.show()
