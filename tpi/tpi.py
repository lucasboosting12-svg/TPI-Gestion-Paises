# TRABAJO INTEGRADOR / LUCAS CLAVERI / RODRIGO MARTIC

# Funciones - Agregar Pais, Actualizar poblacion y superficie, Buscar un Pais por nombre, Filtrar Paises, Ordenar Paises, Estadisticas y Salida.
paises = [] 

# Lista de Paises sincronizado con el CSV.

import csv # Importacion de la libreria csv para manejar archivos CSV

def cargar_paises(ruta_archivo):  # Carga de datos desde un archivo CSV y almacenamiento en una lista de diccionarios
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)

            for fila in lector_csv:
                fila['poblacion'] = int(fila['poblacion'])
                fila['superficie'] = int(fila['superficie']) 
                paises.append(fila)
    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{ruta_archivo}'.")
    return paises

#Funcion para guardar los datos actualizados en el CSV
def guardar_paises(paises, ruta_archivo):
    try:
        with open(ruta_archivo, mode='w', encoding='utf-8', newline='') as archivo:
            encabezados = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor_csv = csv.DictWriter(archivo, fieldnames=encabezados)
            escritor_csv.writeheader()
            escritor_csv.writerows(paises)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

# Funcion secundaria - Agregar_Pais
def agregar_pais(paises):
    print("\n--- AGREGAR PAIS ---")
    
    # Bucle exclusivo para validar el Nombre
    while True:
        try:
            nombre_pais = input("Ingrese el nombre del pais: ").strip().title()
            if nombre_pais == "":
                raise ValueError("No se permiten espacios vacios.")
            
            for caracter in nombre_pais:
                if not caracter.isalpha() and not caracter.isspace():
                    raise ValueError("El nombre no puede contener numeros ni simbolos.")       
            break 
        except ValueError as e:
            print(f"Error: {e} Intentelo de nuevo.\n")

    # Bucle exclusivo para validar el Continente
    while True:
        try:
            continente = input("Ingrese el continente del pais: ").strip().title()
            if continente == "":
                raise ValueError("No se permiten espacios vacios.")
            
            for caracter in continente:
                if not caracter.isalpha() and not caracter.isspace():
                    raise ValueError("El continente no puede contener numeros ni simbolos.")
            break
        except ValueError as e:
            print(f"Error: {e} Inténtelo de nuevo.\n")

    # Bucle exclusivo para validar Superficie y Poblacion
    while True:
        try:
            superficie = int(input("Ingrese la superficie km² del pais: "))
            poblacion = int(input("Ingrese la poblacion del pais: "))
            
            if superficie <= 0 or poblacion <= 0:
                raise ValueError("Los valores deben ser mayores a cero.")
            break
        except ValueError as e:
            print(f"Error: {e} Intentelo de nuevo.\n")

    # Creación del diccionario y guardado en la lista
    nuevo_pais = {
        'nombre': nombre_pais, 
        'continente': continente,
        'superficie': superficie, 
        'poblacion': poblacion
    }

    paises.append(nuevo_pais)
    print("\n--- AGREGADO CON EXITO ---")
    print(f"Nombre Pais: {nombre_pais}, Continente: {continente}, Superficie: {superficie}, Poblacion: {poblacion}")

# Funcion secundaria - Actualizar_Pais
def actualizar_pais(paises):
    print("\n--- ACTUALIZAR PAIS ---")
    pais_a_buscar = input("Ingrese el nombre del pais a actualizar: ").strip().title()
    
    encontrado=False
    for pais in paises:
        if pais["nombre"] == pais_a_buscar:
            encontrado = True
            while True:
                try:
                    superficie = int(input("Ingrese la superficie km² del pais(Actualizada): "))
                    poblacion = int(input("Ingrese la poblacion del pais(Actualizada): "))
                    if superficie <= 0 or poblacion <= 0:
                        raise ValueError("Los valores deben ser mayores a cero.")
                    break
                except ValueError as e:
                    print(f"Error: {e} Intentelo de nuevo.\n")
            pais["superficie"]=superficie
            pais["poblacion"]=poblacion
            print("\n---Datos Cargados Exitosamente---")
            print(f"\nPais: {pais['nombre']} | Superficie(Actual): {superficie} | Poblacion(Actual): {poblacion}")
            break
    if encontrado == False:
        print(f"\nError: No se encontro ningun pais llamado '{pais_a_buscar}'.")

# Funcion secundaria - Buscar_Pais
def buscar_pais(paises):
    print("\n--- BUSCAR PAIS ---")
    pais_a_buscar = input("Ingrese el nombre del pais a buscar: ").strip().title()
    encontrado = False
    for pais in paises:
        
        if pais["nombre"] == pais_a_buscar:
            encontrado = True
            print("---Pais Encontrado---")
            print(f"\nPais: {pais['nombre']} | Continente: {pais['continente']} | Superficie(Actual): {pais['superficie']} | Poblacion(Actual): {pais['poblacion']}")
            break
    if encontrado == False:
        print(f"\nError: No se encontro ningun pais llamado '{pais_a_buscar}'.")

# Funcion secundaria - Filtrar_Pais
def filtrar_paises(paises):
    while True:
        print("\n--- FILTRAR PAISES ---")
        print("1) Filtrar por Continente")
        print("2) Filtrar por Poblacion minima")
        print("3) Rango de superficie")
        print("4) Volver al menu principal")
        opcion_filtro = input("Seleccione una opcion (1-4): ").strip()
        encontrado=False
        contador = 1

        if opcion_filtro == "1":
            continente_filtrar=input("Nombre del continente a filtrar:").strip().title()
            for pais in paises:
                if pais["continente"] == continente_filtrar:
                    encontrado=True
                    print(f"{contador}) Pais: {pais['nombre']}") 
                    contador += 1
                    

            if encontrado == False:
                print(f"\nError: No se encontro ningun continente con ese nombre. '{continente_filtrar}'.")

        elif opcion_filtro == "2":
            print("\n--- FILTRO POR RANGO DE POBLACION ---")
                
            try:
                poblacion_min = int(input("Ingrese la poblacion MINIMA: "))
                poblacion_max = int(input("Ingrese la poblacion MAXIMA: "))
                    
                encontrado = False
                contador = 1
                    
                print(f"\n--- Paises con poblacion entre {poblacion_min} y {poblacion_max} ---")
                    
                for pais in paises:
                    if poblacion_min <= pais["poblacion"] <= poblacion_max:
                        encontrado = True
                        print(f"{contador}) Pais: {pais['nombre']} | Poblacion: {pais['poblacion']}")
                        contador += 1
                    
                if not encontrado:  
                    print("\nError: No se encontraron paises en ese rango de poblacion.")
                        
            except ValueError:
                    print("Error: Por favor, ingrese solo numeros enteros.")

        elif opcion_filtro == "3":
            print("\n--- FILTRO POR RANGO DE SUPERFICIE ---")
            
            try:
                superficie_min = int(input("Ingrese la superficie MINIMA (km²): "))
                superficie_max = int(input("Ingrese la superficie MAXIMA (km²): "))
                
                encontrado = False
                contador = 1
                
                print(f"\n--- Paises con superficie entre {superficie_min} y {superficie_max} km² ---")
                
                for pais in paises:
                    if superficie_min <= pais["superficie"] <= superficie_max:
                        encontrado = True
                        print(f"{contador}) Pais: {pais['nombre']} | Superficie: {pais['superficie']} km²")
                        contador += 1
                
                if not encontrado:
                    print("\nError: No se encontraron paises en ese rango de superficie.")
                    
            except ValueError:
                print("Error: Por favor, ingrese solo numeros enteros.")            

        elif opcion_filtro == "4":
            print("Volviendo al menú principal...")
            break

# Funcion secundaria - Ordenar_Pais
def ordenar_paises(paises):
    while True:
        print("\n--- ORDENAR PAISES ---")
        print("1) Por Nombre (A - Z)")
        print("2) Por Poblacion (Mayor a Menor)")
        print("3) Por Superficie (Mayor a Menor)")
        print("4) Volver al menu principal")
        
        opcion_orden = input("Seleccione una opcion (1-4): ").strip()
        
        if opcion_orden == "1":
            print("\n--- Paises ordenados por Nombre (A-Z) ---")
            paises_ordenados = sorted(paises, key=lambda x: x["nombre"])
            
            contador = 1
            for pais in paises_ordenados:
                print(f"{contador}) Pais: {pais['nombre']} | Continente: {pais['continente']}")
                contador += 1
                
        elif opcion_orden == "2":
            print("\n--- Paises ordenados por Poblacion (Mayor a Menor) ---")
            paises_ordenados = sorted(paises, key=lambda x: x["poblacion"], reverse=True)
            
            contador = 1
            for pais in paises_ordenados:
                print(f"{contador}) Pais: {pais['nombre']} | Poblacion: {pais['poblacion']}")
                contador += 1
                
        elif opcion_orden == "3":
            print("\n--- Paises ordenados por Superficie (Mayor a Menor) ---")
            paises_ordenados = sorted(paises, key=lambda x: x["superficie"], reverse=True)
            
            contador = 1
            for pais in paises_ordenados:
                print(f"{contador}) Pais: {pais['nombre']} | Superficie: {pais['superficie']} km²")
                contador += 1
                
        elif opcion_orden == "4":
            print("Volviendo al menu principal...")
            break
            
        else:
            print("Opcion no valida. Intente de nuevo.")

# Funcion secundaria - Mostrar_Estadisticas
def mostrar_estadisticas(paises):
    print("\n--- ESTADISTICAS GLOBALES ---")
    
    if not paises:
        print("Error: No hay paises registrados para analizar.")
        return
        
    total_paises = len(paises)
    poblacion_total = 0
    superficie_total = 0
    paises_por_continente = {} #Diccionario para contar por continente
    
    for pais in paises:
        poblacion_total += pais["poblacion"]
        superficie_total += pais["superficie"]
        
    
        continente = pais["continente"]   #Contar paises por continente
        if continente in paises_por_continente:
            paises_por_continente[continente] += 1
        else:
            paises_por_continente[continente] = 1
            
    
    promedio_poblacion = poblacion_total // total_paises #Promedios
    promedio_superficie = superficie_total // total_paises
        
    pais_mas_poblado = max(paises, key=lambda x: x["poblacion"])
    pais_menos_poblado = min(paises, key=lambda x: x["poblacion"]) #Agregado
    pais_mas_grande = max(paises, key=lambda x: x["superficie"])
    
    print(f"\nTotal de paises registrados: {total_paises}")
    print(f"Poblacion total combinada: {poblacion_total} habitantes")
    print(f"Superficie total combinada: {superficie_total} km²")
    print("-" * 30)
    print(f"Promedio de poblacion: {promedio_poblacion} hab. por pais")
    print(f"Promedio de superficie: {promedio_superficie} km² por pais")
    print("-" * 30)
    print(f"Pais mas poblado: {pais_mas_poblado['nombre']} ({pais_mas_poblado['poblacion']} hab.)")
    print(f"Pais menos poblado: {pais_menos_poblado['nombre']} ({pais_menos_poblado['poblacion']} hab.)")
    print(f"Pais mas grande: {pais_mas_grande['nombre']} ({pais_mas_grande['superficie']} km²)")
    print("-" * 30)
    print("Cantidad de paises por continente:")
    for cont, cantidad in paises_por_continente.items():
        print(f"- {cont}: {cantidad} pais(es)")

# Funcion principal - Menu repetitivo con interacciones con el usuario. Bloque principal y guardado de funciones secundarias.
def main():

    cargar_paises('dataset.csv') #Cargamos los datos al iniciar el programa

    while True:
        print("\nBienvenido al programa de gestión de países.")
        print("--- Menú Principal ---")
        print("1) Agregar Pais")
        print("2) Actualizar poblacion y superficie")
        print("3) Buscar un pais por nombre")
        print("4) Filtrar paises")
        print("5) Ordenar Paises")
        print("6) Estadisticas")
        print("7) Salir") 
        
        opcion = input("Seleccione una opcion (1-7): ").strip()

        if opcion == "1":
            agregar_pais(paises)
            guardar_paises(paises, 'dataset.csv') # Guardamos los cambios inmediatamente
        
        elif opcion == "2":
            actualizar_pais(paises)
            guardar_paises(paises, 'dataset.csv') 
        
        elif opcion == "3":
            buscar_pais(paises)
        
        elif opcion == "4":
            filtrar_paises(paises)

        elif opcion =="5":
            ordenar_paises(paises)
        
        elif opcion=="6":
            mostrar_estadisticas(paises)
        
        elif opcion == "7":
            print("Saliendo del programa.")
            break
            
        else:
            print("Opcion no valida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()