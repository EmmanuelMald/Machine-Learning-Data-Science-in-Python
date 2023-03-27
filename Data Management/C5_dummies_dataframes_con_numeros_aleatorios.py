# -*- coding: utf-8 -*-
"""
C5 Dummy datasets

Se generan columnas dummies con la generación de números aleatorios
obvio  deben ser del mismo tamaño el número de columnas de números aleatorios

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.DataFrame({
    
    "A" : np.random.randn(1000),
    "B" : 1.5 + 2.5 * np.random.randn(1000), #todo esto es un diccionario
    "C" : np.random.uniform(0,100,1000),
    
    }) #convierte un diccionario a un dataframe

plt.figure()
plt.hist(data.iloc[:,0],density=1)
plt.title("Histograma de las frecuencias relativas de los números aleatorios generados con distribución normal")

plt.figure()
plt.hist(data.iloc[:,1],density=1)
plt.title("Histograma de las frecuencias relativas de los números aleatorios generados con distribución normal con media 1.5 y desviación estándar de 2.5")

plt.figure()
plt.hist(data.iloc[:,2],density=1)
plt.title("Histograma de las frecuencias relativas de los números aleatorios generados con distribución uniforme")

print(data.describe())

#También se pueden crear dataframes a partir de listas con variables categóricas, usaremos de ejemplo el de Churn Model
data1=pd.read_csv(r"C:\Users\LENOVO\OneDrive - Instituto Politecnico Nacional\ARREGLOS\CURSOS\DATA SCIENCE\python-ml-course-master\datasets\customer-churn-model\Customer Churn Model.txt")
column_names=data1.columns.values.tolist()

data3=pd.DataFrame({
    "Columns Names" : column_names,
    "A" : np.random.randn(len(column_names)),
    "B" : np.random.uniform(0,100,len(column_names))
    })