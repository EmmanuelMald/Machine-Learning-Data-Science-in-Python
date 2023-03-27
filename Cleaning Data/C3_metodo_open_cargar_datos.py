# -*- coding: utf-8 -*-
"""
CLASE 3
 
pandas no es tan óptima para leer datasets con demasiados datos

Para eso se puede usar la función open de python, este lee el dataset línea a línea, permitiendo
recorrer el dataset mediante un for

open se abre en modo lectura por default, pero también se puede escribir, y escribir y leer a la vez
open ("fullpath", "r") -escritura
open ("fullpath", "w") -escritura
open ("fullpath", "rw")-lectura escritura

"""
mainpath="C:\\Users\\Emmanuel\\OneDrive - Instituto Politecnico Nacional\\CURSOS\\DATA SCIENCE\\python-ml-course-master\\datasets"
data=open(mainpath + "\\customer-churn-model\\Customer Churn Model.txt","r")

"""
data.strip() elimina espacios en blancos tanto al inicio como al final de la línea
data.split("delimitador")  divide toda la línea de texto dependiendo de un delimitador

Para saber el número de columnas y filas:

"""
import pandas as pd
dic={}
nfilas=0
for line in data:
    nfilas=nfilas+1
    if nfilas==1:
        print("hay ", len(line.split(",")), " columnas")   
        cols=line.split(",")#lista de nombres de cada columna
        for i in cols: #creamos un diccionario donde la llave es el nombre de cada columna
            dic[i]=[] #le adjuntamos a cada columna una lista vacía
print("hay ", nfilas-1," filas en el fichero")

"""para pasar un fichero a un dataframe, primero se necesita pasar del fichero a un diccionario
    y posteriormente convertir el diccionario en un dataframe. 
"""
data=open(mainpath + "\\customer-churn-model\\Customer Churn Model.txt","r")
nfilas=0
for line in data:
    nfilas=nfilas+1
    if nfilas>1:
        value=line.strip().split(",")
        for i in range(len(value)):
            dic[cols[i]].append(value[i])
            
"""Para convertir el diccionario a un dataframe, se utiliza lo siguiente:
    
    """
df=pd.DataFrame(dic) #Dato curioso:spyder muestra variables con inicial en mayúscula
print(df.head())
df1=pd.read_csv(mainpath + "\\customer-churn-model\\Customer Churn Model.txt")
print(df.columns)
print(df1.columns)# Ambos son iguales, el resultado es el mismo que si se abriera con pd.read_csv
    
    



