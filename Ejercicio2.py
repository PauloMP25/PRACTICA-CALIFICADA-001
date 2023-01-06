def convertidorNumeroHexadecimal(n):
    listaResiduo = []
    numero = n
    while 16 <= numero:
        residuo = numero%16
        numero = int(numero/16)
        listaResiduo.append(residuo)
        if numero < 16:
            listaResiduo.append(numero)
    return listaResiduo
def cambiarEquivalenciasDelSistemaHexadecimal(lista):
    listaNumeroConvertido= []
    listaEquivalencias = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    lista.reverse()
    for elemento in lista:
        posicion = elemento
        listaNumeroConvertido.append(listaEquivalencias[posicion])
    return listaNumeroConvertido
    
numero = int(input("Ingrese el numero: "))
numeroHexadecimal = convertidorNumeroHexadecimal(numero)
numeroConvertido = cambiarEquivalenciasDelSistemaHexadecimal(numeroHexadecimal)
StrNumero = "".join(map(str, numeroConvertido))
print("El numero: ",numero,"en el sistema hexadecimal es: ",StrNumero)
