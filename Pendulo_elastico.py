import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate



# Constantes
g = 9.8
lo = 0.1
k = 15
m = 0.1


# Intervalo de tiempo
dt = 0.001
t = np.arange (0.0,5, dt)

# Condiciones iniciales
r = 0.13                # state[0]  ; vector r
# si es negativo sale invertido, si es positivo sale en orden
v = 0.1                # state[1]  ; derivada del r , vector radial
th1 = 0.4*np.pi/180     # state[2]  ; theta
w1 = 0*np.pi/180        # state[3]  ; derivada del theta


#state = np.radians ([th1,w1]) # Transforma en radianes a los elementos de esta lista
state = [r,v,th1,w1]
#       [0,1, 2, 3]

# Funcion
def derivs (state,t):
    dydx = np.zeros_like(state)
    dydx[0] = state[1]     # derivada de la posicion
    dydx[1] = (state[0]*(state[3]**2)) + (g*np.cos(state[2])) - ((k*(state[0] - lo))/m) # EDO de la posicion
    dydx[2] = state[3] # Derivada del angulo 
    dydx[3] = (-2*(state[1]*state[3]/state[0])) - ((g*np.sin(state[2]))/state[0]) # segunda derivada del angulo
    return dydx



y = integrate.odeint(derivs , state ,t)


x1 = y[:,0]*np.sin(y[:,2])
y1 = -y[:,0]*np.cos(y[:,2])

# Energia 

# Energia cinetica
Ek = m*(y[:,1]**2 + (y[:,0]**2)*(y[:,3]**2))/2
# Energia potencial
Ep = -(m*g*y[:,0]*np.cos(y[:,2])) + (k*(y[:,0]-lo)**2)/2

# Energia total
E = Ek + Ep

plt.subplot(3,3,1)
plt.plot(t,y[:,2],'--c')
plt.xlabel('Tiempo (s)')
plt.ylabel(r'Angulo ($\theta$)')
plt.title('Angulo vs Tiempo')
plt.grid()


plt.subplot(3,3,2)
plt.plot(t,y[:,3],'-b')
plt.xlabel('Tiempo (s)')
plt.ylabel(r'Velocidad angular ($\omega$)')
plt.title('Velocidad angular vs Tiempo')
plt.grid()

plt.subplot(3,3,3)
plt.plot(t,y[:,0],'r')
plt.xlabel('Tiempo (s)')
plt.ylabel('Estiramiento')
plt.title('Estiramiento vs tiempo')
plt.grid()

plt.subplot(3,3,4)
plt.plot(t,y[:,1],'r')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.title('Velocidad vs Tiempo')
plt.grid()

plt.subplot(3,3,5)
plt.plot(t,y[:,0],'black')
plt.xlabel('Timpo (s)')
plt.ylabel('r')
plt.title('r vs Tiempo')
plt.grid()


plt.subplot(3,3,6)
plt.plot(y[:,2],y[:,3],'black')
plt.xlabel(r'Angulo ($\theta$)')
plt.ylabel(r'Velocidad angular ($\omega$)')
plt.title('Velocidad angular vs Angulo')
plt.grid()

plt.subplot(3,3,7)
plt.plot(x1,y1,'black')
plt.xlabel('Posicion x (m)')
plt.ylabel('Posicion y (m)')
plt.title('Grafica de posiciones')
plt.grid()

plt.subplot(3,3,8)
plt.plot(t,E,'black')
plt.xlabel('Tiempo (s)')
plt.ylabel('Energia (J)')
plt.title('Energia vs tiempo')
plt.grid()


plt.tight_layout()
