# Lista zakupów
shoplist = ['jabłka', 'mango', 'marchewka', 'banany']
print(u'Mam %s rzeczy do kupienia. \nSą to:' % len(shoplist))
for item in shoplist:
 print(item)
# w Pythinie 3.x: print(item, end=' ')
print(u'\nDla sąsiadki kupuję jeszcze ryż.')
shoplist.append('rice')
print(u'pełna lista zakupów to obecnie %s' % shoplist)
print('Posortowana lista:')
shoplist.sort()
print(shoplist)
print(u'Skreślam pierwszy element, bo mam mało pieniędzy: %s' % shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print(u'Zapamiętam, że nie kupiłem: %s' % olditem)
print(u'Ostateczna lista zakupów: %s' % shoplist)
