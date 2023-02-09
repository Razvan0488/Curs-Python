'''#1 Avand lista
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
a)a)    Folositi un for ca sa iterati prin toata lista cu ajutorul indexilor si sa afisati
‘Masina mea preferata este x’

'''
masini=['Audi','Volvo','BMW','Mercedes','Aston Martin','Lastun','Fiat','Trabant','Opel']
for element in masini:
    print(f'Masina mea preferata este {element}')

# b)    Faceti acelasi lucru cu un for each
masini=['Audi','Volvo','BMW','Mercedes','Aston Martin','Lastun','Fiat','Trabant','Opel']
for element in masini:
    print(f'Masina mea preferata este {element}')
else:
    print('Am terminat masinile preferate')

#c) Faceti acelasi lucru cu un while
masini=['Audi','Volvo','BMW','Mercedes','Aston Martin','Lastun','Fiat','Trabant','Opel']
poz=0
while poz<len(masini):
    print(f'Masina mea preferata este {masini[poz]}')
    poz=poz+1
else:
    print(f'Am terminat cu masinile preferate')

'''#2.
Aceeasi lista
Folositi un for in for
   Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul (v1 - caracter, v2 - element)
Printati varianta finala a listei
Incercati sa rezolvati atat v1 => output: ['aUDi', 'vOLVo', 'bMw', 'mERCEDEs', 'aSTON MARTIn', 'lASTUn', 'fIAt', 'tRABANt', 'oPEl']
Cat si v2 => output: ['audi', 'VOLVO', 'BMW', 'MERCEDES', 'ASTON MARTIN', 'LASTUN', 'FIAT', 'TRABANT', 'opel']
'''
masini=['Audi','Volvo','BMW','Mercedes','Aston Martin','Lastun','Fiat','Trabant','Opel']
for idx_masina in range(len(masini)):
    masina_modif = ''
    for idx_caracter in range(len(masini[idx_masina])):
        if idx_caracter == 0 or idx_caracter == len(masini[idx_masina])-1:
            masina_modif += masini[idx_masina][idx_caracter].lower()
        else:
            masina_modif += masini[idx_masina][idx_caracter].upper()
    masini[idx_masina] = masina_modif
print(masini)


'''3. Aceeasi lista,
Vine un cumparator care doreste sa cumpere un Mercedes
Iterati prin ea cu for
Daca masina e mercedes (if)
   Printam ‘am gasit masina dorita de dvs’
   Iesim din ciclu folosind un cuvant cheie care face acest lucru
Altfel:
   Printam Am gasit masina X. Mai cautam
'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Mercedes':
        print("Am gasit masina dorita de dvs!")
        break
    else:
        print(f"Am gasit masina {masina}. Mai cautam...")

'''# 4. Aceasi lista.
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# Printati S-ar putea sa va placa masina x'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina in ('Trabant', 'Lastun'):
        continue
    print(f"S-ar putea sa va placa masina {masina}")

'''# 5. Modernizati parcul de masini. Creati o lista goala, masini_vechi. Iterati prin masini.
# Cand gasiti Lastun sau Trabant:
#     Salvati aceste masini in masini_vechi
#     Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for i in range(len(masini)):
    if masini[i] in ('Trabant','Lastun'):
        masini_vechi.append(masini[i])
        masini[i]='Tesla'
print(f'Masini noi: {masini}')
print(f'Masini vechi: {masini_vechi}')

'''# 6. Avand dict:
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina x
# Iterati prin lista'''

pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
for masina,pret in pret_masini.items():
    if pret < 15000:
        print(f'Puteti alege masina {masina}')


# 7. Avand lista
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

count_3=0
for i in numere:
    if i==3:
        count_3 +=1
print(count_3)

# 8. Aceeasi lista. Iterati prin ea.
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum)
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma=0
for i in numere:
    suma +=i
print(suma)

# 9. Aceeasi lista. Iterati prin ea.
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
max =-32000
for nr in numere:
     if nr> max:
         max= nr
print(max)

# 10. Aceeasi lista. Iterati prin ea.
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

for i in range(len(numere)):
    if numere[i] >0:
        numere[i]=numere[i]*(-1)
print(numere)

# 11. alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Iterati prin lista alte_numere
# Populati corect celelalte liste
# Afisati cele 4 liste la final
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for n in alte_numere:
    if n % 2 == 0:
        numere_pare.append(n)
    else:
        numere_impare.append(n)
    if n > 0:
        numere_pozitive.append(n)
    else:
        numere_negative.append(n)
print(f"Numere pare:     {numere_pare}")
print(f"Numere impare:   {numere_impare}")
print(f"Numere pozitive: {numere_pozitive}")
print(f"Numere negative: {numere_negative}")

'''# 12. Aceeasi lista. Ordonati crescator lista fara sa folositi sort
# Va puteti inspira vizual de aici
# https://www.youtube.com/watch?v=lyZQPjUT5B4'''
lst = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(0, len(lst)-1):
    for j in range(i+1, len(lst)):
        if lst[j] < lst[i]:
            aux=lst[i]
            lst[i]=lst[j]
            lst[j]=aux
print(lst)

# 13. Ghicitoare de numar.
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#    User alege un numar
#    Programul ii spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitari! Ai ghicit!

import random
secret_nr = random.randint(1,30)
guessed_nr = None

while guessed_nr != secret_nr:
    guessed_nr = int(input("Ghiceste un nr intre 1 si 30: "))
    if guessed_nr == secret_nr:
        print("Felicitari! Ai ghicit!")
    elif guessed_nr < secret_nr:
        print("Nr secret e mai mare!")
    else:
        print("Nr secret e mai mic!")


'''# 14. Alegeti un numar de la tastatura
# Ex:7
# Scrieti un program care sa genereze in consola urmatoarea piramida
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777'''

x=int(input('Introduceti nr:'))
for i in range(1,x+1):
    print(i*str(i))

'''# 15. tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# Iterati prin lista 2d
# Printati ‘Cifra curenta este x’
# (hint: nested for - adica for in for)'''

tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
for lst in tastatura_telefon:
    for nr in lst:
        print(f'Cifra curenta este {nr}')
