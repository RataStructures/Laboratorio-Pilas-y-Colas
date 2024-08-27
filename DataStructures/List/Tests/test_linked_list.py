from DataStructures.List import single_linked_list as lt
from DataStructures.Utils.utils import handle_not_implemented


def setup_tests():
    return lt.new_list(cmpfunction=None, module="SINGLE_LINKED", key=None)


@handle_not_implemented
def test_new_list():
    lista = setup_tests()
    assert lista["first"] is None
    assert lista["last"] is None
    assert lista["size"] == 0
    assert lista["type"] == "SINGLE_LINKED"


@handle_not_implemented
def test_add_first():
    lista = setup_tests()

    lt.add_first(lista, 1)
    lt.add_first(lista, 2)
    lt.add_first(lista, 3)

    assert lista["size"] == 3
    assert lista["first"]["info"] == 3


@handle_not_implemented
def test_add_last():
    lista = setup_tests()

    lt.add_last(lista, 1)
    lt.add_last(lista, 2)
    lt.add_last(lista, 3)

    assert lista["size"] == 3
    assert lista["first"]["info"] == 1
    assert lista["first"]["next"]["info"] == 2
    assert lista["first"]["next"]["next"]["info"] == 3


@handle_not_implemented
def test_is_empty():
    lista = setup_tests()

    assert lt.is_empty(lista) == True

    lt.add_first(lista, 1)
    assert lt.is_empty(lista) == False


@handle_not_implemented
def test_get_size():
    lista = setup_tests()

    assert lt.size(lista) == 0

    lt.add_first(lista, 1)

    assert lt.size(lista) == 1


@handle_not_implemented
def test_get_first_element():

    lista = setup_tests()

    lt.add_first(lista, 1)
    lt.add_first(lista, 2)
    lt.add_first(lista, 3)
    assert lt.first_element(lista) == 3


@handle_not_implemented
def test_get_last_element():

    lista = setup_tests()

    lt.add_first(lista, 1)

    lt.add_first(lista, 2)
    lt.add_first(lista, 3)
    assert lt.last_element(lista) == 1


@handle_not_implemented
def test_get_element():

    lista = setup_tests()

    lt.add_first(lista, 1)
    lt.add_first(lista, 2)
    lt.add_first(lista, 3)

    assert lt.get_element(lista, 1) == 3
    assert lt.get_element(lista, 2) == 2
    assert lt.get_element(lista, 3) == 1


@handle_not_implemented
def test_remove_first():
    lista = setup_tests()

    lt.add_first(lista, 1)
    lt.add_first(lista, 2)
    lt.add_first(lista, 3)

    lt.remove_first(lista)

    assert lista["size"] == 2
    assert lista["first"]["info"] == 2
    assert lista["first"]["next"]["info"] == 1

@handle_not_implemented
def test_remove_last():
    lista = setup_tests()

    lt.add_last(lista, 1)
    lt.add_last(lista, 2)
    lt.add_last(lista, 3)

    lt.remove_last(lista)

    assert lista["size"] == 2
    assert lista["first"]["info"] == 1
    assert lista["last"]["info"] == 2


@handle_not_implemented
def test_insert_element():
    lista = setup_tests()

    lt.add_first(lista, 1)
    lt.add_first(lista, 2)
    lt.add_first(lista, 3)

    lt.insert_element(lista, 2, 4)
    lt.insert_element(lista, 8, 2)
    print(lista)
    assert lista["size"] == 5
    assert lista["last"]["info"]==2
    assert lista["first"]["next"]["info"]==8


@handle_not_implemented
def test_is_present():
    lista = setup_tests()

    lt.add_first(lista, 1)
    lt.add_first(lista, 2)
    lt.add_first(lista, 3)

    assert lt.is_present(lista, 1) == 3
    assert lt.is_present(lista, 2) == 2
    assert lt.is_present(lista, 3) == 1
    assert lt.is_present(lista, 4) == 0


@handle_not_implemented
def test_delete_element():
    lista = setup_tests()

    lt.add_first(lista, 1)
    lt.add_first(lista, 2)
    lt.add_first(lista, 3)

    lt.delete_element(lista, 2)

    assert lista["size"] == 2
    assert lista["first"]["next"]["info"] ==1


@handle_not_implemented
def test_change_info():
    lista = setup_tests()

    lt.add_first(lista, 1)
    lt.add_first(lista, 2)
    lt.add_first(lista, 3)

    lt.ichange_info(lista, 2, 4)

    assert lista["size"] == 3
    assert lista["first"]["info"] == 3
    assert lista["first"]["next"]["info"] == 4
    assert lista["last"]["info"] == 1



@handle_not_implemented
def test_exchange():
    lista = setup_tests()

    lt.add_first(lista, 1)
    lt.add_first(lista, 2)
    lt.add_first(lista, 3)

    lt.exchange(lista, 1, 2)

    assert lista["size"] == 3
    assert lista["first"]["info"] == 2 
    assert lista["first"]["next"]["info"] == 3
    assert lista["last"]["info"] == 1 




@handle_not_implemented
def test_sub_list():
    lista = setup_tests()

    lt.add_last(lista, 1)
    lt.add_last(lista, 2)
    lt.add_last(lista, 3)

    sub_list = lt.sub_list(lista, 1, 2)

    assert sub_list["size"] == 2
    assert sub_list["first"]["info"] == 1
    assert sub_list["first"]["next"]["info"] == 2
    assert sub_list["last"]["info"] == 2
    assert sub_list["datastructure"] == "SINGLE_LINKED"
