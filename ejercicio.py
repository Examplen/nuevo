
import pandas as pd
                                                                                                                 
# creacion de data frame 

"""data = {
    "colores":["amarillo","Rojo","morado","verde"],
    "contraste":[200,125,300,550]
}
myvar = pd.DataFrame(data)

print(myvar)"""


          
#localizar una fila 
"""data = {
    "colores":["amarillo","Rojo","morado","verde"],
    "contraste":[200,125,300,550]
}
myvar = pd.DataFrame(data)

print(myvar.loc[[ 1,2,3 ]])"""


#indices con nombre 

"""data = {
    "colores":[1, 2, 3, 4],
    "contraste":[200,125,300,550]
}
myvar = pd.DataFrame(data, index=["amarillo","Rojo","morado","verde"])

print(myvar)"""

#localizacion de indices 

"""data = {
    "colores":[1, 2, 3, 4],
    "contraste":[200,125,300,550]
}
myvar = pd.DataFrame(data, index=["amarillo","Rojo","morado","verde"])

print(myvar.loc[["morado","verde","amarillo"]])"""


# leer archivos csv


df = pd.read_csv('https://www.w3schools.com/python/pandas/data.csv.txt')

print(df.to_string())










































































































































































































































































