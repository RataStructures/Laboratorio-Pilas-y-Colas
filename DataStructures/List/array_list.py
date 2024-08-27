def new_list():
    newList = {
        "elements": [],
        "size":0
    }
    return newList

def add_first(lista, element):
    lista["elements"].insert(0,element)
    lista["size"]+=1
    return lista

def add_last(lista, element):
    lista["elements"].append(element)
    lista["size"]+=1
    return lista