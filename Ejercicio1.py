def K(n,p,suma):
    suma+= n*p
    if n==1:
        return suma
    return K(n-1,p,suma)
n = int(input("Ingrese un número n: "))
p = int(input("Ingrese un número p:  "))
sumatoria = K(n,p,0)
print("La sumatoria es: ",sumatoria)
