'''1. Creati-va 2 fisiere separate, unul numit functions_tema08.py, in care sa adaugati implementarea, iar altul numit test_functions_tema08.py in care sa aveti clasa de test.
a) Scrieti o functie care primeste un numar natural si returneaza daca e prim sau nu
 e.g.: is_prime(13) => True
         is_prime(24) => False
b) Scrieti 2 teste unitare (unul pentru True si unul pentru False) pentru functia is_prime
c). Scrieti o functie care are 2 parametrii nr naturale a,b cu a<b. Functia returneaza lista numerelor prime din intervalul [a,b].
e.g.: list_of_primes_in_interval(3, 31) => [3,5,7,11,13,17,19,23,29,31]
d) Scrieti 2 teste unitare pentru functia list_of_primes_in_interval
'''

from abc import ABC, abstractmethod

def is_prime(nr):
  for i in range(2,nr):
    if (nr%i) == 0:
      return False
  return True

def lista_de_prime(a,b):
  lista_prime = []
  nr = a
  while nr <= b:
    if is_prime(nr) == True:
      lista_prime.append(nr)
    nr += 1
  return lista_prime

'''2. Creati-va un fisier de test in care sa adaugati o clasa si sa testati metodele (aria, getter, setterl, deletter, descrie) 
claselor Patrat si Cerc de la Tema07.
(Bonus - optional): Puteti incerca sa va instantiati un obiect pe care sa il refolositi la fiecare test cu ajutorul 
functie setUp() al clasei unittest.TestCase
'''


class FormaGeometrica(ABC):
  # pi = 3.14
  def __init__(self):
    self.pi = 3.14

  @abstractmethod
  def arie(self):
    pass

  def descriere(self):
    # print('Cel mai probabil am colturi')
    return 'Cel mai probabil am colturi'


class Patrat(FormaGeometrica):
  def __init__(self, latura):
    super().__init__()
    self.__latura = latura
    print(f'In initul clasei patrat, pi= {self.pi}')

  def arie(self):
    return self.__latura ** 2

  @property
  def latura(self):
    return self.__latura

  @latura.setter
  def set_latura(self, new_latura):
    self.__latura = new_latura

  @latura.getter
  def get_latura(self):
    return self.__latura

  @latura.deleter
  def del_latura(self):
    self.__latura = None
    print('Am sters latura')


class Cerc(FormaGeometrica):
  def __init__(self, raza):
    super().__init__()
    self.__raza = raza

  def arie(self):
    return self.pi * (self.__raza ** 2)

  @property
  def raza(self):
    return self.__raza

  @raza.setter
  def set_raza(self, new_raza):
    self.__raza = new_raza

  @raza.getter
  def get_raza(self):
    return self.__raza

  @raza.deleter
  def del_raza(self):
    self.__raza = None
    print('Am sters raza')

  def descriere(self):
    # print('Eu nu am colturi')
    return 'Eu nu am colturi'