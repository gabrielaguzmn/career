#EJERCICIO NO. 1 - CENTRO DE DIAGNOSTICO

print("---------------------PROGRAMA CENTRO DE DIAGNOSTICO---------------------")
vehicles_num= int(input("Digite la cantidad de vehiculos a revisar en el dia: "))
num = vehicles_num
print("Recuerde los numeros que representan cada una de las marcas de vehiculos:\n1-Mazda\n2- Chevrolet\n3- Renault\n4- Kia")
approved_vehicles = 0
non_approved_vehicles = 0
sum_approved_vehicles = 0
mazda, chevrolet, renault, kia = 0, 0, 0, 0
while vehicles_num!= 0:
    brand= int(input("Digite el numero que representa la marca del vehiculo: "))
    while brand!= 1 and brand!= 2 and brand!= 3 and brand!= 4:
        print("Digite un codigo de marca valido")
        brand= int(input("Digite el numero que representa la marca del vehiculo: "))
    if brand == 1:
        mazda += 1
    if brand == 2:
        chevrolet += 1
    if brand == 3:
        renault += 1
    if brand == 4:
        kia += 1
    model= int(input("Digite el modelo del vehiculo: "))
    vehicle_plate= input("Digite la placa del vehiculo: ").upper()
    calification= float(input("Digite la calificacion: "))
    while calification < 1.0 or calification > 101.0:
        print("Ingrese una calificacion valida")
        calification= float(input("Digite la calificacion: "))
    if calification < 85.0:
        approved_status= ("NO APROBO LA REVISION")
        non_approved_vehicles+= 1
    elif calification >= 85.0 and calification <= 100.0:
        approved_status= ("APROBO LA REVISION")
        approved_vehicles+=1
        
    print("El vehiculo:",brand, "con el numero de placa:", vehicle_plate,"con calificacion de:",calification, approved_status)
    vehicles_num = vehicles_num -1

average = sum_approved_vehicles / approved_vehicles
percentage_approved_vehicles = (approved_vehicles * 100.0)/num
percentage_non_approved_vehicles= (non_approved_vehicles * 100.0)/num
total=""
most_frequent_vehicle_brand =""


if mazda > chevrolet and mazda > renault and mazda > kia:
    most_frequent_vehicle_brand= "Mazda"
    total= mazda
elif chevrolet > mazda and chevrolet > renault and chevrolet > kia:
    most_frequent_vehicle_brand= "Chevrolet"
    total= chevrolet
elif renault > chevrolet and renault > mazda and renault > kia:
    most_frequent_vehicle_brand= "Renault"
    total= renault
elif kia > chevrolet and kia > renault and kia > mazda:
    most_frequent_vehicle_brand= "Kia"
    total= kia


print("******************** INFORME DE LOS DIAGNOSTICOS DEL DIA ********************\n",
      "Cantidad de vehiculos aprobados:",approved_vehicles,"\n",
      "Cantidad de vehiculos no aprobados:",non_approved_vehicles,"\n",
      "Promedio de calificacion de vehiculos aprobados:",average,"\n",
      "Porcentaje de vehiculos aprobados:",percentage_approved_vehicles,"%","\n",
      "Porcentaje de vehiculos no aprobados:",percentage_non_approved_vehicles,"%","\n",
      "La marca de vehiculo mas frecuente es:",most_frequent_vehicle_brand,"con una cantidad de:",total)
