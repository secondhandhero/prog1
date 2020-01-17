
class CSilnia:

    def silnia(self,n):
        if n in [0,1]:
            return 1
        else:
            return n*self.silnia(n-1)

psilnia=CSilnia()
n=int(input('daj l. calkowitą nieujemną'))
print('silnia : ',psilnia.silnia(n) )