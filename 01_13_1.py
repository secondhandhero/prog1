import copy

'''
print(type([1,2,3,3]))
print(type((1,2,3,3)))
print(type({1,2,3,3}))
print(type({1:1,2:1,3:1,3:4}))

print([1,2,3,3])
print((1,2,3,3))
print({1,2,3,3})
print({1:1,2:1,3:1,3:4,3:9})
'''
a=[1,1,1]
b=[2,2,2]
shoplist=[a,b]

mylist1 = shoplist    # zrobienie referencji
mylist2 = shoplist[:]  # zrobienie kopii 'płytkiej' - kopiuje listę referencji do utworzonych obiektów
mylist3 = list(shoplist) # zrobienie kopii ‘płytkiej’
mylist4=shoplist.copy() #zrobienie kopii

import copy
mylist5=copy.copy(shoplist) #zrobienie kopii
mylist6=copy.deepcopy(shoplist) #zrobienie kopii głebokiej

shoplist.append([3,3,3])
b[0]=0


print(shoplist,mylist1,mylist2,mylist3,mylist4,mylist5,mylist6,sep="\n")
print(id(shoplist[1]),id(mylist1[1]),id(mylist2[1]),id(mylist3[1]),id(mylist4[1]),id(mylist5[1]),id(mylist6[1]),sep="\n")

def funkcja():
    pass
print(funkcja())