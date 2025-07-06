import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11
c = 3e8
M_sun = 1.989e30
a = 0.1
rhoc = 2e18

def Density(P, rho0):
    return P/(a * c ** 2) + rho0

def Pressure(rho, rho0):
    return a * (rho - rho0) * c ** 2

def tov(r, state, rho0):
    m, P = state[0], state[1]
    rho = Density(P, rho0)

    dmdr = 4.0 * np.pi * r**2 * rho
    
    dpdr = - (G * rho * m / r ** 2) * (1 + P/(rho * c ** 2)) * (1 + (4 * np.pi * P * r ** 3)/(m * c ** 2)) * (1 - (2 * G * m)/(r * c ** 2)) ** -1

    return [dmdr, dpdr]

def solve(rho0):
    dr = 10
    r = dr
    press = Pressure(rhoc, rho0)
    mass = (4.0/3.0) * np.pi * r**3 * rhoc
    state = [mass, press]
    while state[1] > 0:
        dmdr, dpdr = tov(r, state, rho0) 
        mass += dr * dmdr
        press += dr * dpdr
        state = [mass, press]
        r += dr
    return [r, mass]

num = 1000
rho0list = np.linspace(1e17, 1e18, num)
masy = []
n = 1

for rho0 in rho0list:
    radius, M = solve(rho0)
    masy.append(M/M_sun)
    print(f"{n}/{num}")
    n += 1

plt.plot(rho0list, masy)
plt.title('M(Rho0)')
plt.xlabel('Rho0 [kg/m^3]')
plt.ylabel('Masa w masach słońca')
plt.grid(True)
plt.show()