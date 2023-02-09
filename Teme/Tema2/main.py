# #2.Verificati si afisati daca x este numar natural sau nu
#
# x=5
# if x>=0 :
#     print('x este un numar natural')
# else:
#     print('x nu este numar natural')
#

# '''#3.Verificati si afisati daca x este numar pozitiv, negativ sau neutru'''
# x=input("Introduceti x:")
# x=float(x)
# if x>0:
#     print("x este numar pozitiv")
# elif x==0:
#     print("x este numar neutru")
# else:
#     print("x este numar negativ")

# '''#4. Verificati si afisati daca x este intre -2 si 13'''
# x=input('Introduceti x:')
# x=float(x)
# if x>-2 and x<13:
#     print("x se afla intre intervalul -2 si 13")
# else:
#     print("x nu se afla intre intervalul -2 si 13")

# '''#5. Verificati si afisati daca diferenta dintre x si y este mai mica de 5'''
# x=int(input("introdu x:"))
# y=int(input("introdu y:"))
# if abs(x-y)<5:
#     print("DIferenta este mai mica decat 5")
# else:
#     print("diferenta NU este mai mica decat 5")
#

# '''#6. Verificati daca x NU este intre 5 si 27. (a se folosi ‘not’)'''
# x=int(input('Introduceti pe x:'))
# print(not (x >= 5 and x <= 27))

# '''#7 x si y (int) Verificati si afisati daca sunt egale, daca nu afisati care din ele este mai mare'''
# x=int(input('Introduceti x:'))
# y=int(input('Introduceti y:'))
# if x==y:
#     print('x este egal cu y')
# elif x>y:
#     print("x este mai mare decat y")
# else:
#     print("y este mai mare decat x")

# '''# 8. x, y, z - laturile unui triunghi. Afisati daca triunghiul este isoscel, echilateral sau oarecare.'''
# x=int(input("x="))
# y=int(input("y="))
# z=int(input("z="))
#
# if x==y and x==z :
#     print("triunghiul este echilateral")
# elif x==y or y==z or x==z:
#     print("triunghiul este isoscel")
# else:
#     print("triunghiul este oarecare")

# '''#9. Cititi o literax de la tastatura.Verificati si afisati daca este vocala sau nu'''
# x=input("introduceti litera:")
# if x in "aeiouAEIOU":
#     print(f'{x} este vocala')
# else:
#     print(f'{x} nu este vocala')
#
# '''# 10. Transformati si printati notele din sistem romanesc in  >
# # Peste 9 => A
# # Peste 8 => B
# # Peste 7 => C
# # Peste 6 => D
# # Peste 4 => E
# # 4 sau sub => F'''
# nota =float(input("Introduceti nota:"))
# if nota>10 or nota<1:
#     print("Introduceti o nota intr 1 si 10")
# elif nota > 9:
#     print("A")
# elif nota > 8:
#     print("B")
# elif nota > 7:
#     print("C")
# elif nota > 6:
#     print("D")
# elif nota > 4:
#     print("E")
# else:
#     print("F")

# '''# 11. Verificati daca x are minim 4 cifre (x e int) (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)'''
# x=int(input('introduceti un numar:'))
# count_nr=0
# while x!=0:
#     count_nr=count_nr+1
#     x=int(x/10)
# if count_nr>=4:
#     print('numarul are minim 4 cifre')
# else:
#     print('numarul nu are minim 4 cifre')

# '''# 12. Verificati daca x are exact 6 cifre.'''
# x=int(input('introduceti un numar:'))
# count_cifre=0
# while x!=0:
#     count_cifre=count_cifre+1
#     x=int(x/10)
# if count_cifre==6:
#     print('numarul are exact 6 cifre')
# else:
#     print('numarul NU are exact 6 cifre')
#

# '''# 13. Verificati daca x este numar par sau impar (x e int)'''
# x=int(input('x='))
# if x%2==0:
#     print('x este par')
# else:
#     print('x  este impar')

# '''# 14. x, y, z (int). Afisati care este cel mai mare dintre ele?'''
# x = int(input("x = "))
# y = int(input("y = "))
# z = int(input("z = "))
# print(max(x,y,z))

# '''# 15. x, y, z - reprezinta unghiurile unui triunghi. Verificati si afisati daca triunghiul este valid sau nu.'''
# x=float(input('x='))
# y=float(input('y='))
# z=float(input('z='))
# if x+y+z==180:
#     print('triunghiul este valid')
# else:
#     print('triunghiul nu este valid')

# '''# 16. Avand stringul: 'Coral is either the stupidest animal or the smartest rock' cititi de la tastatura un int x.
# # Sa se afiseze stringul fara ultimele x caractere (ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte')'''
#
# my_string='Coral is either the stupidest animal or the smartest rock'
# x=int(input('x='))
# print(my_string[:-x])

# '''# 17.Acelasi string; declarati un string nou care sa fie format din primele 5 caractere + ultimele 5'''
# my_string='Coral is either the stupidest animal or the smartest rock'
# new_string=my_string[:5]+my_string[-5:]
# print(new_string)

# '''# 18. Acelasi string.
# # Salvati intr-o variabila si afiseaza indexul de start al cuvantului rock.
# # (hint: este o functie care va ajuta sa faceti asta).
# # Folosind aceasta variabila + slicing, afisati tot stringul pana la acest cuvant
# # output: 'Coral is either the stupidest animal or the smartest ' '''
#
# the_string = 'Coral is either the stupidest animal or the smartest rock'
# word_to_find = 'rock'
#
# index_of_word = the_string.find(word_to_find)
# print(index_of_word)
# print(the_string[:index_of_word])

# '''# 19. Cititi de la tastatura un string. Verificati daca primul si ultimul caracter sunt la fel.
# # Se va folosi un assert. Atentie: se doreste ca programul sa fie case insensitive: 'apA' e acceptat.'''
#
# my_string=input('Introduceti string:')
# assert my_string[0].lower() == my_string[-1].lower()

# '''# 20. Avand stringul '0123456789'. Afisati doar numerele pare.
# # Apoi afisati doar numerele impare (hint: folositi slicing, controlati din pas)'''
# my_string = '0123456789'
# print(f"Numere pare:  {my_string[::2]}")
# print(f"Numere imare: {my_string[1::2]}")

'''# 21. Verificare imbarcare persoane
# Tineti urmatoarele date
# Varsta
# Insotit de mama
# Insotit de tata
# Pasaport
# Act permisiune mama
# Act permisiune tata

# Conditii de imbarcare
# Daca pers are varsta peste 18 ani si are pasaport
# Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
# Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la celalat parinte

# Aici vreau sa testati codul cu toate variantele posibile
# Sa generati cazuri de test si expected result, apoi sa rulati codul si sa completati actual results
# Ex:
# Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
# Etc...'''
varsta = int(input("Introduceti varsta (introduceti un varsta valida): "))
pasaport = bool(int(input("Persoana are pasaport? (introduceti 1 pt da, 0 pt nu)")))
insotit_de_mama = bool(int(input("Persoana e insotita de mama? (introduceti 1 pt da, 0 pt nu): ")))
insotit_de_tata = bool(int(input("Persoana e insotita de tata? (introduceti 1 pt da, 0 pt nu): ")))
permisiune_mama = bool(int(input("Persoana are act de permisiune de la mama? (introduceti 1 pt da, 0 pt nu): ")))
permisiune_tata = bool(int(input("Persoana are act de permisiune de la tata? (introduceti 1 pt da, 0 pt nu): ")))

if (varsta>=18 and pasaport) or (varsta<18 and pasaport and insotit_de_tata and insotit_de_mama) or (varsta<18 and insotit_de_mama and permisiune_tata) or (varsta<18 and pasaport and insotit_de_tata and permisiune_mama):
    print('Persoana imbarcata')
else:
    print('Persoana nu este imbarcata')

