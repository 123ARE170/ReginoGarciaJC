
from array import array as arr 
#impresion de una tabla 
def print_table(imput_table):
    # imprimiendo cada elemento 
    for row in table: 
     for column in row: 
        print(column, end=",")
    print("\b") 
    
table = [
    arr('i',[1,2,3]),
    arr('i',[4,5,6]),
    arr('i',[7,8,9]),
]
print_table(table) 

# Insercion 
row = 1 
column = 2 
value = 99 
#Insertar en la fila 1 columna 2 el valor 99 
table[row].insert(column, value)

#imprimiendo mensaje 
print("-- DESPUES DE LA ISERCCION DEL ELEMENTO ---")
print_table(table) #dry 

# INSERTANDO  UNA FILA COMPLETA 
new_row = arr('i',[100,200,300])
pos = 1 
table.insert(pos, new_row)

# imprimir mensaje ble
print("--- despues del a insercion de fila ---")
print_table(table) 

# eliminacion 
del table[2]

print("--- ELIMINACION ---")
print_table(table)