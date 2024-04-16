import pandas as pd

grupoA=[50,40]
grupoB=[60,70]

datos={"GRUPO A":grupoA,"Grupo B": grupoB}

nombre_filas=["Sin recompensa","Con recompensa"]

tabla=pd.DataFrame(datos, index=nombre_filas)

print(tabla)

print(tabla.sum())

total_personas=sum(tabla.sum())

print("Total de personas es:", total_personas)

print(tabla.loc["Sin recompensa"])
total_sin_recompensa= sum(tabla.loc["Sin recompensa"])

print((total_sin_recompensa/total_personas)*100)

x=tabla.loc["Con recompensa", "GRUPO A"]

print((x/total_personas)*100)




