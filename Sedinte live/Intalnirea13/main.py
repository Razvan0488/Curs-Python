# C13_EX01: Daca presupunem urmatorul dictionar ca fiind resursele/baza noastra de date

meniu = {
    "id_preparat_1": {
        "nume": "omleta",
        "gramaj": 200,
        "pret": 15
    },
    "id_preparat_2": {
        "nume": "steak de vita",
        "gramaj": 350,
        "pret": 125
    },
    "id_preparat_3": {
        "nume": "salata",
        "gramaj": 300,
        "pret": 30
    },
}


# API de a afla pretul unui preparat
def afla_pret(alegere):
    for preparat in meniu:
        if meniu[preparat]['nume'] == alegere:
            return meniu[preparat]['pret']


print(afla_pret("steak de vita"))