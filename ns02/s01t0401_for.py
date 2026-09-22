"""
Escribir un programa que calcule 
la suma de los "n" numeros naturales 
por ejemplo si n=100, el programa calculara la suma del 1 al 100
42
"""
# importamos biblioteca time 
import time 

#Creando una marca de tiempo 
timestamp_01 = time.time() 

#programa que calcula la suma
#de los "n" numeros naturales 
n = 500
total_sum = 0 

#Ciclo for 
for number in range(1,n+1):  

    total_sum = total_sum +number 
    # 1: sum <- 0 + 1 
    #sum = 1 
    # 2: sum <- 1 + 2
    # 3: sum <- 3 + 3 
    # ...
    # 100: sum <- antSu_(-1) +100 
print(f"La suma de 1 hasta {n} es: {sum}")
     
# toamndo el timepo final 
timestamp_02 = time.time() 

# impresion del tiempo 
print(f"tiempo de ejeecucion:{(timestamp_02-timestamp_01) * 1e6:.2f} " us)