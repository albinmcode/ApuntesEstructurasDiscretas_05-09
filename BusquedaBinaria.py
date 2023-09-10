l = [0, 1, 7, 9, 14, 75, 111] #debe estar ordenado
a = int(input("Introduzca el número que desea buscar: "))
def binary_search(l, a):
    return _binary_search(l, 0, len(l)-1, a, 0)
def _binary_search(l, low, high, a, contador):
    if contador > len(l)//2: #condición de parada
        return False #si recorrió más de la mitad del arreglo, no esta
    contador += 1
    mid = (high+low) // 2
    if l[mid] == a:
        return True
    elif l[mid] > a:
        return _binary_search(l, low, mid-1, a, contador)
    else:
        return _binary_search(l, mid+1, high, a, contador)
if binary_search(l, a):
    print("El número", a, "sí se encuentra en la lista")
else:
    print("El número", a, "no se encuentra en la lista")