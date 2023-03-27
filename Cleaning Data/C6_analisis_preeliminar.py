# -*- coding: utf-8 -*-
"""
CLASE 6  DIMENSIONES Y ESTRUCTURAS

A veces queremos saber si los datos se leyeron correctamente, el tamaño y tipo de datos, 
visualización, obtener nombres de columnas, obtener desviaciones estándar, promedios, etc


"""
import pandas as pd

mainpath="C:\\Users\\LENOVO\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\CURSOS\\DATA SCIENCE\\python-ml-course-master\\datasets"
filename1="\\titanic\\titanic3.csv"
fullpath=mainpath+filename1
data=pd.read_csv(fullpath)
print(data.head())

"Dimensión, número de filas y columnas del dataset, se usa la siguiente función"

print(data.shape)
print(data.tail) #muestra las útlimas columnas del dataset
print(data.columns.values) #muestra los valores o nombres del dataframe

"Resumen de los datos estadísticos básicos de las variables numéricas:"
describe=data.describe()

"La siguiente función nos da el tipo de dato de cada columna del dataset"
tipo_datos=data.dtypes
print(tipo_datos) #objects son considerados strings

"Cómo sabemos si faltan valores y cómo podemos gestionarlos? en el titanic, hace falta la edad de 64 personas"
"o si faltan nombres de las personas"

#pd.isnull(se le puede pasar cualquier columna de datos, o todas las columnas)

"pd.isnull() regresa una matriz de nx2 de valores"

print(pd.isnull(data["body"])) #True significa que sí es un valor nulo
print(pd.notnull(data["body"])) #True significa que no es nulo
print(pd.isnull(data["body"]).values.ravel().sum()) #suma todos los valores nulos (con respuesta TRUE)

"""
CÓMO GENERAR LOS VALORES QUE FALTAN EN EL DATASET?
Los valores que faltan pueden ser por dos razones

    *Debido a la extracción de los datos:
        Cuando se extraen datos pueden borrarse algunos debido a incompatibilidades 


    *Recolección de los datos:
        Antes de guardarse los datos, algunos valores no pueden ser introducidos en la base de datos
        

#OPCIÓN 1: BORRAR LA FILA DE LOS DATOS QUE FALTAN, O BORRAR TODA LA COLUMNA

    función: data.dropna(axis=0 o 1, how="qué filas o columnas eliminar")

    data.dropna(axis=0 es filas 1 es columnas, how="qué filas tiene que borrar, all, any")
    all:todos
    any:cualquier elemento que contenga al menos 1 NaN

OPCIÓN 2: Imputación o cómputo de los valores faltantes, cambiar NaN por un 0, un string, dependiendo del contexto
    rellenar todo el valor faltante con 0
    
    data.fillna(0)
    data.fillna("desconocido")
    
    REEMPLAZAR DEPENDIENDO DE LA COLUMNA
    
    data["body"]=data["body"].fillna(0)
    data["homedestination"]=data["homedestination"].fillna("Desconocido")


fillna no sobreescribe el archivo original

Si no se conoce el valor real, se pone el promedio en NaN, y así no altera tanto los datos



"""
data1=data
data1=data1.dropna(0,"all") #Elimina todas las filas que tengan en todas sus columnas un valor nulo
data2=data
data2=data2.dropna(0,"any") #Elimina todas las filas que tengan en alguna columna un valor nulo
data3=data
data3=data3.dropna(1,"all")#Elimina todas las columnas que tengan en todas sus filas un valor nulo
data4=data
data4=data4.dropna(1,"any")#Elimina todas las columnas que tengan en alguna fila un valor nulo
data5=data
data5=data5.fillna(0)#Rellena todos los na del dataset con un 0
data6=data
data6=data6.fillna("desconocido")#Rellena todos los na del dataset con "desconocido"}
data7=data
data7["body"]=data7["body"].fillna(0)
data7["age"]=data7["age"].fillna(0)
data7["cabin"]=data7["cabin"].fillna("desconocido")
data7["embarked"]=data7["embarked"].fillna("desconocido")
data7["boat"]=data7["boat"].fillna("desconocido")
data7["fare"]=data7["fare"].fillna(0)
data7["home.dest"]=data7["home.dest"].fillna("desconocido")
data7.to_csv(mainpath+"\\titanic\\titanic3_limpio.csv")
print(pd.isnull(data7).values.ravel().sum())

"""
Si se quiere sustituir valores na por la media de todas las columnas, o por el valor que está
justo arriba o justo abajo de la columna

data[age]=data[age].fillna(method="ffill") pone el valor que se encuentra más cerca, ya sea el de adelante o
el de atrás

data[age]=data[age].fillna(data[age].mean()) pone el valor promedio
"""
