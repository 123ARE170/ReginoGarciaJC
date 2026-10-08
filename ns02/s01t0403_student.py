'''
1. Identifico el tamaño de la entradac} "n"
El tamaño de la entrada es el numero 
de estudiantes 
2. es ver cuanto crece el numero de operaciones
en mi algoritmo conforme 
crece el tamaño de la entrada 
0(n) + 0(4) = 0(n+4) = 0(n)  
'''
#Creando una lista de estudiantes 
student_list_01 = ['Jodan','Pipen','Curry','Shack'] 
student_list_02 = ['Mike','Saul','Walter','Jessy'] 

# Verificando presencia de estudiante 
def check_student (input_student, student_list):
    for student in student_list: 
        if input_student == student: # 0(n)
            print ("Estuidante Econtrado")
            return student # 0(1) 
    # Si no encuentro al estudiante 
    print ("Estuidante NO  Econtrado") # 0(1)
    return None # 0(1) 

#Probando algortimo 
check_student("Walter", student_list_01)     
