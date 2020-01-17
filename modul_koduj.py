# modul kodujacy


class CSzyfrant:
    def __init__(self, key):
        self.klucz = key

    def szyfruj(self, data):
        if data < 0:
            data = data + 256
        return ((data + self.klucz) % 256)


class CKooder(CSzyfrant):
    def __init__(self,key):
        CSzyfrant.__init__(self,key)
    def wykres(self):
        x = []
        y = []
        for a in range(-255, 256, 1):
            x.append(a)
            y.append(self.szyfruj(a))
        return x,y
print('nowa gałą')