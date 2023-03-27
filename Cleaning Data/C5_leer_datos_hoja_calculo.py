# -*- coding: utf-8 -*-
"""
CLASE 5

Leer datos desde una hoja de datos, FICHEROS XLS y XLSX de EXCEL

También hay que añadir la pestaña que se va a leer
"""
import pandas as pd
mainpath="C:\\Users\\LENOVO\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\CURSOS\\DATA SCIENCE\\python-ml-course-master\\datasets"
filename1="\\titanic\\titanic3.xls"
filename2="\\titanic\\titanic3.xlsx"
fullpath1= mainpath + filename1
fullpath2=mainpath + filename2
# data=pd.read_excel(fullpath1,"nombre de la pestaña a leer")
titanic1=pd.read_excel(fullpath1,"titanic3")
titanic2=pd.read_excel(fullpath2,"titanic3")
