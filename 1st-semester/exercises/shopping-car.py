def shopping_car():
    price = 1
    item = 1
    total_items = 0
    total_price = 0
    list_items = ""

    while price != 0:
        price = int(input(f"Precio del item {item} es: "))
        if price != 0:
            cant = int(input(f"Cantidad del item {item} es: "))
            total_items += cant
            cost = price*cant
            list_items  = list_items + f"item {item}: cantidad {cant}, le cuesta: {cost}\n"
            total_price = total_price + cost
            
        item = item + 1
        
    print ("Los items comprados son:\n", list_items )
    print("La cantidad de unidades a llevar son: ", total_items)
    print("El valor total de las compras son: ", total_price)
    
shopping_car()