import numpy as np
import matplotlib.pyplot as plt

datos=np.loadtxt("Canal_ionico1.txt")
x=datos[:,0]
y=datos[:,1]

circulos=np.loadtxt("datos.txt")
x_circulo=circulos[:,0]
y_circulo=circulos[:,1]
r_circulo=circulos[:,2]

radio_mayor=0
pos=0
for i in range(len(r_circulo)):
	if (r_circulo[i]>radio_mayor):
		radio_mayor=r_circulo[i]
		pos=i


fig, ax=plt.subplots()
plt.scatter(x,y)
circle1=plt.Circle((x_circulo[pos],y_circulo[pos]),r_circulo[pos])
ax.add_artist(circle1)
ax.set_aspect('equal','datalim')
plt.title ("x=" + str (x_circulo[pos]) + " y =" + str (y_circulo[pos]) + " radio =" + str (r_circulo[pos]))
plt.savefig('ej1.jpg')
plt.close()

histograma=plt.hist(y,bins='auto')
plt.savefig('hist1.jpg')
plt.close()
