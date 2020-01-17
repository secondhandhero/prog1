# silnia rekursywnie

class CSilnia:

    def silnia(self, n):

         if n ==0 or n==1:
              return 1
         else:
              return (n * self.silnia(n-1))


PoliczSilnieZ=CSilnia()
n=int(input('daj liczbe całkowitą nieujemną:  '))

if (type(n)==int and n >= 0):
    print (' silnia z ',n,' \n wynosi = ' , PoliczSilnieZ.silnia(n))
else:
   print('to była zła liczba')