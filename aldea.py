import pandas as pd

aldea1=[10000, 30]
aldea2=[100, 50]

datos={"Aldea 1":aldea1,"Aldea 2": aldea2}

nombre_filas=["Población", "Incremento"]

tabla=pd.DataFrame(datos, index=nombre_filas)

print(tabla)

print("Total de población")
print(tabla.loc["Población"] )

print("Incremento:")


print(tabla.loc["Incremento"])

#print(((tabla.loc["Población"] * (tabla.loc["Incremento"].sum())/100)) )

print((tabla.loc["Población"] + (tabla.loc["Población"] * (tabla.loc["Incremento"])/100)) )