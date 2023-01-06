def convertidorDeBase10(n,base,k):
    listaNumeroConvertido = []
    numero = n
    while k <= numero:
        residuo = numero%k
        numero = int(numero/k)
        listaNumeroConvertido.append(residuo)
        if numero < k:
            listaNumeroConvertido.append(numero)
    return listaNumeroConvertido
def convertidorABase10(n,base):
    suma = 0
    lista = [int(x) for x in str(n)]
    lista.reverse()
    for x in range(0,len(lista)):
        numero =lista[x]*(base**x)
        suma+= numero
    return suma
numero = int(input("Ingrese el numero: "))
baseNumero = int(input("Ingrese la base del numero: "))
baseConversion = int(input("Ingrese la base a cambiar: "))
if baseNumero != 10:
    numero = convertidorABase10(numero,baseNumero)
    baseNumero = 10
    numeroConvertido = convertidorDeBase10(numero,baseNumero,baseConversion) 
else:
    numeroConvertido = convertidorDeBase10(numero,baseNumero,baseConversion)     
numeroConvertido.reverse()
StrNumero = "".join(map(str, numeroConvertido))
print("El numero convertido es:",StrNumero)