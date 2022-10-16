sajat_lista = [5, 12, 27, 9, 3, 12,9 ]
k = 12

def remove_element(lista):
    """
    Removes a given k value completely from a list, on every index
    """
    global k
    for i in lista:
        if i == k:
            lista.remove(k)
    return lista

print(remove_element(sajat_lista))