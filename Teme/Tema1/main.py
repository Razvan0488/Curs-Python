#un string este o lista de caractere de tipul char.
# declar si initializez o variabila de tipul string
masina= 'Volvo'
# declar si initializez o variabila de tipul integer
an_fabricatie = 2001
# declar si initializez o variabila de tipul float
pret = 3514.99
# declar si initializez o variabila de tipul boolean
inmatriculata = True
print(masina)
#Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
#Verificati tipul acesteia
pret=round(pret)
print(pret)
'''folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
(rezolvati nepotrivirile de tip prin ce modalitate doriti)'''
print(f'Am inchiriat masina marca {masina}')
print(f'Valoarea masinii este de {pret}')
print(f'Raspunsul la intrebarea,daca aceasta este inmatriculata este {inmatriculata}')
print(f'Anul fabricatiei este {an_fabricatie}')
'''6.
citeste de la tastatura numele
citeste de la tastatura prenumele
afiseaza 'Numele complet are x caractere'
'''
nume=input("Introduceti numele dumneavoastra:")
prenume=input("Introduceti prenumele dumneavoastra:")
print(f'Numele complet are {len(nume)+len(prenume)} caractere')

'''7.
citeste de la tastatura lungimea
citeste de la tastatura latimea
afiseaza 'Aria dreptunghiului este x'
'''
lungimea=input('Introduceti lungimea:')
latimea=input('Introduceti latimea')
lungimea=int(lungimea)
latimea=int(latimea)
print(f'Aria dreptunghiului este {lungimea*latimea}')

'''8.
Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
afisati de cate ori apare cuvantul 'the'
'''
my_string="Coral is either the stupidest animal or the smartest rock"
print(my_string.count("the"))

'''9.
acelasi string
inlocuieste the cu THE peste tot
printeaza rezultatul
'''
my_string="Coral is either the stupidest animal or the smartest rock"
my_string=my_string.replace('the' , 'THE')
print(my_string)

'''10.
citeste de la tastatura un string de dimensiune impara
afiseaza caracterul din mijloc
'''
the_string=input("Introduceti un text de dimensiune impara:")
print(the_string[len(the_string)//2])

'''11.
folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
si salveaza fiecare cuvant intr-o variabila
acum printeaza ambele variabile pentru verificare
'''
the_string=input('Introduceti un string format din doua cuvinte:')
s1,s2=the_string.split(' ')
print(s1,s2)

'''# 12. citeste un string de la tastatura (eg: alabala portocala)
salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite)
 capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
 => alAbAlA portocAla'''
the_string = input("Introduceti un string: ")

primul_caracter = the_string[0]
the_string = the_string[0] + the_string[1:-1].replace(primul_caracter,primul_caracter.upper()) + the_string[-1]
print(the_string)

'''# 13. citeste un user de la tastatura
citeste o parola
 afiseaza: 'Parola pt user x este ***** si are x caractere'
 ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
 eg: parola abc => ***
parola abcd => ****'''

user=input('Introduceti userul:')
parola=input('Introduceti parola:')
print(f'Parola pt userul {user} este {len(parola)*"*"} si are {len(parola)} caractere')

''' 14. TODO_1 de la curs (C01EX01)
 Cum facem sa afisam valoare lui pi cu doar 2 zecimale? presupunem pi = 3.146712'''
pi=3.14159
print(round(pi,2))

'''15. TODO_2 de la curs (C01EX02)
# Avand my_string = "Hello Pythonistas" , vrem sa afisam stringul: "eoyoss"'''

my_string = "Hello Pythonistas"
print(my_string[1::3])



