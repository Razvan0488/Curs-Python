'''1. a) Sa se scrie un iterator (clasa) pentru literele mici din alfabet
    b) Adaugati o functie print_until_letter(the_letter) care sa afiseze doar literele pana la litera data ca argument

a)
class AlphabetIterator:
    def __init__(self):
        # implementarea voastra aici

    def __iter__(self):
        return self

    def __next__(self):
        # implementarea voastra aici


alphabet_it = AlphabetIterator()
for letter in alphabet_it:
    print(letter)
    # a
    # b
    # c
     ….
    # z

b)
print_until_letter(‘e’)
# a
# b
# c
# d
# e
'''
print('a) \n')
class AlphabetIterator:
    def __init__(self):
        self.letter = 'a'
    def __iter__(self):
        return self
    def __next__(self):
        current_letter = self.letter
        self.letter = chr(ord(self.letter)+1)
        if current_letter == chr(ord('z')+1):
            raise StopIteration
        return current_letter

alphabet_it = AlphabetIterator()
for letter in alphabet_it:
    print(letter)

print('\n b)')

def print_until_letter(the_letter):
    iterator_alfabet = AlphabetIterator()
    for litera in iterator_alfabet:
        if litera <= the_letter:
            print(litera)
print_until_letter('g')


# 2) Generator pt primele n nr prime
def is_prime(nr):
    prime=True
    for i in range(2,nr):
        if nr%i==0:
            prime=False
    return prime
def prime_gen(n):
    i = 2
    count_nr_prime = 0
    while count_nr_prime !=n:
        if is_prime(i):
            yield i
            count_nr_prime += 1
        i += 1

for nr in prime_gen(7):
    print(nr)

print('\n ')
'''3.  a) Functie pentru primele n nr din sirul lui Fibonacci
     b) Generator pentru primele n nr din sirul lui Fibonacci
Sirul lui Fibonacci: 0,1,1,2,3,5,8,13,21,34.... 
Sirul incepe cu 0 si 1, fiecare numar din sir avand proprietatea ca este suma precedentelor 2 (oricare n = n-2 + n-1, de ex 8 = 3 + 5)

a)
def fibo(n):
    # implementarea voastra aici
   

print(fibo(8)) # => [0,1,1,2,3,5,8,13]


b)
def fibo_gen(n):
    # implementarea voastra aici


for i in fibo_gen(8):
    print(i)
    # 0
    # 1
    # 1
    # 2
    # 3
    # 5
    # 8
    # 13
'''

print('a) \n')
def fibo(n):

    if n <= 0:
        raise ValueError("Alegeti un numar > 0")
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    fibo_numbers = [0, 1]
    a, b = 0, 1
    generated_numbers = 2

    while generated_numbers < n:
        fibo_numbers.append(a+b)
        a, b = b, a+b
        generated_numbers += 1
    return fibo_numbers

print(fibo(6))

print('\n b)')
def fibo_gen(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

for val in fibo_gen(6):
    print(val)
