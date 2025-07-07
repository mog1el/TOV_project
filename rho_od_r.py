import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11
c = 3e8
M_sun = 1.989e30
rho0 = 1e17
a = 0.1
rhoc = 2e18

def Density(P):
    return P/(a * c ** 2) + rho0

def Pressure(rho):
    return a * (rho - rho0) * c ** 2

def tov(r, state):
    m, P = state[0], state[1]
    rho = Density(P)

    dmdr = 4.0 * np.pi * r**2 * rho
    
    dpdr = - (G * rho * m / r ** 2) * (1 + P/(rho * c ** 2)) * (1 + (4 * np.pi * P * r ** 3)/(m * c ** 2)) * (1 - (2 * G * m)/(r * c ** 2)) ** -1

    return [dmdr, dpdr]

radiusy = []
densities = []
dr = 10
r = dr
press = Pressure(rhoc)
mass = (4.0/3.0) * np.pi * r**3 * rhoc
state = [mass, press]
while state[1] > 0:
    dmdr, dpdr = tov(r, state) 
    mass += dr * dmdr
    press += dr * dpdr
    state = [mass, press]
    radiusy.append(r/1000)
    densities.append(Density(press))
    print(f"Done for r = {r/1000} km")
    r += dr

plt.plot(radiusy, densities)
plt.axhline(y=rhoc, color='grey', linestyle='--')
plt.axhline(y=rho0, color='grey', linestyle='--')
plt.title('Rho(r)')
plt.xlabel('Radius [km]')
plt.ylabel('Density [kg/m^3]')
plt.grid(True)
plt.show()
