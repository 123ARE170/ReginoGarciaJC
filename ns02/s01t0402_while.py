
"""
Escribir un programa que calcule 
la suma de los "n" numeros naturales 
por ejemplo si n=100, el programa calculara la suma del 1 al 100
42 usando ciclo while 
"""
# importar la biblioteca 
import time 

#crear varibales 
#el problema 
n = 100
the_sum = 0 

# timepo el t1
timestamp_01 = time.time()

# iniciando la suma 
#100 
while(n > 0 ): 
    the_sum = the_sum + n  #100 + 99 + 98 ... +1 
    n = n -1 

timestamp_02 = time.time() 

# imprimimos la solucion 
print(f"la suma es {the_sum}") 

#caclulear el tiempo 
elapsed_time = round((timestamp_02 - timestamp_01) * 1e6, 2)
print(f"Tiempo de ejecución: {elapsed_time} us")