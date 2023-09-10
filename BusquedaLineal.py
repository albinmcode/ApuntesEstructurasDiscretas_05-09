l = [1, 7, 9, 14, 75]
a = int(input("Introduzca el número que desea buscar: "))
def linear_search(l, a):
    return linear_search_aux(l, a, 0)
def linear_search_aux(l, a, i):
    if i == len(l):
        return False
    elif l[i] == a:
        return True
    else:
        return linear_search_aux(l, a, i+1)
if linear_search(l, a):
    print("El número", a, "sí se encuentra en la lista")
else:
    print("El número", a, "no se encuentra en la lista")