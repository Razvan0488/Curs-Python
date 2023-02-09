def sublist_containing_o(lst):
    new_list=[]
    for x in lst:
        if 'o' in x:
            new_list.append(x)
    return new_list