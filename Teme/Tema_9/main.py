'''1.Given the multi-line string student_grades:
 a). Using the below data, create your student_grades.csv from student_grades string.
 b). List the contents of the file as a list of dicts, a row being a dict of form:
 {"student_name": <name_of_student>, "subject": <name_of_subject>, "grade": <grade>}
 c). List the student that has the most grades and how many it has   # => Celine, 3  poate fi si un dict {"student": "Celine", "no_of_grades": 3} sau {"Celine": 3} sau ("Celine", 3), "Student with most grades ... "

student_grades =”””
Eveline,math,9
Andrew,physics,6
Celine,music,10
Matthew,math,7
Celine,english,10
Matthew,english,10
Celine,chemistry,6
“””
'''

import csv
import collections
import json

student_grades = """Eveline,math,9
Andrew,pysics,6
Celine,music,10
Matthew,math,7
Celine,english,10
Maatthew,english,10
Celine,chemistry,6"""

lista_stud = student_grades.split("\n")
print(lista_stud)
lista2 = []
for row in lista_stud:
    lista2.append(row.split(","))
print(lista2)
with open("student_grades.csv", "w",newline='') as f:
    writer = csv.writer(f)
    for row in lista2:
        writer.writerow(row)
list_of_dict = []
with open ("student_grades.csv", "r", newline="") as f:
    reader = csv.DictReader(f,fieldnames=['student_name', 'subject', 'grade'])
    for row in reader:
        list_of_dict.append(row)
print(list_of_dict)

lista_aparitii = []
for student in list_of_dict:
    lista_aparitii.append(student['student_name'])
c= collections.Counter(lista_aparitii)
for i in c:
    print(i)
    break


'''2. : Given the json file people.json:
 a). Write a function that will print all the details of a person. The function will receive an id, 
 ex: print(show_details_by_id("aeec8c5e-f513-4dfd-8435-1d49eb90877c")) => 
{
         "first_name": "Mike",
         "last_name": "McMan",
         "sex": "M",
         "age": 52,
         "partner": "d48da772-fdb0-4b14-9ff5-aafe29c15dc9",
         "children": ["dd69e184-ee18-491c-ba36-db625ba35d8b", "b14031ee-bec5-4902-8e78-95508bd89b64", "9fc00e67-5d00-4830-8679-4e2e66f7fe64"]
 }
 b).  Write a function that will print all the details of a person in a readable way (first name, last name, age, sex, partner, children). 
The function will receive the first_name and last_name of the person.
 ex: print(show_details_by_id("Mike", "McMan")) => 
 First name: Mike
 Last name: McMan
 Sex: M
 Age: 52
 Partner: Mary McMan
 Children: ["Anna", "Adrian", "Danna"]
 c). List the details of the youngest person
 d). List the details for of all the girls Mike has
 e). List the details of the children 'Mike' and 'Mary' have together.
 f). Add a function to marry 2 people, for example Anna to John and do the required changes! 
 g). Add a function to add a new person in people.json using a dict
 ex: add_person({'first_name': 'Mark', 'last_name': 'Bark', 'sex': 'M', 'age': 10}) and it should appear in file 
 Bonus: to test g)., you can add a function to list all people in file

'''
print("\n a)")
def show_details_by_id(person_id):
    with open ("people.json", "r",) as f:
        from_file = json.load(f)
    return from_file['people'][person_id]
print(show_details_by_id("d48da772-fdb0-4b14-9ff5-aafe29c15dc9"))


print("\n b)")
def read_data_base():
    with open ("people.json","r") as f:
        people = json.load(f)
    return people["people"]


def show_details_by_first_and_last_name(first_name, last_name):
    people_dict = read_data_base()
    for person_id, person_details in people_dict.items():
        if person_details['first_name'] == first_name and person_details['last_name'] == last_name:
            partner = people_dict[person_details['partner']]
            children = [people_dict[child_id]['first_name'] for child_id in person_details['children']]
            print(f"First name: {person_details['first_name']}\n"
                  f"Last name: {person_details['last_name']}\n"
                  f"Age: {person_details['age']}\n"
                  f"Sex: {person_details['sex']}\n"
                  f"Partner: {partner['first_name']} {partner['last_name']}\n"
                  f"Children: {children}"
                  )

show_details_by_first_and_last_name("Mike", "McMan")

print("\n c)")

def show_details_of_youngest_person():
    people_dict = read_data_base()
    mini_age = 100
    mini_id_age = None
    for person_id, person_details in people_dict.items():
        if person_details['age'] < mini_age:
            mini_age = person_details['age']
            mini_id_age = person_id
    print(show_details_by_id(mini_id_age))
show_details_of_youngest_person()

print('\n d)')

def show_details_of_Mike_girls():
    people_dict = read_data_base()
    for person_id, person_details in people_dict.items():
        if person_details['first_name'] == 'Mike':
            for child_id in person_details['children']:
                if people_dict[child_id]['sex'] == 'F':
                    print(show_details_by_id(child_id))

show_details_of_Mike_girls()

print('\n e)')


def show_details_of_common_children(id_person1, id_person2):
    people_dict = read_data_base()

    parent1_children_list = set(people_dict[id_person1]["children"])
    parent2_children_list = set(people_dict[id_person2]["children"])
    common_children_ids = parent1_children_list.intersection(parent2_children_list)
    for child_id in common_children_ids:
        print(show_details_by_id(child_id))


show_details_of_common_children("aeec8c5e-f513-4dfd-8435-1d49eb90877c", "d48da772-fdb0-4b14-9ff5-aafe29c15dc9")

print('\n f)')
























