"""coupling Hamiltonian class def"""
from math import exp
import numpy as np
from .spinconfig import SpinConfig


class Hamiltonian():
    """Create a class of Hamiltonian of 2-d Ising model.

    Parameters
    ----------
    J: float, optional
        Coupling parameter, default J=-2 .
    u: float, optional
        External field strength, default u=1.1 .

    Returns
    -------
    Hamiltonian: class
        A Hamiltonian of a Ising model with J: coupling strength, u: external field factor.

    Examples
    --------
    >>>ham = Hamiltonian(-2,1.1)
    >>>ham. J
    -2
    """

    def __init__(self, J=-2, u=1.1):
        self.u = u
        self.J = J

    def energy(self, spinlist):
        """Calculate the energy of a given spinconfiguration.

        Parameters
        ----------
        spinlist : list
            Spin configuration represented in '1': spin up, '0': spin down.

        Returns
        -------
        energy : float
            Total energy out from both the external filed and coupling from neighbor spins.

        Examples
        --------
        >>>ham = Hamiltonian(-2,1.1)
        >>>ham. energy([0,1,0,1,1])
        -4.9
        """
        self.spinlist = spinlist

        E = 0
        # Energy from the external field:
        # H_external = Sum over i of u * spin[i]
        for eachspin in self.spinlist:
            if eachspin == 1:
                E += self.u * 1
            elif eachspin == 0:
                E += self.u * (-1)
            else:
                print("Spin input error")

        # Energy from coupling the nearest neighbor spin:
        # H_c = -J/k * spin[i] * spin[i+1]

        newList = self.spinlist[1:]
        newList.append(self.spinlist[0])
        for spinx, spiny in zip(self.spinlistspinlist, newList):
            if spinx == spiny:
                E += -self.J * 1
            elif spinx != spiny:
                E += -self.J * (-1)
            else:
                print("Type error spininput")

        return E

    def average(self, T=1, N=0):
        """Calculate the oberservables of a given spin list with N sites.

        Parameters
        ----------
        T : float, optional
            Temperature of the system.
        N : interger, optional
            The site number of a spin list. 

        Returns
        -------
        E, m, C, ms : set
            Average energy, average magnetism, heat capacibility, magnetic susceptbility.

        Examples
        --------
        >>>ham = Hamiltonian(-2,1.1)
        >>>ham. average(10, 4)
        (-1.894905381126034,
         -0.29386784002835087,
         0.17850826588133842,
         0.26682385808137565)
        """
        mySpin = SpinConfig(N)

        Zsum = 0
        E = 0
        EE = 0
        m = 0
        mm = 0

        for i in range(mySpin.iMax):
            myspinlist = mySpin.input_decimal(i)
            mi = mySpin.magnetization()
            Ei = self.energy(myspinlist)
            Zi = exp(-Ei/T)

            Zsum += Zi
            E += Zi * Ei
            EE += Zi * Ei*Ei
            m += Zi * mi
            mm += Zi * mi * mi

        # get average energy
        E = E/Zsum
        EE = EE/Zsum
        # get average magnetism
        m = m/Zsum
        mm = mm/Zsum
        # get capacity
        C = (EE - E**2)/(T*T)
        # get magnetic susceptibility
        ms = (mm - m**2)/(T)

        return E, m, C, ms
