#1. Functie care sa calculeze si sa returneze suma a 2 numere
def sum(nr1,nr2):
    return nr1+nr2
print(sum(2,4))

#2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
def adevar(nr):
    if nr%2==0:
        return True
    else:
        return False
print(adevar(4))

#3. Functie care returneaza numarul total de caractere din numele tau complet.(nume, prenume, nume_mijlociu)
def count_char(nume,prenume,domiciliu):
    return len(nume)+len(prenume)+len(domiciliu)
print(count_char('cuciureanu','razvan','iasi'))

#4. Functie care returneaza aria dreptunghiului
def arie_dreptunghi(lungime,latime):
    return lungime*latime
print(arie_dreptunghi(2,8))

#5. Functie care returneaza aria cercului
def arie_cerc(raza):
    return 3.14*(raza**2)
print(arie_cerc(3))


# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu
def verif_caracter(caracter, string):
    if caracter in string:
        return True
    else:
        return False


print(verif_caracter('d', 'Ala bala'))


#7. Functie fara return, primeste un string si printeaza pe ecran:
#-Nr de caractere lower case este x
#-Nr de caractere upper case exte y
def count_caractere(string):
    count_lower=0
    count_upper=0
    for caracter in string:
        if caracter.islower():
            count_lower =count_lower+1
        else:
            if caracter.isupper():
                count_upper =count_upper+1
    print({count_lower})
    print({count_upper})
count_caractere('Ala bala')


#8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
def lista_numere(lista):
    lista1=[]
    for elem in lista:
        if elem>0:
            lista1.append(elem)
    return lista1
print(lista_numere([1,-2,3,4]))

####9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
#Primul numar x este mai mare decat al doilea nr y
#Al doilea nr y este mai mare decat primul nr x
#Numerele sunt egale.
def numere(x,y):
    if x>y:
        print(f'Primul numar {x} este mai mare decat al doilea numar {y}')
    else:
        if x<y:
            print(f'Al doilea numar {y} este mai mare decat primul numar {x}')
        else:
            print('NUmerele sunt egale')
numere(4,3)

####10. Functie care primeste un numar si un set de numere.
#Printeaza ‘am adaugat numarul nou in set’ + returneaza True
#Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
def numere_set (nr,setul):
    if nr in setul:
        print(f'Nu am adaugat numarul in set.Acesta exista deja')
        return False
    else:
        setul.add(nr)
        print('Am adaugat numarul in set')
        return True
print(numere_set(7,{1,2,3,4,5}))

# 11. Functie care primeste o luna din an si returneaza cate zile are acea luna

from calendar import monthrange

def zilele_lunii(luna):
    return monthrange(2022,luna)[1]
print(zilele_lunii(3))

'''# 12. Functie calculator care sa returneze 4 valori 
# Suma, diferenta, inmultirea, impartirea a 2 numere

# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)'''

def calculator(x,y):
    return x+y, x-y, x*y, x/y
a,b,c,d = calculator(10,2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

'''# 13. Functie care primeste o lista de cifre (adica doar 0-9)
# Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returneaza un DICT care ne spune de cate ori apare fiecare cifra
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }'''

def counter_cifre(lista):
    dict_nr_cifre = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for nr in lista:
        dict_nr_cifre[nr] += 1
    return dict_nr_cifre
print(counter_cifre([1, 3, 1, 5, 9, 7, 7, 5, 5]))

'''# 14. Functie care primeste 3 numere
# Returneaza valoarea maxima dintre ele'''

def numere(x,y,z):
    return max(x,y,z)
print(numere(1,2,3))

'''# 15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
# Ex: daca dam nr 3
# Suma va fi 6 (0+1+2+3)'''
def suma(x):
    suma=0
    while x!=0:
       suma += x
       x=x-1
    return suma
print(suma(5))

'''# 16. Functie care nu primeste argumente, dar cere un input de la tastatura si va printa
# “Numarul ales este pozitiv” sau “Numarul ales este negativ” sau “Numarul ales este 0”, 
dupa caz, iar daca nu introducem un numar, sa se afiseze “Nu ati ales un numar valid”; 
la final sa se afiseze “Sfarsitul functiei” indiferent de caz.'''
def numar():
     nr = input("Introduceti nr:")
     try:
         nr = float(nr)
     except:
        print('Nu ati ales un numar valid')
     else:
         if nr > 0:
             print("Numarul ales este pozitiv")
         elif nr < 0:
             print("Numarul ales este negativ")
         else:
             print("Numarul ales este 0")
     finally:
         print("Sfarsitul functiei")
numar()

'''# 17. Functie care primesete 2 liste de numere (numerele pot fi dublate)
# Returnati numerele comune 

# Ex:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Raspuns: {2, 3}'''

def numere_comune(lst1,lst2):
    return set(lst1) & set(lst2)
print(numere_comune([1,2,3],[3,4,5]))

'''# 18. Functie care sa aplice o reducere de pret. 
Daca apelul functiei nu primeste valoarea reducerii, sa ia valoarea default 10%.
# Daca produsul costa 100 lei si aplicam reducere de 10%
# Pretul va fi 90
# Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida
def discount(price, discount_percent=10):'''

def reducere_pret(pret, reducere=10):
    if reducere in range(0,100):
        pret= pret - pret*reducere/100
        return pret
    else:
        print('Reducerea nu a putut fi aplicata')
print(reducere_pret(100,50))
print(100)

'''# 19. Functie care sa afiseze data si ora curenta din ro
# (bonus: afisati si data si ora curenta din China)'''
from datetime import datetime, timedelta, timezone


# v1
def display_date_time_v1():
    now = datetime.now()
    print(f"Date and time Romania: {now}")
    print(f"Date and time China: {now + timedelta(hours=5)}")


display_date_time_v1()

'''# 20. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun 
daca nu vrei sa ne zici cand e ziua ta :)'''
from datetime import datetime


def days_til_birthday(birthday_date="25.12.2022"):
    birthday_date = datetime.strptime(s, "%d.%m.%Y")
    today = datetime.today()

    days_left = (birthday_date - today).days
    print(days_left)


days_til_birthday()



