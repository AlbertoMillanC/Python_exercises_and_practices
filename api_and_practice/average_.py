
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


datos = [[23, 36, 15, 18, 56, 45, 32, 10, 43, 55, 41, 63,12],["Enero", "Febrero", "Marzo","Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]]
#determinamos las produccion promedio de la empresa

df= pd.DataFrame(datos,index=list("PM"))
produccion=df.iloc [0,:]
print(df)
#calculamos el promedio de la produccion
promedio=np.mean(produccion)
print("la produccion promedio de la empresa fue", promedio)

#encontramos el mes de mayor produccion. 
dfT=df.transpose()
print(dfT)
maxi=dfT.max()

np.where(dfT ==maxi)
posicion_mayor=np.where(dfT ==maxi)
P=(posicion_mayor[0][1])

print("la produccion mayor fue",df[P][0], "y se dio en el mes",df[P][1])

#semestre de menor produccion. 
semestre1=produccion.head(6).sum()
print("la produccion del semestre 1 fue", semestre1)
semestre2=produccion.tail(6).sum()
print("la produccion del semestre 2 fue", semestre2)


# meses donde se produjeron mas de 50 aires
dfT[dfT["P"]>50]

#produccion meses impares
promedioI=dfT.iloc[[0,1,3,5,7,9,11],[0]].mean()
print("promedio meses impares",promedioI)

#meses donde la prpduccion supero el promedio

promedioP=dfT["P"].mean()
dfT[dfT["P"]>promedioP]

#grafico
plt.plot(dfT["P"],dfT["M"])