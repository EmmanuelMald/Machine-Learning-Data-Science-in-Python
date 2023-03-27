"""
CLASE 1. QUÉ ES UN DATASET?
Un dataset es un fichero en donde se tienen los datos, 
es un fichero que se carga dentro de un programa (R o Python)

Está organizado en filas y columnas, se puede pensar como un diccionario que 
contiene una serie de objetos estructurados

Se tiene una serie de etiquetas para filas y columnas.

Se trabaja con archivos que son csv (coma separated value), excel, txt y demás.

Cómo se cargan los datos?

Todos los archivos se separan por un caracter especial llamado "separador", usualmente es la coma

Siempre pedir el delimitador del dataset

pandas es la librería que se usa para abrir e importar datasets.

"""
import pandas as pd

"Se puede abrir de varias maneras un csv, la primera es poner una r antes de la dirección completa del archivo"

data=pd.read_csv(r"C:\Users\LENOVO\OneDrive - Instituto Politecnico Nacional\ARREGLOS\CURSOS\DATA SCIENCE\python-ml-course-master\datasets\titanic\titanic3.csv")


"La segunda es poner doble diagonal invertida"

data1=pd.read_csv("C:\\Users\\LENOVO\\OneDrive - Instituto Politecnico Nacional\\ARREGLOS\\CURSOS\\DATA SCIENCE\\python-ml-course-master\\datasets\\titanic\\titanic3.csv")

print(data.head()) #"muestra las primeras 5 filas"

# Qué pasa si el separador no es una coma, es otro caracter? a continuación se muestran los parámetros de pd.read_csv()

"""
pd.read_csv(filepath, separador, dtype, header, names, skiprows,index_col, skip_blank_lines)
            
            filepath=la ruta del dataset
            
            separador= puede ser cualquier caracter, se escribe entre comillas, acepta REGULAR EXPRESSIONS
            
            dtype= por default es None, pero pueden formatearse, variable de tipo fecha viene como strings y se necesita convertir a variable tipo fecha
                   columnas se clasifican en {"a o nombre de cabecera"=np.float64, "b"=np.int32}
            
            header=None, el valor del argumento header puede ser un entero o toda una lista
                   header usa la primera fila como cabecera del dataframe, header=0, primera fila
            
            names=indica el nombre de las columnas, crea una lista donde pones el nombre de las columnas{"ingresos", "pagos"}
            
            skiprows=None (default), pero permite no leer columnas, si ponemos skiprows=12, empezará a leer desde la columna 13
            
            index_col=None, permite ponerle nombre a las filas de un dataset
            
            skip_blank_lines=True or False (if True: las líneas en blanco serán saltadas)

            na_filter=True or False (True elimina la fila que tenga algun valor nulo)
            
"""

