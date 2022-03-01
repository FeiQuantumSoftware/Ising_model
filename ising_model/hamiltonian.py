"""coupling Hamiltonian class def"""

class Hamiltonian():
    """Hamiltonian(J,miu)
    Input:
    --------
    (J: float; u=miu:float)

    """

    def __init__(self, J=-2, u=1.1):

        self.u = u
        self.J = J

    def energy(self, spinconfig):

        self.spinconfig = spinconfig
        E = 0
        """
        Energy from the external field:
        H_external = Sum over i of u * spin[i]
        """
        for eachspin in self.spinconfig:
            if eachspin == 1:
                E += self.u * 1
            elif eachspin == 0:
                E += self.u * (-1)
            else:
                print("Spin input error")

        """
        Energy from coupling the nearest neighbor spin:
        H_c = -J/k * spin[i] * spin[i+1]
        """
        newList = self.spinconfig[1:]
        newList.append(self.spinconfig[0])
        for spinx, spiny in zip(self.spinconfig, newList):
            if spinx == spiny:
                E += -self.J * 1
            elif spinx != spiny:
                E += -self.J * (-1)
            else:
                print("Type error spininput")

        return E

    def average(self, T=1, N=0):
        """Get average property of Ising model with N spins
        Input 
        -----------
        Temperatur--Float, N_spin_site---Integer
        eg. average(10,9)

        Return
        -----------
        E, m, C, ms   ---- Float
        """

        mySpin = SpinConfig(N)

        Zsum = 0
        E = 0
        EE = 0
        m = 0
        mm = 0

        for i in range(mySpin.iMax):
            spinConfig = mySpin.input_decimal(i)
            mi = mySpin.magnetization()
            Ei = self.energy(spinConfig)
            Zi = exp(-Ei/T)

            Zsum += Zi
            E += Zi * Ei
            EE += Zi * Ei*Ei
            m += Zi * mi
            mm += Zi * mi * mi

        """Normalize over Zsum"""
        E = E/Zsum
        EE = EE/Zsum
        m = m/Zsum
        mm = mm/Zsum
        # get capacity and magnetic susceptibility
        C = (EE - E**2)/(T*T)
        ms = (mm - m**2)/(T)

        return E, m, C, ms