# -*- coding: utf-8 -*-
"""
C7 Visualización básica de un data set

Representaciones gráficas del dataset

Plots y visualización de los datos

"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv(r"C:\Users\LENOVO\OneDrive - Instituto Politecnico Nacional\ARREGLOS\CURSOS\DATA SCIENCE\python-ml-course-master\datasets\customer-churn-model\Customer Churn Model.txt")
print("Hay ", pd.isnull(data).values.ravel().sum(), " datos faltantes en el dataset")
print("Los tipos de datos son: \n", data.dtypes)

#para guardar un plot en el directorio local se usa la función
# savefig("path_donde_guardas_la_imagen.jpeg") 
#puede guardarse en png, jpg, jpeg, etc

"Scatter Plot, gráfica de dispersión, se usa la función data.plot"

#data.plot.tipodegrafica("columna que se va a poner en x","columna que se pone en y")

data.plot.scatter("Day Mins", "Day Charge")
data.plot.scatter("Night Mins", "Night Charge")

"""¿Qué pasa si quiero juntar más variables?
    
    La función plt.subplots regresa dos parámetros, el nombre del cuadro donde se guardará la matríz de las gráficas
    y una matriz de ixj que serán las posiciones de las subgráficas que se tengan
        
"""


figure,axs=plt.subplots(2,2, sharey=True, sharex=True)#crea una matriz de figuras de 2x2
data.plot.scatter("Day Mins","Day Charge",ax=axs[0,0])
data.plot.scatter("Night Mins","Night Charge",ax=axs[0,1])
data.plot.scatter("Day Mins","Night Charge",ax=axs[1,0])
data.plot.scatter("Night Mins","Day Charge",ax=axs[1,1])

"""Histogramas de frecuencias

    Cómo se distribuye una variable numérica, se puede saber el tipo de distribución que tiene nuestros
    datos
    
    
     """

fig2=plt.figure()
plt.hist(data["Day Calls"],10)
plt.xlabel("Número de llamadas al día")
plt.ylabel("Frecuencia")
plt.title("Histograma del número de llamadas al día")

fig3=plt.figure()
plt.hist(data["Day Calls"],20)
plt.xlabel("Número de llamadas al día")
plt.ylabel("Frecuencia")

plt.figure()
plt.hist(data["Day Calls"],[0,30,60,90,120,150,180])
plt.xlabel("Número de llamadas al día")
plt.ylabel("Frecuencia")


"""Regla de Esturges para saber el número de clases en un histograma:
    num_clases= 1 + np.log2(3333)
    np.ceil(valor numérico) redondea hacia arriba
    """
num_clases=np.ceil(1+np.log2(data.shape[0])) #regresa un valor flotante, pero para usarlo en el histograma
#se necesita pasar la variable a entera

plt.figure()
plt.hist(data["Day Calls"],int(num_clases))
# color="color" es el color de las clases
# ec="color" es el color de las esquinas, va dentro de plt.hist
plt.xlabel("Número de llamadas al día")
plt.ylabel("Frecuencia")

"""
    Diagrama de caja y bigotes (o BOXPLOT)
    se usa la función
    
    plt.boxplot(data["nombre de la columna"]). 
    
    Cómo se interpreta este diagrama?
    
    La caja indica la importancia de donde está la gran mayoría de datos, 
    la caja empieza en el 25 % y termina en el 75 %, la línea roja es la mediana (valor de enmedio)
    Rango intercuartílico, cuartil 75 y cuartil 25, es la longitud de la caja
    los bigotes (líneas negras horizontales) siempre se colocan a 1.5 veces el rango intercuartílico
    los valores que están arriba de los bigotes, se colocan como outlayers (datos fuera de lo común)
    
    Nos permiten saber dónde se centran los valores, y también nos dicen los valores fuera de lugar
    
"""

plt.figure()
plt.boxplot(data["Day Calls"])
plt.ylabel("Número de llamadas diarias")
