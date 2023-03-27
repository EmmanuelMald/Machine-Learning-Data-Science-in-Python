# -*- coding: utf-8 -*-
"""
CLASE 4
 Leer datos desde una URL externa
  
 Muchas veces los datos vienen en una página web en forma de fichero
 
 
"""
import pandas as pd
import urllib3 #navegar y acceder a información desde una url


medals_url="http://winterolympicsmedals.com/medals.csv"


"ABRIR UN ARCHIVO CSV DESDE UNA PÁGINA WEB CON PANDAS"

medals_data=pd.read_csv(medals_url)

"ABRIR UN ARCHIVO CSV DESDE UNA PÁGINA WEB CON urllib3"

http=urllib3.PoolManager()
r=http.request('GET',medals_url)
r.status
print(r.data) #da el archivo como un string, ya aprendimos como pasarlo a dataframe
lines=r.data.split("\n") #separa un solo renglón por espacio en la lista
cont=0
dic={}
for line in lines: 
    cont=+1
    if cont==1:
        head=line.split(","); #crea una lista con la cabecera del fichero
        for i in head:
            dic[head[i]]=[] #para cada columna se crea un espacio en el diccionario con una lista vacía
    col=line.split(",") #separa los datos de cada columna en un espacio de una lista
    for i in col: 
        dic[head[i]].append[col[i]] #añade los valores a cada columna
df=pd.DataFrame(dic) #convierte el diccionario en un dataframe
    
    