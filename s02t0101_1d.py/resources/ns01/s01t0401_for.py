"""
Escribir un programa que calcule 
la suma de los "n" numeros naturales 
por ejemplo si n=100, el programa calculara la suma del 1 al 100
42
"""
import time 

# Función que suma los primeros "n" números naturales
def sum_of_n(n):
    total_sum = 0 
    for number in range(1, n + 1):   
        total_sum = total_sum + number 
    return total_sum

# Variable para guardar el dataset
dataset = [] # [(n, time, sum)]

# Generando el contenido del dataset (10 iteraciones: 1 a 10)
for repetition in range(1, 11): 
    # Calculamos N para esta repetición
    n = repetition * 500 
    
    # Tomamos el tiempo inicial
    timestamp_01 = time.time() 

    # Ejecutamos la función
    result = sum_of_n(n)

    # Tomamos el tiempo final
    timestamp_02 = time.time() 

    # Calculamos el tiempo transcurrido en microsegundos
    elapsed_time = round((timestamp_02 - timestamp_01) * 1e6, 2)

    # Agregamos la tupla (n, tiempo, suma) al dataset
    dataset.append((n, elapsed_time, result))

# Imprimimos los resultados al finalizar el ciclo
for tup in dataset: 
    print(tup)