
usuarios = []
primer = True
opt1 = True
def menu1():
    raya ="-"*50
    saludo ="Bienvenid@ a DeliNet"
    print(f'{raya}\n{saludo.center(50," ")}\n{raya}\n')
    m1 = tuple(["1.-Registrar Usuario","2.-Ingresar","3.-Salir"])    
    print(f'{m1[0].center(50," ")}\n{m1[1].center(42," ")}\n{m1[2].center(37," ")}')    
    return("")

def menu_comida():
   raya2 = "-"*50
   saludo2 = "Productos"
   print(f'{raya2}\n{saludo2.center(50," ")}\n{raya2}\n')
   m2 = tuple(["1.-Italiana Carne","2.-Italiana Pollo","3.-Italiana Champiñon"])    
   print(f'{m2[0].center(50," ")}\n{m2[1].center(42," ")}\n{m2[2].center(37," ")}')

def registrar():   
   usuarios=[["Nombre,Edad,Nombre Usuario","Contraseña","Dirección","Correo"]]
   usuarios.append([input("Ingrese su nombre: "),
                       input("Ingrese su edad: "),
                       input("Ingrese su nombre de usuario: "),
                       input("Ingrese su contraseña: "),
                       input("Ingrese su dirección: "),
                       input("Ingrese su correo: ")])
   print("Has sido registrado con exito")
   

while primer==True:
    print(menu1())
    try:
        opt = int(input("Ingrese su opción: "))
        if opt <1 or opt >3:
         print("Por favor, ingrese una opción correcta")
         primer = True
        else:
         primer = False
    except ValueError:
     print("Por favor, ingrese un numero entero")  
    while opt1 == True:
            if opt==1:
             print(registrar())
             opt = False
            elif opt==2:
             if len(usuarios) == 0:
                print("No se encuentra ningun usuario registrado")
                vuelva = True
                while vuelva==True:
                   volver = input("Ingrese (M), para volver al menu: ")
                   if volver.upper() == "M":
                      vuelva= False
                      opt1 = False
                      primer = True
                   else:
                      print("Ingrese la letra correcta")
                      vuelva = True
             else:
               usuario = input("Ingrese su usuario: ")
               contraseña = input("Ingrese su contraseña: ")

               if usuario == usuarios[1][2] and contraseña== usuarios[1][3]:
                 print(menu_comida())
              
            else:
              opt = False
              primer = False   


      