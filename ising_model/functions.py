"""Provide the primary functions."""


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format).

    Replace this function and doc string for your own project.

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from.

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution.
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())




#def spin configuration class

class SpinConfig():
    
    def __init__(self,N=0):
        """N = total spin_number"""
        self.N = N
        self.iMax = 2**self.N

    def input_decimal(self, decimal_Input):
        """initialize spin configuration when input is decimal.
        Input 
        -----------
        Enteger that decimal of a binary number '10110001' that represent a spin configuration
        Example: input_decimal(5)
                 return: [1,0,1]
        -----------
        Return: binary list in 0 and 1
        """        
        spinlist=[]
        for element in bin(decimal_Input)[2:]:
            spinlist.append(int(element))
            
        while len(spinlist) < self.N:
            spinlist = [0]+spinlist
            
        self.config = spinlist
        
        return self.config

    
    def input_p_m(self, p_m_Input):
        """Initialize spin configuration when input is decimal.
    
        Parameters 
        ----------
            p_m_Input: string
            
        Return
        -----------
            list (in 0 and 1)
        """
        self.p_m_Input = p_m_Input
        spinlist2=list()
        for element in self.p_m_Input:
            if element =="+":
                spinlist2.append(1)
            elif element == "-":
                spinlist2.append(0)
            else:
                pass
        
        self.config = spinlist2
        
        return spinlist2


    def magnetization(self):
        
        magnet = 0   
        for eachspin in self.config:
            if eachspin == 1:
                magnet += 1
            elif eachspin == 0:
                magnet += -1
            else:
                print("Spin input error")
                
        return magnet




#coupling Hamiltonian class def:
from math import exp

class Hamiltonian():
    """Hamiltonian(J,miu)
    Input:
    --------
    (J: float; u=miu:float)
    
    """
    
    def __init__(self,J=-2,u=1.1): 
        
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
                E+= self.u * 1
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
            if spinx==spiny:
                E += -self.J * 1
            elif spinx!=spiny:
                E += -self.J * (-1)
            else:
                print("Type error spininput")
                
        return E    
    
    
    

    def average(self,T=1,N=0):
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
            
            Zsum +=Zi 
            E += Zi * Ei
            EE += Zi * Ei*Ei
            m += Zi * mi
            mm += Zi * mi * mi
        
        """Normalize over Zsum"""
        E = E/Zsum
        EE = EE/Zsum
        m = m/Zsum
        mm = mm/Zsum
        #get capacity and magnetic susceptibility
        C = (EE - E**2)/(T*T)
        ms = (mm - m**2)/(T)
        
        return E, m, C, ms



#plots

import matplotlib.pyplot as plt
import numpy as np

Tlist=np.linspace(0.1,10,num=100)

Elist = list()
mlist = list()
Clist = list()
mslist = list()

for element in Tlist:
    E, m, C, ms = myH.average(element, 8)
    Elist.append(E) 
    mlist.append(m) 
    Clist.append(C) 
    mslist.append(ms) 
    
plt.figure(num = 0, dpi = 120)
plt.plot(Tlist, Elist,label="<E>")
plt.plot(Tlist, mlist,label="<m>")
plt.plot(Tlist, Clist,label="C")
plt.plot(Tlist, mslist,label="ms")
plt.legend()
plt.xlabel("T")




#test functions
H = Hamiltonian()
E, m , C, ms = H.average(1,2)

print(" E  = %12.8f" %E)
print(" M  = %12.8f" %m)
print(" HC = %12.8f" %C)
print(" MS = %12.8f" %ms)