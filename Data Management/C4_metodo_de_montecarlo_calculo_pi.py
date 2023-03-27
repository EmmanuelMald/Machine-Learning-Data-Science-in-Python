# -*- coding: utf-8 -*-
"""
C4: Método de la simulación de Monte-Carlo para encontrar el valor de pi

Imagina que tengo un cuadrado de lado 2r, y dentro de él, tengo un círculo de radio r.
Cuál es la probabilidad de que si yo pongo un punto dentro del cuadrado, este vaya a caer también dentro del círculo?

Yo lo imagino así:
    Mi espacio muestral es el área total del cuadrado, es decir, 4r^2
    y el área donde tengo la probabilidad de que caiga en el círculo es de pi*r^2
    
    P(circulo)=pi r^2/(4 r^2)= pi/4
    
    pi=4*P(círculo)
    
    pero P(círculo)=número de veces que cae un puntito en el círculo entre la cantidad total de puntos que aventé
    
    como la probabilidad de que el punto caiga en cualquier punto es equiprobable, se puede usar una distribución
    uniforme para simular la probablidad de que caiga un puntito en cualquier punto.
    
    la ecuación de un disco en geometría analítica es:
        
        x^2+y^2 <= r^2
    
    Si el lado del cuadrado es de 1 unidad y yo genero valores aleatoreos entre 0 y 1, que es la longitud total del 
    cuadrado, y además le añado un contador que haga la desigualdad del disco, entonces estaré calculando
    cuántos puntos caen dentro del circulo y además tendré el valor total de lanzamientos, que será el número de datos
    que genere en cada una de las distribuciones uniformes

    
"""

import numpy as np
import matplotlib.pyplot as plt

def calculo_pi(n,nex): #n es el número de puntos a lanzar en cada experimento, nex es el número de veces que se repite el experimento
    pi_list=[] #lista que guardará cada valor de pi que salga en cada experimento
    sumpi=0 #suma todos los valores de pi que salen por cada experimento
    for j in range(nex):
        pc=0
        x=np.random.uniform(0,1,n).tolist() #genero números aleatorios de la componente x (toda la longitud del cuadrado)
        y=np.random.uniform(0,1,n).tolist() #genero números aleatorios de la componente y
        cont=0 #hago el contador para calcular la probabilidad de que el punto (x,y) caiga dentro del círculo
        for i in range(n):
            if (x[i]-0.5)**2+(y[i]-0.5)**2 <= 0.5**2: #si el punto cae dentro del disco, aumenta 1 al contador. Esta es la ecuación de
            #un círculo centrado en el punto(0.5,0.5) y de radio 0.5
                cont+=1
        pc=cont/n #probabilidad de que caiga el punto dentro del círculo
        valorpi=4*pc #calculo el valor de pi
        pi_list.append(valorpi)
        sumpi += valorpi
    pi_avg=sumpi/nex
    plt.plot(pi_list)
    plt.figure()
    plt.hist(pi_list,density=1) #notar que las frecuencia del valor de pi obedece a una gaussiana
    print("El valor de pi obtenido con", n, "muestras y",nex, "experimentos es de", pi_avg)
    return 


# OPTIMIZANDO EL CÓDIGO Y TIEMPO DE CÓMPUTO
"""
    Observar que si hago un espacio muestral desde x: [-1,1] hasta y:[-1,1], el disco queda centrado en el origen
    y es de radio 1, sin embargo, al elevar al cuadrado los números negativos desaparecen por lo que la lista que 
    necesitaría generar sería de 0 a 1 y estaría aumentando a 4 la rapidez de cálculo por simple simetría. La 
    probabilidad de que el punto caiga en el círculo calculándolo por relación de áreas queda igual.
"""

def pi_montecarlo(n,nex): #n es el número de puntos a lanzar en cada experimento, nex es el número de veces que se repite el experimento
    pi_list=[] #lista que guardará cada valor de pi que salga en cada experimento
    sumpi=0#suma todos los valores de pi que salen por cada experimento
    for j in range(nex):
        x=np.random.uniform(0,1,n).tolist() #genero números aleatorios de la componente x (toda la longitud del cuadrado)
        y=np.random.uniform(0,1,n).tolist() #genero números aleatorios de la componente y
        cont=0 #hago el contador para calcular la probabilidad de que el punto (x,y) caiga dentro del círculo
        for i in range(n):
            if (x[i])**2+(y[i])**2 <=1: #si el punto cae dentro del disco, aumenta 1 al contador
                cont+=1
        pc=cont/n #probabilidad de que caiga el punto dentro del círculo
        valorpi=4*pc #calculo el valor de pi
        pi_list.append(valorpi)
        sumpi += valorpi
    pi_avg=sumpi/nex
    plt.plot(pi_list)
    plt.figure()
    plt.hist(pi_list,density=1) #notar que las frecuencia del valor de pi obedece a una gaussiana
    print("El valor de pi obtenido con", n, "muestras y",nex, "experimentos es de", pi_avg)
    return 