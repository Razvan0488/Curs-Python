# '''1.
# Clasa Cerc
#
# Atribute: raza, culoare
#
# Constructor pt ambele atribute
#
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()
# '''
#
# from math import pi
#
# class Cerc:
#     def __init__(self,raza,culoare):
#         self.raza= raza
#         self.culoare=culoare
#     def descriere_cerc(self):
#         print(f'Cercul are culoarea {self.culoare} si are raza {self.raza}')
#     def aria(self):
#         return pi*self.raza**2
#     def diametru(self):
#         return 2*self.raza
#     def circumferinta(self):
#         return 2*pi*self.raza
#
#
# cerc1 = Cerc(5, 'galben')
# cerc2 = Cerc(4, 'rosu')
#
# cerc1.descriere_cerc()
# cerc2.descriere_cerc()
#
# print(cerc1.aria())
# print(cerc2.aria())
#
# print(cerc1.diametru())
# print(cerc2.diametru())
#
# print(cerc1.circumferinta())
# print(cerc2.circumferinta())
#
# '''2.
# Clasa Dreptunghi
#
# Atribute: lungime, latime, culoare
#
# Constructor pt toate atributele
#
# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().
# '''
#
# class Dreptunghi:
#     def __init__(self,lungime,latime,culoare):
#         self.lungime= lungime
#         self.latime=latime
#         self.culoare=culoare
#     def descriere(self):
#         print(f'Dreptunghiul are lungimea {self.lungime} ,latimea {self.latime} si culoarea {self.culoare}')
#     def arie(self):
#         return self.lungime*self.latime
#     def perimetru(self):
#         return 2*self.lungime+2*self.latime
#     def schimbare_culoare(self,culoare_noua):
#         self.culoare=culoare_noua
#
# d1=Dreptunghi(5,4,'albastru')
# d2=Dreptunghi(7,6,'rosu')
#
# d1.descriere()
# d2.descriere()
# print(d1.arie())
# print(d2.arie())
# print(d1.perimetru())
# print(d2.perimetru())
# d1.schimbare_culoare('verde')
# d2.schimbare_culoare('galben')
# print(d1.culoare)
# print(d2.culoare)
#
# '''3.
# Clasa Angajat
#
# Atribute: nume, prenume, salariu
#
# Constructor pt toate atributele
#
# Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)
# '''
#
# class Angajat:
#     def __init__(self, nume, prenume,salariu):
#         self.nume=nume
#         self.prenume=prenume
#         self.salariu= salariu
#     def descriere(self):
#         print(f'Angajatul are numele {self.nume} si prenumele  {self.prenume} si are salariul {self.salariu}')
#     def nume_complet(self):
#         print(f'Numele complet al angajatului este {self.nume} {self.prenume}')
#     def salariu_lunar(self):
#         print(f"Salariul lunar este {self.salariu}")
#     def salariu_anual(self):
#         print(f'Salariul anula este {self.salariu*12}')
#     def marire_salariu(self,procent):
#         self.salariu= self.salariu+ procent/100*self.salariu
# a1=Angajat('Popescu','Ionel',1000)
# a2=Angajat('Ionescu','Mihai',1200)
# a1.descriere()
# a2.descriere()
# a1.nume_complet()
# a2.nume_complet()
# a1.salariu_lunar()
# a2.salariu_lunar()
# a1.salariu_anual()
# a2.salariu_anual()
# a1.marire_salariu(20)
# a2.marire_salariu(15)
# print(a1.salariu_lunar())
# print(a2.salariu_lunar())
#
# '''
# 4.
# Clasa Cont
#
# Atribute: iban, titular_cont, sold
#
# Constructor pentru toate
#
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)
# '''
#
# class Cont:
#     def __init__(self,iban,titular_cont,sold):
#         self.iban=iban
#         self.titular_cont=titular_cont
#         self.sold=sold
#     def afisare_sold(self):
#         print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold}')
#     def debitare_cont(self,suma_debitata):
#         if suma_debitata > self.balance:
#             print()
#         else:
#             self.balance -= suma_debitata
#             print(f"{suma_debitata}RON has been debited from the account")
#
#     def creditare_cont(self, suma_depusa):
#             self.balance += suma_depusa
#             print(f"{suma_depusa}RON has been credited to the account")

# '''5.
# Clasa Factura
#
# Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
#
# Constructor: toate atributele, fara serie
#
# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti
#
# Factura seria x numar y
# Data: generati automat data de azi
# Produs | cantitate | pret bucata | Total
# Telefon |      7       |       700       | 49000
# '''
#
# from datetime import date
# class Factura:
#      def __init__(self, numar, nume_produs, cantitate, pret_buc):
#          self.numar = numar
#          self.nume_produs = nume_produs
#          self.cantitate = cantitate
#          self.pret_buc = pret_buc
#      def schimba_cantitatea(self,cantitate_noua):
#         self.cantitate = cantitate_noua
#      def schimba_pretul(self, pret_nou):
#         self.pret_buc = pret_nou
#      def schimba_nume_produs(self, produs_nou):
#          self.nume_produs = produs_nou
#      def generare_factura(self):
#          print(f"Date: {date.today()}\n| Product | Quantity | Price per unit | Total |")
#          print("-" * 47)
#          print(
#              f"| {self.nume_produs:^8}|{self.cantitate:^10}|{self.pret_buc:^16}|{self.cantitate * self.pret_buc:^7}|")
#
# b1 = Factura(1001, "Telefon", 7, 700)
# b1.generare_factura()

'''6.
Clasa Masina

Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate masinile cand ies din fabrica sunt gri
Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
Culori disponibile = alegeti voi 5-7 culori
Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
Inmatriculata = False

Constructor: model, viteza_maxima

Metode:
descrie() (se vor printa toate atributele, inafara de culori_disponibile)
inmatriculare() - va schimba atributul inmatriculata in True
vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
franeaza() - masina se va opri si va avea viteza 0
'''
class SpeedEError(Exception):
    pass
class Masina:
    def __init__(self, model, viteza_maxima):
        self.marca = 'Ford'
        self.model = model
        self.viteza_maxima = viteza_maxima
        self.viteza_actuala = 0
        self.culoare = 'gri'
        self.culori_disponibile = {"Grey", "White", "Black", "Red", "Blue", "Green", "Purple", "Orange"}
        self.inmatriculata = False
    def descriere(self):
        print(f'Ati cumparat masina marca {self.marca} ,model {self.model}.Masina poate atinge viteza de {self.viteza_maxima}.Culoare din fabrica este gri insa se poate modifica contracost.Viteza actuala a acesteia este de {self.viteza_actuala}.Iar statusul inmatricularii este  {self.inmatriculata}')
    def inmatriculare(self):
        self.inmatriculata = True
    def vopseste(self,new_color):
        if new_color in self.culori_disponibile:
            self.culoare = new_color
            print(f'Am vopsit masina dumneavoastra in culoarea {self.culoare}')
        else:
            print(f'Culoarea dumneavoastra nu este disponibila.Puteti alege una dintre culorile urmatoare: {self.culori_disponibile}')
    def accelerare(self,new_speed):
        if new_speed < 0:
            raise SpeedEError(f'Error,{new_speed}< 0')
        else:
            if new_speed > self.viteza_maxima:
                self.viteza_actuala = self.viteza_maxima
            else:
                self.viteza_actuala = new_speed
        print(f'Ati ajuns la viteza {self.viteza_actuala}')
    def franeaza(self):
        self.viteza_actuala = 0
        print(f'Ai franat.Viteza ta actuala este de {self.viteza_actuala}')

masina1= Masina('Focus', 240)
masina1.descriere()
masina1.vopseste('Orange')
masina1.accelerare(60)
masina1.inmatriculare()
masina1.franeaza()

'''# 7. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

# Metode:
# adauga_task(nume, descriere) - se va adauga in dict
# finalizeaza_task(nume) - se va sterge din dict
# afiseaza_todo_list() - doar cheile
# afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
# daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
# Daca acesta raspunde nu - la revedere
# daca raspunde da - il cerem detalii task si salvam nume+detalii in dict'''


class TodoList:
    def __init__(self):
        self.todo = {}

    def add_task(self, name, description):
        self.todo[name] = description

    def finalize_task(self, name):
        print(f"Task {self.name}: \u2713. Removing it from the list.")
        #         self.todo.pop(name)
        del self.todo[name]

    def show_todo_list(self):
        print(list(self.todo.keys()))

    def show_task_details(self, task_name):
        if task_name not in self.todo:
            to_add = input(f"Task {task_name} is not in the todo list. Do you want to add it? [y/n]: ")
            if to_add.lower().startswith('y'):
                details = input(f"Add a description for the task {task_name}: ")
                self.todo[task_name] = details
            else:
                print("Aright, bye bye!:)")
        else:
            print(f">Task: {task_name}\n>Description: {self.todo[task_name]}")


todo_list = TodoList()
todo_list.show_todo_list()
todo_list.add_task("Cooking Pasta",
                   "This is my amazing pasta recipe that goes like:\n\t 1. boil some water \n\t 2. take a hand full of spaghetti... \n\t 3. break them in half... and somewhere in the world some italian will cry in anger for doing such a sacrilege :D")
todo_list.show_todo_list()
todo_list.show_task_details("Cooking Pasta")
todo_list.show_task_details("Exercise")
todo_list.show_task_details("Exercise")