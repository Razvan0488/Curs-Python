'''# C08_EX01: a) Scrieti o functie care primeste o lista de stringuri si returneaza lista formata din acele stringuri care contin 'o'
def sublist_containing_o(lst):
    return ....


print(sublist_containing_o(["Python", "este", "limbajul", "nostru", "preferat"]))  # ["Python", "nostru"]'''

lst=["Python", "este", "limbajul", "nostru", "preferat"]
def sublist_containing_o(lst):
    new_list=[]
    for x in lst:
        if 'o' in x:
            new_list.append(x)
    return new_list
print(sublist_containing_o(lst))