import matplotlib.pyplot as plt
import numpy
from mpl_toolkits.mplot3d import Axes3D
from numpy import sin, linspace
LIMITE=21
A=[ n**2 if n%2 == 0 else n**3 for n in range(0,LIMITE)]
print(A)
pares=[x for x in range(0,len(A)) if x%2 == 0]
print(pares)




fig, ax = plt.subplots(facecolor='w', edgecolor='k')
ax.plot (A, marker="o", color="b", linestyle='solid')
ax.grid(True)
ax.set_xlabel('X') #Etiqueta del eje x
ax.set_xlabel('Y') #Etiqueta del eje y
ax.grid(True)
ax.legend(["numeros pares e inpares"])
plt.title('Puntos')
plt.show()
fig.savefig("pareseimpares.png") #Guardando la gráfica

par = pares
fig, ax = plt.subplots(facecolor='w', edgecolor='k')
ax.plot (par, marker="o", color="r", linestyle='solid')

ax.grid(True)
ax.set_xlabel('X') #Etiqueta del eje x
ax.set_xlabel('Y') #Etiqueta del eje y
ax.grid(True)
ax.legend(["numeros pares e inpares"])
plt.title('Puntos')
plt.show()
fig.savefig("par.png") #Guardando la gráfica


lista=["juna","jose","dario","damian"]
print("lista original:")
print(lista)
nuevalista=[k.upper() for k in lista]
print("lista nueva:")
print(nuevalista)

movie= [("Citizen Kane", 1941), ("Spirited Away", 2001), ("It's a Wonderfil Life", 1946), ("Gattaca", 1997),("No Country for Old Men", 2007),("Rear Window", 1954), ("The Lord off the Rings: The Fellowship of the Ring", 2001), ("Groundhog Day", 1993),("Close Encounters of the Kind", 1977), ("The Royal Tenenbaums", 2001), ("The Aviator", 2004), ("Raiders of the Lost Ark", 1981), ("Baywatch", 2017), ("The House Bunny", 2008), ("Thor", 2011), ("Avatar", 2009), ("Titanic", 1997), ("Big Momma's House", 2008), ("Little Man", 2006), ("Scary Movie 5", 2013), ("The Call", 2013), ("Harry Potter y la piedra filosofal", 2001), ("Volcano", 1997), ("Furious 7",2915),("The Fate of the Fourious", 2017), ("Deadpool", 2016), ("Spider-Man 3", 2007), ("Yo, Robot", 2884), ("I am Legend",2887)]

print(movie)
print(len(movie))
#nuevalista2=[(x, y) for x in movie in range(0,29) for y in movie if y.star ]
#print(nuevalista2)
