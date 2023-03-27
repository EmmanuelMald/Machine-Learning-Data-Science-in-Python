# -*- coding: utf-8 -*-
"""
C6 agrupación de datos por categorías

Agrupar, agregar y filtrar datasets
Agregar datos es combinarlos con algún criterio, utilizando una variable categórica 

Agregación de datos por categoría

primero se generará un dummie dataset con información numérica y categórica
"""
import pandas as pd
import numpy as np

n=500 #tamaño del dataset
gender=["Male","Female"] #variable categórica
income_class=["Poor","Middle Class","Rich"] #variable categórica
gender_data=[]
income_data=[]
for i in range(n): #crear mis datos de variables categóricas
    gender_data.append(np.random.choice(gender)) #np.random.choice(gender) Elige aleatoriamente un valor de la lista
    income_data.append(np.random.choice(income_class)) 

height=160 + 30*np.random.randn(n) #el peso, altura, edad e ingreso de las personas siguen una distribución normal
weigth=65 + 25*np.random.randn(n) #np.ceil() da el siguiente número entero del número flotante, pero hay que pasarlo a entero
age=30+ 12*np.ceil(np.random.randn(n))
income=18000 + 3500*np.random.randn(n)
data=pd.DataFrame({
    "Gender": gender_data,
    "Social Status": income_data,
    "Height":height,
    "Weight":weigth,
    "Age":age,
    "Income": income  
    })
print(data.dtypes)

#Agrupación por variables categóricas
""" 
    Para hacer una agrupación de datos categóricos, se usa la función data.groupby("nombre de la columna categórica")

"""

grouped_gender=data.groupby("Gender") #crea un objeto llamado groupby con dos atributos, el nombre y el grupo.
#Siempre crear una variable cuando se use esa función. Para acceder a ella, funciona como pedir un dato de una lista

print(grouped_gender.groups) #grouped_gender.groups muestra el diccionario de las variables categóricas y 
# en el diccionario está la posición de la variable a la que se refiere cada fila

for names,groups in grouped_gender:
    print(names,groups) #muestra todos los datos
    
mujeres=grouped_gender.get_group("Female") #Regresa todas las filas del dataset que tengan en la variable categórica "Gender"
                                    # el valor de "Female" #La función me regresa un dataframe


#AGRUPACIÓN POR MÁS DE UNA CATEGORÍA CATEGÓRICA:
double_group=data.groupby(["Gender","Social Status"]) #saldrán 6 categorías, que son las combinaciones posibles de
#organizar las variables categóricas de Gender (2, male, female) y Social Status (3, poor, middle class,rich)
for names, groups in double_group:
    print(names)
    print(groups)

mujeres_ricas=double_group.get_group(("Female","Rich")) #debe ponerse una tupla de las variables categóricas que quieres

"""Agregar datos es aplicarle una función, una operación o algo a mi grupo de datos

    Operaciones sobre datos agrupados

"""

print(double_group.sum()) #suma todos los valores de cada una de las categorías
double_group.mean() #da las medias de cada una de las categorías
double_group.size() #nos permite saber cuántas cosas hay en cada categoría
double_group.describe() #da todos los estadísticos para cada categoría

"""
Los objetos groupby se comportan del mismo modo que cualquier dataframe, es decir, se puede seleccionar una de
las columnas del groupby

"""

grouped_income=double_group["Income"]
grouped_income.describe()


"""El método agregate nos sirve para agregar conjuntamente los valores que nos interesen, por ejemplo,
    la suma de las edades
"""

double_group.aggregate({
    "Income": np.sum, #dame la suma de los ingresos
    "Age": np.mean, #dame el promedio de las edades 
    "Height": np.std #dame la desviación estándar de la altura
    })
"""Para trabajar con este tipo de datos se usa el método lambda para definir un tipo de cálculo específico en python

Supongamos que en lugar de querer el promedio de la edad, queremos la tipificación de la edad, es decir,
queremos la media de la edad divido por la desviación típica
"""

double_group.aggregate({
    
     "Age": np.mean,
     "Height": lambda x: np.mean(x)/np.std(x) #x es la variable que se va a usar para hacer el cálculo deseado
    })

"""Si a todas las columnas le quiero aplicar la misma operación:
    
    En lugar de un diccionario, se pone una lista con las operaciones que quieren ponerle a todas las variables"""

double_group.aggregate([np.sum,np.min,np.std])
double_group.aggregate([lambda x: np.mean(x)/np.std(x)])