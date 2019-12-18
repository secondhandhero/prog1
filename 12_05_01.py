# 'ab' to krótka lista adresowa
pass
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Spammer': 'spammer@hotmail.com'}
print("Adres Swaroop'a to", ab['Swaroop'])
# Usuwanie pary z listy
del ab['Spammer']
print('Ilość kontaktów w liście: {}\n'.format(len(ab)))
for name, address in ab.items():
    print('Adres: %s to %s' %(name,address))
# lub:
    print('Adres: {} to {}'.format(name,address))
# dodanie pary
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nAdres Guido'to", ab['Guido'])
pass
