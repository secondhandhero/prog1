bri = set(['brazil', 'russia', 'india'])
print('india' in bri)
bric = bri.copy()
bric.add('china')
print(bric.issuperset(bri))
bri.remove('russia')
print(bri & bric)
bric.intersection(bri)
