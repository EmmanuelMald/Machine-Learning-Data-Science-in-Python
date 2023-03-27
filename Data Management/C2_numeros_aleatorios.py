# -*- coding: utf-8 -*-
"""
C2

Generación aleatoria de números aleatorios


"""
import numpy as np
import random
import pandas as pd

print(np.random.randint(1,100)) #genera un número entero entre 1 y 100

#la forma más clásica de generar un número aleatorio es entre 0 y 1 (decimales)

print(np.random.random())

#función que genera una lista de n números aleatorios enteros dentro del intervalo [a,b]

def randint_list(n,a,b):
    x=[]
    for i in range(n):
        x.append(np.random.randint(a,b)) 
    return x

#ya existe un método que hace esto por nosotros, con los mismos parámetros y mismos valores que 
#hemos hecho nosotros

print(random.randrange(1,100,6)) #rango entre 1 y 100,que sean múltiplos de 7, solo da un valor

for i in range(10):
    print(random.randrange(1,100,5)) #el punto de partida es 1, por eso es multiplos de 5 + 1
    
"SHUFFLING"

a=np.arange(100) #Genera una lista ordenada de valores desde el 0 hasta el 100, con valores de np
print(a)
a=np.random.shuffle(a) #Desordena la lista
print(a)
data=pd.read_csv(r"C:\Users\LENOVO\OneDrive - Instituto Politecnico Nacional\ARREGLOS\CURSOS\DATA SCIENCE\python-ml-course-master\datasets\customer-churn-model\Customer Churn Model.txt")
col=data.columns.values.tolist()
print(col)
print(np.random.choice(col)) #permite seleccionar una columna al azar

"""
SEMILLA:
    
Se establece el valor para el cual se inicia el conjunto de números aleatorios para guardar estos
datos y que se vuelvan repetibles"""

np.random.seed(2018) #el número que se escoge es el que el usuario quiera
for i in range(5):
    print(np.random.random()) # Con la semilla, salen los mismos números
    