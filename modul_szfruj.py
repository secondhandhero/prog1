#modul szyfrujacy


class CSzyfrant:

    def __init__(self, key):
        self.klucz = key

    def szyfruj(self, data):
        if data < 0:
            data = data + 256
        return ((data + self.klucz) % 256)

class kooder(CSzyfrant):
    def __init__(self,key):
        self.klucz=key

    def wykres(self):
    szyfrant=CSszyfrant(self.klucz)
        for a in range(-255, 256, 1):
        x.append(a)
        y.append(szyfrant.szyfruj(a))
    return (x,y)