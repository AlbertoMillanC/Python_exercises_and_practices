"""
A pure Python implementation of the quick sort algorithm

For doctests run following command:
python3 -m doctest -v quick_sort.py

For manual testing run:
python3 quick_sort.py
"""
from __future__ import annotations

from random import randrange


def quick_sort(collection: list) -> list:
    """A pure Python implementation of quick sort algorithm

    :param collection: a mutable collection of comparable items
    :return: the same collection ordered by ascending

    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    """
    if len(collection) < 2:
        return collection
    pivot_index = randrange(len(collection))  # Use random element as pivot
    pivot = collection[pivot_index]
    greater: list[int] = []  # All elements greater than pivot
    lesser: list[int] = []  # All elements less than or equal to pivot

    for element in collection[:pivot_index]:
        (greater if element > pivot else lesser).append(element)

    for element in collection[pivot_index + 1 :]:
        (greater if element > pivot else lesser).append(element)

    return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(quick_sort(unsorted))


# arr[] = {10, 80, 30, 90, 40, 50, 70}
# Índices: 0 1 2 3 4 5 6

# bajo = 0, alto = 6, pivote = arr[h] = 70
# # Inicializar el índice de elemento más pequeño,
# i = -1

# Atravesar elementos de j = bajo a alto-1
# j = 0 : Desde arr[j] <= pivote, hacer i++ e swap(arr[i], arr[j])
# i = 0
# arr[] = {10, 80, 30, 90, 40, 50, 70} // Ningún cambio como i y j
#                                      son los mismos

# j = 1 : Desde arr[j] > pivote, no hagas nada
# Sin cambios en i y arr[]

# j = 2 : Desde arr[j] <= pivote, hacer i++ e swap(arr[i], arr[j])
# i = 1
# arr[] = {10, 30, 80, 90, 40, 50, 70} // Intercambiamos 80 y 30

# j = 3 : Desde arr[j] > pivote, no hagas nada
# Sin cambios en i y arr[]

# j = 4 : Desde arr[j] <= pivote, hacer i++ e swap(arr[i], arr[j])
# i = 2
# arr[] = {10, 30, 40, 90, 80, 50, 70} // 80 y 40 Intercambiados
# j = 5 : Desde arr[j] <= pivote, haga i++ e intercambie arr[i] con arr[j]
# i = 3
# arr[] = {10, 30, 40, 50, 80, 90, 70} // 90 y 50 Intercambiados

# Salimos del bucle porque j es ahora igual a high-1.
# Finalmente colocamos pivote en la posición correcta intercambiando
# arr[i+1] y arr[high] (o pivote)
# arr[] = {10, 30, 40, 50, 70, 90, 80} // 80 y 70 Intercambiados

# Ahora 70 está en su lugar correcto. Todos los elementos más pequeños que
# 70 están antes y todos los elementos mayores de 70 años están después
# eso.