# Vectors

array =[5,7,8,9,15,2,3,4,7,7,12,34,56,65,73,23,14,56,86,33,21,213,45,12,3,5,198]
num = 1
odd_numbers_sum = 0
while num > 0:
    num = int(input("Ingrese un numero positivo o uno negativo para finalizar el programa: "))
    if num % 3 == 0 and num % 5 != 0 and num > 0:
        mitada= len(array)/2
        for i in range(0,int(mitada),1):
            array[i] = array[i] - 3
        print("El numero ingresado era multiplo de 3, se le restaron 3 unidades a la mitad de los datos del array")
        print(array)

    if num % 5 == 0 and num % 3 != 0 and num > 0:
        for a in range(0, len(array),1):
            array[a]= array[a] - 1
        print("El numero ingresado era multiplo de 5, se le resto 1 unidad a cada dato del array")
        print(array)

    if num % 5 == 0 and num % 3 == 0 and num > 0:
        for b in range(0, len(array),1):
            if array[b] % 2 != 0:
                odd_numbers_sum = odd_numbers_sum + array[b]
        print("El numero ingresado era multiplo de 5 y 3\nLa suma de los numeros impares del array es: "+str(odd_numbers_sum))

    if num % 5 != 0 and num % 3 != 0 and num > 0:
        smitad= len(array)/2
        for c in range(int(smitad),len(array),1):
            array[c]= array[c] + 4
        print("El numero ingresado NO es multiplo ni de 3, ni de 5, se le sumaron 4 unidades a cada dato de la segunda mitad del array")
        print(array)

    if num < 0:
        print("Programa finalizado")