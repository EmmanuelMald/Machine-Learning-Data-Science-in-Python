# -*- coding: utf-8 -*-
"""
C7 Filtrado, transformación y operaciones útlies

"""
#recreando el dummie dataframe:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

social_status=["Rich","Poor","Middle Class"]
Gender=["Male","Female"]
n=500
l_social_status=[]
l_gender=[]
for i in range(n):
    l_social_status.append(np.random.choice(social_status))
    l_gender.append(np.random.choice(Gender))
l_age=np.ceil(30 +20*np.random.randn(n)) #crea una distribución normal con media 30 y desv est 20
l_income=10000 + 2000*np.random.randn(n)
l_weight=60+ 20*np.random.randn(n)
l_height=np.ceil(160 + 20*np.random.randn(n))
data=pd.DataFrame({
    "Social Status":l_social_status,
    "Gender":l_gender,
    "Age":l_age,
    "Weight":l_weight,
    "Height":l_height
    
    })

# agrupando los datos 

group_gender=data.groupby("Gender")

for i,j in group_gender:
    print(i) #da los grupos que se crearon de la variable categórica 

for i,j in group_gender:
    print(j)
    print(j) #da todas las filas que están dentro del grupo i

# si quiero hacer un dataframe con un grupo en específico que se creó en group_gender:
mujeres=group_gender.get_group("Female") #se crea un dataframe

#si quiero agrupar por más de una variable categórica

genero_clase=data.groupby(["Gender","Social Status"])#se crean tantos grupos como combinaciones posibles de las variables
mujeres_ricas=genero_clase.get_group(("Female","Rich"))#seleccionar un grupos en específico con dos variables, se debe poner como tupla

# Fitrar datos

"""Supongamos que queremos elegir elementos cuya suma de la columna de edad sea mayor a 2400"""
edad_mayor_a_valor=genero_clase["Age"].filter(lambda x: x.sum()>2400) #Elige a todos los elementos cuya suma de todas sus edades sea mayor
                                                    # a 2400, la operación devuelve la posición de los elementos que cumplen la condición

# Transformación de variables

"""Se define una función con lambda"""

zscore=lambda x: x-x.mean()/x.std() #se define una operación

#posteriormente se le aplica a los datos agrupados

zgroup=genero_clase.transform(zscore) #le aplica a todos los grupos la función zscore. También es un dataframe

plt.hist(zgroup["Age"]) #nos da la campana de gauss


#OPERACIONES DIVERSAS MÚY ÚTILES

a=data.loc[(data["Gender"]=="Female") & (data["Social Status"]=="Rich")]
b=data[(data["Gender"]=="Female") & (data["Social Status"]=="Rich")]
c=data[data.Gender == "Female"]