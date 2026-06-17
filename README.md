# TPI-Gestion-Paises

## Descripcion del Proyecto
Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar una base de datos de países. El sistema lee la información desde un archivo CSV (`dataset.csv`) y permite realizar operaciones de creación, lectura, actualización, filtrado, ordenamiento y cálculo de estadísticas globales. 

El objetivo principal es aplicar y demostrar el dominio de las estructuras de datos fundamentales en Python (listas y diccionarios), el diseño modular mediante funciones, el manejo de excepciones y la persistencia de datos en archivos de texto plano.

## Enlaces Importantes
* **Video Demostrativo:** https://www.youtube.com/watch?v=lCJbISFdcpg
* **Documentación Técnica (PDF):** En la Carpeta TPI del repositorio

## Instrucciones de Uso e Instalación

### Requisitos previos
* Python 3.x instalado en el sistema.
* Archivo `dataset.csv` ubicado en la misma carpeta que el script principal.

### Ejecución
1. Clonar o descargar este repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el script principal con el siguiente comando:
   ```bash
   python main.py


### Funcionalidades Principales (Menú)
**Agregar País:** Permite registrar un nuevo país ingresando su Nombre, Continente, Superficie y Población. Cuenta con validaciones estrictas para evitar campos vacíos o tipos de datos incorrectos.

**Actualizar Población y Superficie:** Busca un país por nombre y permite modificar sus datos numéricos, guardando los cambios automáticamente en el CSV.

**Buscar País:** Realiza una búsqueda por coincidencia exacta de nombre y muestra la información detallada del país.

**Filtrar Países:** Submenú que permite visualizar grupos de países según:

Continente específico.

Rango de población (mínima y máxima).

Rango de superficie (mínima y máxima).

**Ordenar Países:** Submenú para ordenar y visualizar la lista completa según:

Nombre (Alfabéticamente A-Z).

Población (De mayor a menor).

Superficie (De mayor a menor).

**Estadísticas:** Calcula y muestra indicadores clave globales como totales, promedios, los países con valores máximos/mínimos y la cantidad de países por continente.


## Ejemplos de Entradas y Salidas

**Ejemplo 1: Agregar un país**

--- AGREGAR PAIS ---
**Ingrese el nombre del pais:** Italia
**Ingrese el continente del pais:** Europa
**Ingrese la superficie km² del pais:** 301340
**Ingrese la poblacion del pais:** 59000000

--- AGREGADO CON EXITO ---
Nombre Pais: Italia, Continente: Europa, Superficie: 301340, Poblacion: 59000000

**Ejemplo 2: Estadísticas Globales**

--- ESTADISTICAS GLOBALES ---
Total de paises registrados: 4
Poblacion total combinada: 672109800 habitantes
Superficie total combinada: 11653182 km²
------------------------------
Promedio de poblacion: 168027450 hab. por pais
Promedio de superficie: 2913295 km² por pais
------------------------------
Pais mas poblado: Brasil (213993437 hab.)
Pais menos poblado: Argentina (45376763 hab.)
Pais mas grande: Brasil (8515767 km²)
------------------------------
Cantidad de paises por continente:
- America: 2 pais(es)
- Asia: 1 pais(es)
- Europa: 1 pais(es)