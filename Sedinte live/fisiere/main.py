import json
with open("numbers.json","r") as f:
    from_file=json.load(f)
lst1=from_file['integer_numbers']
lst2=from_file['float_numbers']
sum1=0
for x in lst1:
    sum1=sum1+x
media1=sum1/len(lst1)
print(media1)
sum2=0
for x in lst2:
    sum2=sum2+x
media2=sum2/len(lst2)
print(media2)
media_totala=(sum1+sum2)/(len(lst1)+len(lst2))
print(media_totala)
media_totala=(media1+media2)/2#nu e ok
print(media_totala)#nu e ok
#v2
print(sum(lst1)/len(lst1))
print(sum(lst2)/len(lst2))
#v3
import statistics
print(statistics.mean(lst1+lst2))