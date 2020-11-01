import time #Libreria Tiempo
import threading #Libreria Hilos


# //////////////////////////////////////////////////////////////////
#                   Comentarios / Consignas para el tp


# Requisitos Generales

# - No se desarrollarán interfaces de usuario, el programa se ejecuta desde la terminal
# - La configuración del sistema operativo a simular se indica a través de flags o parámetros del sistema.
# - Los resultados de la simulación deben imprimirse por pantalla y además guardarse en un archivo.
# - Aquellas cuestiones no especificadas explícitamente, quedan a consideración del alumno.

# Requisitos Simulacion

# - Todos los tiempos se miden en segundos. // quantum
# - La memoria es infinita.
# - Ante cualquier conflicto entre procesos (por ejemplo, dos con igual prioridad) se debe dar prioridad según FCFS.
# - La prioridad 1 es la mayor y la N es la menor.
# - No se realizan llamadas al sistema por I/O de un proceso.
# - Se desconoce (no se requiere) la propiedad usuario de los procesos.
# - Los procesos del sistema operativo a simular se identifican por un código y cuentan con una serie de atributos.
# Estos valores se ingresan al sistema por medio de un archivo de extensión txt cuyo nombre se debe solicitar al inicio 
# de la ejecución delsimulador.
# - Si se están utilizando threads, los mismos podrán acceder al archivo de procesos o imprimir la terminal de a uno.

# Usar funcion time ejemplo

print ('Hoy es -', time.ctime(), time.time())
