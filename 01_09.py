# kolejna próba

class PoliczenieSilni():


    def silniowanie(self,n):

        if n in {0,1} :
            return 1
        else:
            return n*self.silniowanie(n-1)

silnia=PoliczenieSilni()

x=int(input('daj liczbe'))
print(silnia.silniowanie(x))