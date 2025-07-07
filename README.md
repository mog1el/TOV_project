A project that simulates important relations in neutron stars by numerically solving the TOV equations and a "primitive" EoS $P = a(\rho - \rho_0)c^2$. The scripts model $M(R)$, $\rho(r)$, $R(\rho_0)$ and $M(\rho_0)$. The project was assigned by prof. Tomasz Bulik, who suggested it to me as a way to hone my programming skills.

---

Assumptions:

1. $a = 0.1$
2. $\rho_0 = 10^{17}$
3. $\rho_c = 2 * 10^{18}$
4. $c = 3 * 10^8$

All of them are listed at the top of each script, so feel free to change them if you deem it necessary (for example to improve accuracy).

---

In the simulations (except for $\rho(r)$ ) there is a constant `num` that determines the amount of small fragments that a space will be cut into. To get better (more acurate) results, you can increase the number. It, however, increases the number of calculations made by the computer, prolonging the time of completion.

In all of the simulations there is a step dr, set to 10m by default. Minimizing it will also increase the accuracy and prolong the time of computation.

For the code to work, some dependencies are necessary. To install them, run `pip install numpy matplotlib `. After doing this and downloading the python files, you are ready to go.

---

Here are the plots that one can get by running the scripts without changing their accuracy:

Total  star mass in respect to total radius:

![M(R)](https://github.com/user-attachments/assets/e9ae4b2a-d49f-4b80-aa29-f2f3aeec0cb0)

---

Density destribution in a neutron star, with horizontal lines marking the central and surface densities:

![rho(r)](https://github.com/user-attachments/assets/6288e847-b625-4154-af01-aee10628cd77)

---

Total radius in respect to $\rho_0$:

![R(Rho0)](https://github.com/user-attachments/assets/47b36017-ef2c-477e-9861-87a2bbd675ad)

---

Total star mass in respect to $\rho_0$:

![M(Rho0)](https://github.com/user-attachments/assets/bdd1cfc3-03f5-4996-90c3-eaad60b4ead0)

---
