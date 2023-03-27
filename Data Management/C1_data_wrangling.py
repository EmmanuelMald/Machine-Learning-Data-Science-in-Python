# -*- coding: utf-8 -*-
"""
C1 Data wrangling o también data munging, visualización de datos, es el proceso de transformar y mapear
datos de un dataset raw en otro con la intención de hacerlo más apropiado y valioso para una variedad 
de propósitos posteriores, como el análisis.

Es una parte importante en un manejo de datos, todos los datos estarán repartidos en diferentes datasets
o en tablas, a veces no necesitamos todos los datos, algunas filas o algunas columnas para iniciar a 
trabajar.

Subdividir un datasets, se pueden crear dummies datasets, agregar datos para agrupar información
hacer cruces de datos, vamos a ver toma de muestras, muestreo aleatorio, conjunto de entrenamiento
y la parte de testing para comprobar que el modelo funciona correctamente.


"""
import pandas as pd

data=pd.read_csv(r"C:\Users\Emmanuel\OneDrive - Instituto Politecnico Nacional\ARREGLOS\CURSOS\DATA SCIENCE\python-ml-course-master\datasets\customer-churn-model\Customer Churn Model.txt",",")

# Crear un subconjunto de datos, extraer toda la columna de un dataset

account_length=data["Account Length"] #esto es un objeto de tipo Series

"""Objeto de tipo Series consiste en los valores de números de la columna seleccionada
    no usar sintaxis de un dataframe
"""

subset=data[["Account Length","Phone","Eve Charge","Day Calls"]]#Esto es un data frame

"""Si se selecciona una sola columna es un tipo Series, si son más de 1 columna, es dataframe
Para eliminar columnas:
Crear una lista de todos los nombres del conjunto de datos que no quiero
"""
all_cols=data.columns.values.tolist()

col_no_deseadas=["Account Length","Phone","Eve Charge","Day Calls"]
sublist=[x for x in all_cols if x not in col_no_deseadas] #ve uno por uno en la lista de columnas 
#y quédate con x, si x no está en col_no_deseadas
#ahora sí hacemos un dataframe con las columnas deseadas, que están guardadas en sublist

data_chida=data[sublist]
"""También se puede usar para las filas, si queremos obtener las primeras 20 filas:"""
print(data[0:20])

"""
data[0:8] == data[:8]
data[10:final de datos] == data[10:]

Esto limita conocer el número de fila donde tenemos los datos, por lo que usamos condicionales

EJ. Usuarios con "Total Mins">100

data1=data[data["Night Calls"]>100]

& and
| or
~ not
"""
data1=data[data["Night Calls"]>100] #Dame las filas que tengan valores mayores a 100 en la columna Night Calls
data2=data[data["State"]=="NY"]#Dame todas las filas de usuarios que vivan en Nueva York
data3=data[(data["State"]=="NY") & (data["Night Calls"]>100)]
#Dame todas las filas de usuarios que vivan en Nueva York y que tengan llamadas de noche mayores a 100
data4=data[(data["State"]=="NY") | (data["Night Calls"]>100)]
#Dame todas las filas de usuarios que vivan en Nueva York o que tengan llamadas de noche mayores a 100

"""
Resumiendo: 
    Sintaxis para obtener una cantidad de filas:
        data=data[3:] da las filas desde la fila 3 hasta la última
        data=data[data["Night Calls"]>100] me da las filas que cumplen con la condición dada

    Sintaxis para obtener una cantidad de columnas:
        data=data[[lista de columnas que se desean]]
        
    Qué pasa si quiero un número específico de columnas y filas a la vez?

"""

#Quiero minutos de día, de noche y longitud de la cuenta de los primeros 50 individuos

"condición de columnas: minutos de día, noche y longitud de la cuenta"
"condición de filas: de los primeros 50 individuos"

#SIEMPRE RECORDAR QUE LOS DATASETS FUNCIONAN COMO MATRICES CON UNA DIFERENCIA [filas][columnas] o [columnas][filas]
# COMO SIEMPRE, PARA NO COMPLICARSE [FILAS][COLUMNAS]

data5=data[["Day Mins","Night Mins","Account Length"]][:50]

data6=data[:50][["Day Mins","Night Mins","Account Length"]]

data7=data.iloc[0:10,3:6]

data8=data.iloc[:,[3,7]] #cuando las columnas no están ordenadas se pueden utilizar sus posiciones, al igual
#que a las filas

#SIEMPRE QUE ACCEDAMOS POR ÍNDICE USAR ILOC, CON LOC SE PUEDE USAR EL NOMBRE DE LAS COLUMNAS
data9=data.loc[[1,3],["Day Mins","Night Mins"]]


data10=data[data["Night Calls"]>100][["Day Mins"]] #Dame las filas en las que las llamadas nocturnas sean 
#mayores a 100, pero dame solo la columna "Day Mins"
data11=data[:50][data["Night Calls"]>100]

#Si se quiere agregar una columna con alguna operación con las columnas, se hace lo siguiente:
data["Total Mins"]=data["Day Mins"]+ data["Night Mins"] + data["Eve Mins"]
data["Total Calls"]=data["Day Calls"]+ data["Night Calls"] + data["Eve Calls"]
