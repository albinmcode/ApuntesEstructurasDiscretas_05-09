n = int(input("Introduzca la base de la potencia: "))
k = int(input("Introduzca el exponente de la potencia: "))
def potencia(n, k):
    if k==0:
        return 1
    else:
        return n*potencia(n, k-1)
print("El resultado de la potencia es:", potencia(n, k))