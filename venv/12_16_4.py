class TSzyfrant:

    def __init__(self,klucz):
        self.klucz=klucz

    def szyfruj(self, liczba):
        return (liczba + self.klucz) % 256

    def odszyfruj(self, liczba):
        return (256 + liczba - self.klucz) % 256


szyfrant=TSzyfrant(89)
wiadomosc = int(input('Podaj dodatnią liczbę do zaszyfrowania: '))
szyfr=szyfrant.szyfruj(wiadomosc)
print('Wynik=%s' % szyfr)
print('Odszyfrowany: %s' % szyfrant.odszyfruj(szyfr))