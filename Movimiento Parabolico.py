"""
Movimiento parabolico
"""

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


# Definicion de variables

ans = int(input('El angulo que ingresara esta en grados, [1] Si ; [2] No -->'))

if(ans == 1):
    ang  = float(input('Ingrese el angulo en grados: '))
    angR = (ang*np.pi)/180
elif (ans == 2):
    angR = float(input('Ingrese el angulo en radianes: '))
else:
    print('Codigo incorrecto')
    exit()


vo = float(input('Ingrese el valor de la velocidad inicial: '))
g  = float(input('Ingrese el valor de la gravedad: '))

Vx = vo*np.cos(angR)
Vy = vo*np.sin(angR)

Tt = (2*Vy)/(g)
print('El tiempo total de vuelo es: ', Tt)

Dx = Vx*Tt
print('La distancia en el eje x es: ',Dx)

Hy = ((Vy)**2)/(2*g)
print('La altura maxima alcanzada es: ',Hy)

# Datos para el grafico

X = np.arange(0,Dx, 0.001)

# Trayectoria
y = np.tan(angR)*X-(g*X**2)/(2*(Vx)**2)

plt.plot(X,y)
plt.axhline(y=0, xmin=0, xmax=Dx, color = 'black')
plt.axvline(x=0, ymin=0, ymax=Hy, color = 'black')
plt.scatter(0, 0, color = 'red', linewidths= 3)
plt.xlabel('Distancia de disparo')
plt.ylabel('Altura del disparo')
plt.title('Movimiento parabolico')
plt.grid()






 

