import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11
c = 299792458
M_sun = 1.9891e30
rho0 = 1e17
a = 0.1

def Density(P):
    return P/(a * c ** 2) + rho0

def Pressure(rho):
    return a * (rho - rho0) * c ** 2

def tov(r, state):
    m, P = state[0], state[1]
    rho = Density(P)

    dmdr = 4 * np.pi * r**2 * rho
    
    dpdr = - (G * rho * m / r ** 2) * (1 + P/(rho * c ** 2)) * (1 + (4 * np.pi * P * r ** 3)/(m * c ** 2)) * (1 - (2 * G * m)/(r * c ** 2)) ** -1

    return [dmdr, dpdr]

def solve(rhoc):
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
        r += dr
    return [r, mass]

num = 5000
rhoclist = np.linspace(rho0 + 1, rho0 * 100, num)
radiusy = []
masy = []
n = 1

for rhoc in rhoclist:
    radius, M = solve(rhoc)
    radiusy.append(radius/1000)
    masy.append(M/M_sun)
    print(f"{n}/{num}")
    n += 1

plt.plot(radiusy, masy)
plt.title('M(R)')
plt.xlabel('Promień [km]')
plt.ylabel('Masa w masach słońca')
plt.grid(True)
plt.show()