import re
import numpy as np #Libreria importada para usar sus funciones sobre el análisis de datos.

#Librerias para generar el csv
import pandas as pd 
import os
import matplotlib.pyplot as plt

#Se ingresa el texto quemado en código con 48 palabras.
print("------------------------------------------------------------")
print("El texto es:")
print()
text = "excelente servicio, correo1@gmail.com, muy malo el servicio, correo2@uniminuto.com, correo3@hotmail.com,  bacano ese producto, bastante bueno el producto, correo4@udistrital.com, el servicio es increible, esta chimba la propuesta de servicio, correo5@hotmail.com, correo6@uniminuto.com, esta genial el producto, muy melo el servicio, correo7@gmail.com, malisimo el serivicio, bueno el producto, bueno el servicio, correo8@hotmail.com"
text2= text
print(text)
print("------------------------------------------------------------")

patron = re.compile(r'\W+')
palabras = patron.split(text)
palabrasBuenas = 0

#Se cuentan todas las palabras que son sinonimo de bueno
for i in palabras:

    if i == "excelente":
        palabrasBuenas = palabrasBuenas+1

    else:

        if i == "bacano":

            palabrasBuenas = palabrasBuenas+1

        else:

            if i == "bueno":

                palabrasBuenas = palabrasBuenas+1

            else:

                if i == "increible":

                    palabrasBuenas = palabrasBuenas+1

                else:

                    if i == "chimba":

                        palabrasBuenas = palabrasBuenas+1

                    else:

                        if i == "genial":

                            palabrasBuenas = palabrasBuenas+1

                        else:

                            if i == "melo":

                                palabrasBuenas = palabrasBuenas+1

print("Comentarios buenos:")
print()
cantidadComentarios = []

for x in range(palabrasBuenas): #Se imprime la palabra bueno la cantidad de veces del contador

    cantidadComentarios.append("bueno")    
    print("bueno")

conversion = str(palabrasBuenas) #Se transforma el valor en str para poder concatenar 
print()
print("Cantidad comentarios buenos: "+conversion)
print("------------------------------------------------------------")

print("Texto cambiando cada palabra sinónima de bueno por la palabra “bueno”.")
print()

#Se busca cada palabra, se remplazada en el texto y se sobreesribe en la misma variable
excelente = re.compile(r'\bexcelente\b')
text = excelente.sub("bueno", text)

bacano = re.compile(r'\bbacano\b')
text = bacano.sub("bueno", text)

increible = re.compile(r'\bincreible\b')
text = increible.sub("bueno", text)

chimba = re.compile(r'\bchimba\b')
text = chimba.sub("bueno", text)

genial = re.compile(r'\bgenial\b')
text = genial.sub("bueno", text)

melo = re.compile(r'\bmelo\b')
text = melo.sub("bueno", text)

print(text)
print("------------------------------------------------------------")

print("Todos los correos electrónicos encontrados en el texto.")
print()
mail = re.compile(r' \b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b', re.X)
correos=mail.findall(text)
print(correos)
print("------------------------------------------------------------")
print("Bonus")
print()

try:

    os.chdir(r'D:\Universidad\10 Semestre\Mineria de datos\Prueba Script') #####Ruta de guardado del csv

    vector = [{'Texto original':text2,'Comentarios buenos':cantidadComentarios, 'Cantidad comentarios buenos':palabrasBuenas,'Texto cambiando cada palabra sinónima de bueno':text,'Todos los correos electrónicos encontrados en el texto':correos}]

    convertirExcel = pd.DataFrame(vector)

    convertirExcel.to_excel('Expresion_regular.xlsx',index=False)

    print("Documento csv generado correctamente")

except:
    
    print("Error ! Verifique la ruta de guardado del archivo csv")
