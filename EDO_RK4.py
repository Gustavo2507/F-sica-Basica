"""
Metodo de Runge-Kutta de 4to orden para un Sistema de Ecuaciones Diferenciales Ordinarias
"""

import numpy as np
import matplotlib.pyplot as plt




n = int(input('Ingrese el numero de intervalos: '))

x = np.zeros(n)
y = np.zeros(n)

x[0] = float(input('Ingrese la condicion inicial de x: ' ))
y[0] = float(input('Ingrese la condicion inicial de y: ' ))

to = float(input('Ingrese el tiempo inicial: '))
tf = float(input('Ingrese el tiempo final: '))



h = (tf - to)/n

# Sitema de funciones
def f(t,x,y):
    return(-4*y+np.cos(t))

def g(t,x,y):
    return(x)

t = np.arange(to,tf,h)

for i in np.arange(0,n-1):
    
    Ak1 = f(t[i], x[i],y[i])
    Bk1 = g(t[i], x[i],y[i])
    
    Ak2 = f(t[i] + h/2 ,x[i] + (h/2)*Ak1, y[i] + (h/2)*Bk1)
    Bk2 = g(t[i] + h/2 ,x[i] + (h/2)*Ak1, y[i] + (h/2)*Bk1)
    
    Ak3 = f(t[i] + h/2 ,x[i] + (h/2)*Ak2, y[i] + (h/2)*Bk2)
    Bk3 = g(t[i] + h/2 ,x[i] + (h/2)*Ak2, y[i] + (h/2)*Bk2)
    
    Ak4 = f(t[i] + h, x[i] + h*Ak3, y[i] + h*Bk3)
    Bk4 = g(t[i] + h, x[i] + h*Ak3, y[i] + h*Bk3)
    
    x[i+1] = x[i] + (h/6)*(Ak1 + 2*Ak2 + 2*Ak3 +Ak4)
    y[i+1] = y[i] + (h/6)*(Bk1 + 2*Bk2 + 2*Bk3 +Bk4)

    
 
plt.plot(x,y)
plt.title('Sistema de EDO')
plt.xlabel('Posicion')
plt.ylabel('f(t,x,y)')
plt.grid()

