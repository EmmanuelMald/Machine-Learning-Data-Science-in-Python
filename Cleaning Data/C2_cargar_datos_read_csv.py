# -*- coding: utf-8 -*-
"""
CLASE 2

CARGAR DATOS A TRAVÉS DE LA FUNCIÓN READ_CSV

df=dataframe
"""
import pandas as pd

mainpath="C:\\Users\\LENOVO\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\CURSOS\\DATA SCIENCE\\python-ml-course-master\\datasets"
filename="\\titanic\\titanic3.csv"
fullpath= mainpath + filename

data2=pd.read_csv(fullpath)

"Leer un dataset que sea un txt que esté separado por comas"

data3=pd.read_csv(mainpath + "\\customer-churn-model\\Customer Churn Model.txt")

print(data3.columns.values) #permite leer las columnas

"para cambiar el nombre de las columnas por otras que ya nos dan en otro archivo se hace lo siguiente"

name_cols=pd.read_csv(mainpath + "\\customer-churn-model\\Customer Churn Columns.csv")
nuevas_columnas=name_cols["Column_Names"].tolist() #Pasa una columna de un df a una lista
print(nuevas_columnas)
"Una vez hecho eso, data 4 tendrá como header la lista de las nuevas columnas"
data4=pd.read_csv(mainpath + "\\customer-churn-model\\Customer Churn Model.txt",header=None, names=nuevas_columnas)

