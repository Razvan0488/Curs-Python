'''#1 Declara o lista note_muzicale in care sa pui do re mi etc pana la do
a)Afiseaz-o
b)Inverseaza ordinea folosind slicing si suprascrie aceasta lista
c)Printeaza varianta actuala (inversata)
d)Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
e)Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala

Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi intr-o lista noua. Metoda gasita de tine, face suprascrierea automat si permanentizeaza aceste modificari. Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.
'''
note_muzicale = ['do','re','mi','fa','sol','la','si','do']
print(note_muzicale)
note_muzicale=note_muzicale[::-1]
print(note_muzicale)

'''#2.
De cate ori apare ‘do’?
'''
print(note_muzicale.count('do'))
'''#3.
Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
Gasiti 2 variante sa le uniti intr-o singura lista.
'''
l1=[3, 1, 0, 2]
l2=[6,5,4]
l3=l1+l2
print(l3)

'''4.
Sortati si afisati lista generata la ex anterior
Stergeti numarul 0 folosind o functie
Afisati iar lista
'''
l3.sort()
print(l3)
l3.pop(0)
print(l3)
'''#6Folosind un if verificati lista generata la ex3 si afisati
Lista este goala
Lista nu este goala
'''
if l3:
    print('lista nu e goala')
else:
    print('lista este goala')

'''#6.
Folositi o functie care sa goleasca lista de la ex3
'''
l3.clear()
print(l3)

'''#7.
Copy paste la ex 5. Verificati inca o data.
Acum ar trebui sa se afiseze ca lista e goala
'''
if l3:
    print('lista nu e goala')
else:
    print('lista este goala')

'''8.
Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folositi o functie ca sa afisati Elevii (cheile)
'''
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}


'''#9.
Printati cei 3 elevi si notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o veti lua folosindu-va de cheie
'''


'''#10.
Dorel a facut contestatie si a primit 6
Modificati nota lui Dorel in 6
Printati nota dupa modificare
'''
dict1['Dorel'] = 6
print(dict1['Dorel'])

'''11.
Gigel se transfera din clasa
Cautati o functie care sa il stearga
Vine un coleg nou. Adaugati Ionica, cu nota 9
Printati noii elevi
'''
del dict1['Gigel']
dict1['Ionica']=9
print(dict1)

'''12.
Set
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
Adaugati in zilele_sapt ‘luni’
Afisati zile_sapt. Ce observati?
'''
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}


'''# 13.Folositi un if si verificati daca:
# - Weekend este un subset al zilelor din sapt
# - Weekend nu este un subset al zilelor din sapt'''
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
if weekend.issubset(zile_sapt):
    print(f"Weekend e subset al zile_sapt")
else:
    print(f"Weekend nu e subset al zile_sapt")

'''# 14. Afisati diferentele dintre aceste 2 seturi'''
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
print(zile_sapt.difference(weekend))

'''# 15. Afisati intersectia elementelor din aceste 2 seturi'''
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
print(zile_sapt.intersection(weekend))

'''# 16. Ne imaginam o echipa de fotbal pt teren sintetic. 3 Schimbari maxime admise.
# Declara o Lista cu 5 jucatori
# Schimbari_efectuate = va jucati voi cu valori diferite
# Schimbari_max = 3

# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# Efectuam schimbarea
# Stergem jucatorul scos din lista
# Adaugam jucatorul intrat
# Afisam a intra x, a iesit y, mai aveti z schimbari
# Daca jucatorul nu e in teren:
# Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# Afisati ‘mai aveti z schimbari’

# Testati codul cu diferite valori

# Google search hint
# “how to check if item is in list python”'''

playing = ["Leo", "Cristiano", "Erling", "Kylian", "Gianluigi"]
substitutes = ["Sergi", "Ferran", "Memphis", "Ansu", "Frenkie"]
substitutes_max = 3

substitutes_done = int(input("Introduceti cate schimbari au fost efectuate pana acum dintr-un maxim de 3: "))
player_to_change = input(f"Introduceti numele unui jucator pe care sa il schimbati dintre {playing}:")
if player_to_change in playing:
    if substitutes_done < substitutes_max:
        player_in = substitutes.pop()
        playing.remove(player_to_change)
        playing.append(player_in)
        print(f"A intrat {player_in}, a iesit {player_to_change}, mai aveti {substitutes_max - substitutes_done} schimbari")
    print(f"Mai aveti {substitutes_max - substitutes_done} schimbari ")
else:
    print(f"Nu se poate efectua schimbarea, deoarece jucatorul {player_to_change} nu e in teren!")