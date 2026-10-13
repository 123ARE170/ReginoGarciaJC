#Array 
#from array immport * 
import array as arr

#creacion de un arrglo 
# i: Entero con signo 
# I: Entero sin signo 
# f: Numero decimal 
# d: Numero decimal doble 
# u: Crácteres unicode
my_array = arr.array('i',[200,20,2.12,22,32,42,52,62,72,82,92]) 
#interaccion automatica 
# for num in my_array: 
#     print(num)
#Acceso individual a los elementos 
# print(my_array[0]) # primer elemento 
# print(my_array[1]) # segubdo elemento 
# print(my_array[1]) # tercer elemento 
#tamño de arreglo 
#length
print(len(my_array))
#interaccion por indices 
for i in range(len(my_array)):
    #print(f"Elemento {i+1}: {my_array[i]}")
    if my_array[1] % 2 == 0: 
        print(f"Elemento Num {i+1}:{my_array[i]}")
        
