trabajadores = []
rojo = True
azul = True
cargos = ["Ceo","Desarrollador","Analista De Datos"]

def registrar(trabajadores):
      nombre = input("Ingrese nombre del trabajador: ").title()
      verde = True
      while verde == True:
         cargo = input("Ingresar cargo (CEO/Desarrollador/Analista de datos: )").title()
         if cargo not in cargos:
             print("Seleccione el cargo correcto")
             continue
         else:
             break
      amarillo = True  
      while amarillo == True:
         try:  
             sueldo_bruto = int(input("Ingrese sueldo bruto: "))
             break
         except ValueError:
             print("Ingrese valor correcto")
             amarillo = True  
    

      desc_salud = sueldo_bruto * 0.07
      desc_afp =  sueldo_bruto * 0.12
      liquido = sueldo_bruto - (desc_salud-desc_afp)

      trabajadores.append([
       "Nombre:",nombre,
       "Cargo:",cargo,
       "Sueldo Bruto:",sueldo_bruto,
       "Des. salud:",desc_salud,
       "Des. AFP:",desc_afp,
       "Sueldo Liquido:",liquido,
        ])
      return("Has sido registrado con exito")

def listar_trabajadores(trabajadores):                   
    for a in trabajadores:
     print(a)


while rojo == True:
  try:  
    hola = "\nBienvenido al Mejor registro de sueldos\n"
    menu=(hola,"1.-Registrar Usuario","2.-Listar todos los trabajadores","3.Imprimir planilla sueldos","4.-Salir del programa")
    for a in menu:
      print(a)
      continue
    opcion = int(input("\nSeleccione su opciòn: "))
    if opcion ==1:
      registrar(trabajadores)
    elif opcion == 2:
      while azul == True:
       if trabajadores == []:
          print("No se encuentran registros")
          m1 = input("Ingrese (M) para volver al menu: ").upper()
          if m1 == "M":
             azul = False
             rojo = True
          else:
             azul = True
       else:
            listar_trabajadores(trabajadores)
            break
      azul = True   
    elif opcion == 3:
      ""
    elif opcion == 4:
      print("Ha salido del programa satisfactoriamente")
      break
    else:
      print("Ingrese una opciòn valida\n")
      rojo = True
  except ValueError:
     print("Seleccione la opción valida\n")     
     rojo = True      

