# -*- coding: utf-8 -*-
"""
CLASE 7 

Dummy variables

Separa las diferentes variables categóricas, de manera que puedas tener una variable cuantitativa
se genera otra columna con la variable dummie

Por ejemplo, en el dataset, se tiene la variable categórica sex, (hombre/mujer), se crean dos variables
dummie, una variable hombre (1/0 si es o no hombre), y una variable mujer (1/0 si es o no mujer)
"""
import pandas as pd

path="C:\\Users\\LENOVO\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\CURSOS\\DATA SCIENCE\\python-ml-course-master\\datasets"
filename="\\titanic\\titanic3_limpio.csv"
mainpath=path+filename

data=pd.read_csv(mainpath)

"""dummy_sex=pd.get_dummies(qué columna se convierte en dummie, prefix="sex")
Lo que hará será hacer dos variables con las dos opciones de la varible categórica, serán llamadas
sex_male, sex_female
"""

dummy_sex=pd.get_dummies(data["sex"],"sex")

print("En el titanic había ", dummy_sex["sex_female"].sum()," mujeres y ", dummy_sex["sex_male"].sum()," hombres")

"""Una vez que se crean las variables dummy, se deben añadir a las columnas del data,
lo más conveniente, ya que se tiene la variable categórica en variable cuantitativa, es eliminar
la variable categórica original (sex), y concatenar el dataframe original con el que se creó
al formarse las varibles dummies"""

data=data.drop(["sex"],1) # dataframe.drop ["nombre de fila o columna", 1 para columnas/0 para filas]
#recordar que data.función no guarda la función en el dataset original, por eso hay que reescribirlo

data=data.drop([data.columns[0]],1) #elimina la primer columna del dataframe, esto es porque
#el dataset tenía una columna de más que no servía de nada.

data=pd.concat([data,dummy_sex],1) #concatena los dos dataframes en las columnas, 0 si quisera añadir filas
# siempre hay que reescribir el dataframe.



