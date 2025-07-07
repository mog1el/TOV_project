A project that simulates important relations in neutron stars by numerically solving the TOV equations and a "primitive" EoS $P = a(\rho - \rho_0)c^2$. The scripts model $M(R)$, $\rho(r)$, $R(\rho_0)$ and $M(\rho_0)$. The project was assigned by prof. Tomasz Bulik, who suggested it to me as a way to hone my programming skills.

---

Assumptions:

1. $a = 0.1$
2. $\rho_0 = 1e17$
3. $\rho_c = 2e18$

All of them are listed at the top of each script, so feel free to change them if you deem it necessary.

---

In the simulations (except for $\rho(r)$, there is a constant `num` that determines the amount of small fragments that a space will be cut into. To get better (more acurate) results, you can increase the number. It, however, increases the number of calculations made by the computer, prolonging the time of completion.

In all of the simulations there is a step dr, set to 10m by default. Minimizing it will also increase the accuracy and prolong the time of computation.

For the code to work, some dependencies are necessary. To install them, run `pip install numpy matplotlib `. After doing this and downloading the python files, you are ready to go.

---

Here are the plots that one can get by running the scripts without changing their accuracy:

Total  star mass in respect to total radius:
![M(R)](https://github.com/user-attachments/assets/a748ba31-60aa-44a4-9345-03dd55b30c88)

Density destribution in a neutron star, with horizontal lines marking the central and surface densities:
![rho(r)](https://github.com/user-attachments/assets/44e1ae9b-ac98-4279-bd56-4a6c30b89d6b)

Total radius in respect to $\rho_0$
![R(Rho0)](https://github.com/user-attachments/assets/abd1a68d-828f-4f64-8c25-42591ccc9975)

Total star mass in respect to $\rho_0$:
![M(Rho0)](https://github.com/user-attachments/assets/65e8f961-13b7-42ad-af7f-3c2919b3dbf4)
