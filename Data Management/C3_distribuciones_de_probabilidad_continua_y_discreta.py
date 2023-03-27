# -*- coding: utf-8 -*-
"""
C3 Funciones de distribución de probabilidad (con variables aleatorias, obvio)
Sirve para hacer datasets con una cierta distribución de probabilidad


Todas las áreas bajo la curva de distribución de probabilidad tiene un área de 1 porque es la probabilidad total

Si se quiere generar números aleatoreos que sigan una distribución de probabilidad
(las fundamentales son la uniforme y la de Gauss)

La distribución uniforme (Es un rectángulo, es decir, todas las opciones tienen la misma probabilidad de ocurrir)
del rango (1,b), se tiene que la probabilidad es 1/(b-a) 
    
"""

# Distribución uniforme: Todos los valores tienen la misma probabilidad=1/rango

import numpy as np
import matplotlib.pyplot as plt
data=np.random.uniform(1,100,200) # np.random.uniform(limite inferior,superior,número de muestras)
plt.figure()#crea una gráfica
plt.hist(data,10) #mientras mayor sea el número de muestras, más se asemeja a una distribución uniforme
#recordar que para frecuencias relativas se usa density=True
plt.figure() #crea otra gráfica, si no se pone, las funciones las pone en una sola gráfica
plt.hist(data,10,density=1)
#para hacer un histograma de frecuencias relativas acumulativas:
plt.figure()
plt.hist(data,10,density=1,cumulative=True)



#Distribución normal o campana de Gauss
"""
    Ocurre en casi todas las cosas de la vida XD
"""
data1=np.random.normal(50,2,1000000) #np.randm.uniform(media, desviación estándar, número de datos)
data2=np.random.randn(1000000) #da una distribución con media igual a cero y desviación típica de 1
plt.figure()
x=range(0,1000000)
plt.plot(x,data2)
plt.figure()
plt.hist(data2,100) # con 100 clases, la distribución de probabilidad es una campana de Gauss bien y bonita
plt.figure()
plt.hist(data1,100,density=1)
plt.plot(x,sorted(data1)) #Si graficamos los valores en orden, nos podemos dar cuetna que primero crecen poquito
#luego avanza mucho y luego vuelve a crecer poco
#también se puede hacer la distribución normal con otra media y desviación como
media=10
desvest=3
data3=media+desvest*np.random.randn(1000000)
plt.figure()
plt.hist(data3)
data4=np.random.randn(2,100)#regresa dos conjuntos de datos de 100 datos cada uno con una distribución normal


