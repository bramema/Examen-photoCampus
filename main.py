while True:
    
    print("======= PhotoCampus =======")
    print("1. ver paquetes")
    print("2. registrar servicios")
    print("3. configuracion")

    print("===========================")
    op = input("Opcion: ")
    print("===========================")

    match op:

        case "1":
            print("paquetes ")

        case "2":
            print("servicios")
        
        case "3":
            print("configuracion")
            print("===========================")
            print("1. agregar nuevos servicios")
            print("2. editar servicios")
            print("3. eliminar servicios")
            print("4. volver al menu")

            print("===========================")
            configuracion = input("opcion: ")
            print("===========================")

            if configuracion == "1":
                print("1. agregar nuevos servicios")

            elif configuracion == "2":
                 print("2. editar servicios")

            elif configuracion == "3":
                print("3. eliminar servicios")

            elif configuracion == "4":
                print("4. volver al menu")
                print("===========================")

            else:
                print("OPcion invalida ")    

        case _:
            print("opcion valida")






           
            
            
            