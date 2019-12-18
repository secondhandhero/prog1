points = 7 # pierwsza liczba jest ukryta
counter = points # suma punktow
print('Możesz zakończyć sumowanie wpisując 0')
while counter < 21 and points != 0:
    points = int(input('Wpisz liczbę od 0 do 12: '))
    if points<0 or points>12:
        print('Od 0 do 12!')
        continue
    counter+= points # dodanie liczby
print('Suma=%s' % counter)