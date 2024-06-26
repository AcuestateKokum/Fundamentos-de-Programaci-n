trabajadores = [["Nombre","Cargo","Sueldo Bruto","Dcto. Salud","Dcto. AFP","Sueldo Liquido"]]
rojo = True
azul = True
naranjo = True
cargos = ["Ceo","Desarrollador","Analista De Datos"]

def registrar(trabajadores):
      nombre = input("Ingrese nombre del trabajador: ").title()
      verde = True
      while verde == True:
         cargo = input("Ingresar cargo (CEO/Desarrollador/Analista de datos): ").title()
         if cargo not in cargos:
             print("Seleccione el cargo correcto")
             continue
         else:
             break
      amarillo = True  
      while amarillo == True:
         try: 
             sueldo_bruto = int((input("Ingrese sueldo bruto: ")))
             
             break
         except ValueError:
             print("Ingrese valor correcto")
             amarillo = True  
    

      desc_salud = round(sueldo_bruto * 0.07)
      desc_afp =  round(sueldo_bruto * 0.12)
      liquido = round(sueldo_bruto - (desc_salud-desc_afp))
      
      trabajadores.append([nombre,cargo,sueldo_bruto,desc_salud,desc_afp,liquido])
        
      return(f"{nombre} Has sido registrado con éxito")

      

def listar_trabajadores(trabajadores):                  
     for a in trabajadores:
         for j in a:
            print(j,end="\t")
         print()   
     
def imprimir(trabajadores):
   seleccionar = input("Ingrese cargo para imprimir planilla: ").title()
   if seleccionar in cargos:
      with open("Listado por cargo.txt",'w') as archivo:
         for a in trabajadores:
            for b in a:
               archivo.write(f"{b}")
         
          
      

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
       if len(trabajadores) ==1:
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
      while naranjo == True:
       if len(trabajadores) ==1:
          print("No se encuentran registros")
          m2 = input("Ingrese (M) para volver al menu: ").upper()
          if m2 == "M":
             naranjo = False
             rojo = True
          else:
             naranjo = True
       else:
            imprimir(trabajadores)
            break
      naranjo = True       
    elif opcion == 4:
      print("Ha salido del programa satisfactoriamente")
      break
    else:
      print("\nIngrese una opciòn valida\n")
      rojo = True
  except ValueError:
     print("\nSeleccione la opción valida\n")     
     rojo = True      

