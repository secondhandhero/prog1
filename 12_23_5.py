# program testowy 1

import matplotlib.pyplot as pl

from modul_koduj import CKooder

for k in range(100, 220, 40):
    kkkod = CKooder(k)
    x,y=kkkod.wykres()
    pl.plot(x,y, label=k)

pl.grid()
pl.legend(loc='best')
pl.show()
