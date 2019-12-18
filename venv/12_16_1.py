def szyfruj(liczba, klucz):
    return (liczba + klucz) % 256

def odszyfruj(liczba, klucz):
    return (256 + liczba - klucz) % 256

wiadomosc = int(input('Podaj dodatnią liczbę do zaszyfrowania: '))
szyfr=szyfruj(wiadomosc, 89)
print('Wynik=%s' % szyfr)
print('Odszyfrowany: %s' % odszyfruj(szyfr, 89))