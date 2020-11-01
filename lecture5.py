                                                        # set
# a = set()
# print(type(a))

# a = set('string')               set ne upooryadochenyi tip dannyh
# print(a)

# a = set([1,2,1,2,3])            udalyaet dublikaty
# print(a)

# a = set([1,2,3,1,2, 'a', 'a', 'b'])         hranyatsy neizmenyemye tipy dannyh
# print(a)

# a = {'a', 'b', 'c'}

# a.add('d')
# a.update({'f', 'l'}, {'m', 'n'})
# a.remove('a')          vydaet oshibky 
# a.discard('c')         ne vydaet oshibky
# b = a.pop()
# print(a)
# print(b)

# a = {'a', 'b', 'c', 'd'}
# lenght = len(a)
# print(lenght)
# print('g'not in a)
# print('a' in a)

# if 'd' in a:
#     a.remove('d')
# print(a)

# dancing = {'Masha', 'Sasha', 'Nikita', 'Syimyk', 'Aiperi'}
# singing = {'Syimyk', 'Masha', 'Adilet'}
# drawing = {'Mirbek', 'Dastan', 'Nikita'}
# x = dancing - singing - drawing
# x =  dancing.difference(singing, drawing)
# x = drawing.intersection(dancing, singing)
# x = dancing & singing & drawing
# print(x)
# dancing.issuperset(dancing)
# print(dancing.issuperset(singing))
# print(dancing.issubset(singing))

# x = dancing.intersection(singing)              peresechenie
# # print(x)

# x = singing.difference(dancing)     
# x = singing.symmetric_difference(dancing)      ne peresekaetsya     
# x = dancing ^ singing ^ drawing
# print(x)
# x = dancing.union(singing)                     ob'edenyaet
# x = dancing | singing | drawing
# print(x)

# print(dir(dancing))

# '-' - raznosst'
# '^' - simmitrichnaya raznosst'
# '&' - peresechenie
# '|' - obyedinenie

                            #    set izmenyaemyi       frozenset neizmenyaemyi

                                #  frozenset
krujok1 = {'Masha', 'Sasha', 'Nikita', 'Syimyk', 'Aiperi'}
krujok2 = {'Syimyk', 'Masha', 'Adilet'}
krujok3 = {'Mirbek', 'Dastan', 'Nikita'}
# frozen_krujok1 = frozenset(krujok1)
# print(type(frozen_krujok1))
x = frozenset(krujok1)
print(type(x))








