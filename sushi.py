

menu_sushi = 1
roll1 = "Pikachu Roll"
roll2 = "Otaku Roll"
roll3 = "Pulpo Venesoso Roll"
roll4 = "Anguila electrica Roll"
r1 = 4500
r2 = 5000
r3 = 5200
r4 = 4800
cantidad_total1 = 0
cantidad_total2 = 0
cantidad_total3 = 0
cantidad_total4 = 0
menu_cupon = 1
codigo = "soyotaku"


while menu_sushi == 1:

    tipos_roll = int(input("1.Pikachu Roll....$4500\n2.Otaku Roll....$5000\n3.Pulpo Venenoso Roll....$5200\n4.Anguila Electrica Roll....$4800\n\nEliga una opción: "))

    if tipos_roll == 1:
        cantidad1 = int(input("\n¿Cuantos roll desea?: "))     
        cantidad_total1 = cantidad1*r1

    if tipos_roll == 2:
        cantidad2 = int(input("\n¿Cuantos roll desea?: "))     
        cantidad_total2 = cantidad2*r2

    if tipos_roll == 3:
        cantidad3 = int(input("\n¿Cuantos roll desea?: "))     
        cantidad_total3 = cantidad3*r3

    if tipos_roll == 4:
        cantidad4 = int(input("\n¿Cuantos roll desea?: "))     
        cantidad_total4 = cantidad4*r4

    total_final = int(cantidad_total1+cantidad_total2+cantidad_total3+cantidad_total4)
    

    otro = int(input("\nDesea otro tipo de roll(Si = 1 / No = 0)\n"))
    

    if otro == 1:
        menu_sushi = 1

    elif otro == 0:
        menu_sushi = 0
        
        

while menu_cupon == 1:

    cupon = int(input("Tiene codigo de descuento (Si = 1 / No = 0)"))

    if cupon == 1:
        dcto = input("Ingrese su codigo de descuento: ")    

    if dcto == codigo:
        menu_cupon = 0
        total_descuento = (total_final-(total_final*0.1))

    if dcto != codigo:
     print("jajajaj")

    elif cupon == 0:
        menu_cupon = 0    

    


    

       




        





    