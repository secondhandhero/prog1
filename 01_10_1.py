
class Osoba:
    def __init__(self,imie):
        self.imie=imie
    def przywitajSie(self):
        print(self.imie,' Witaj, jak się masz?')
o=Osoba('misiek')
o.przywitajSie()