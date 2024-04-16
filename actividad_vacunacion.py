import pandas as pd

vacunados=[110,500]
novacunados=[95,100]

datos={"Vacunados":vacunados,"No Vacunados": novacunados}

nombre_filas=["Infectados","No Infectados"]

tabla=pd.DataFrame(datos, index=nombre_filas)

total_personas=sum(tabla.sum())

print((tabla.loc["Infectados"]/tabla.sum()) *100)