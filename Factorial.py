n = int(input("Introduzca un número entero para saber su factorial: "))
def factorialde(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorialde(n-1) 
print("El factorial de dicho número es", factorialde(n))