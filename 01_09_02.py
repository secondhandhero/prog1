# silnia iteracyjnie

class LiczSilnie():


    def silniowanie(self,n):
        wynik=1

        for i in range(2,n+1):
            wynik=wynik*i
        return wynik


Silnia=LiczSilnie()

x=int(input('pp'))
if type(x)==int and x >= 0:
    print(Silnia.silniowanie(x))
else:
    print('zla liczba')