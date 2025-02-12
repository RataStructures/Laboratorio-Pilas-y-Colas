
from DataStructures.Queue import queue as q
from DataStructures.Utils.utils import handle_not_implemented


def setup_queue():
    # Inicializa una cola vacía para pruebas
    return q.new_queue()


@handle_not_implemented
def test_new_queue():
    # Verifica que la cola se crea correctamente y está vacía
    my_queue = setup_queue()

    assert type(my_queue) == dict
    assert my_queue["size"] == 0
    assert my_queue["elements"] == []


@handle_not_implemented
def test_enqueue():
    # Verifica que los elementos se agregan correctamente al final de la cola
    my_queue = setup_queue()

    q.enqueue(my_queue, 1)

    assert my_queue["size"] == 1
    assert my_queue["elements"][-1] == 1  


@handle_not_implemented
def test_dequeue():
    # Verifica que el `dequeue` retira y devuelve el primer elemento de la cola
    my_queue = setup_queue()

    q.enqueue(my_queue, 10)
    q.enqueue(my_queue, 20)
    first_element = q.dequeue(my_queue)

    assert first_element == 10
    assert my_queue["size"] == 1
    assert my_queue["elements"][0] == 20  


@handle_not_implemented
def test_peek():
    # Verifica que `peek` devuelve el primer elemento sin eliminarlo
    my_queue = setup_queue()

    q.enqueue(my_queue, "A")
    q.enqueue(my_queue, "B")
    first_element = q.peek(my_queue)

    assert first_element == "A"
    assert my_queue["size"] == 2  


@handle_not_implemented
def test_is_empty():
    # Verifica si la cola detecta correctamente si está vacía o no
    my_queue = setup_queue()

    assert q.is_empty(my_queue) is True

    q.enqueue(my_queue, 5)

    assert q.is_empty(my_queue) is False


@handle_not_implemented
def test_size():
    # Verifica que `size` devuelve el número correcto de elementos
    my_queue = setup_queue()

    assert q.size(my_queue) == 0

    q.enqueue(my_queue, "X")
    q.enqueue(my_queue, "Y")

    assert q.size(my_queue) == 2
