import pandas as pd

grupoA=[50,40]
grupoB=[60,70]

datos={"GRUPO A":grupoA,"Grupo B": grupoB}

nombre_filas=["Sin recompensa","Con recompensa"]

tabla=pd.DataFrame(datos, index=nombre_filas)

print(tabla)

