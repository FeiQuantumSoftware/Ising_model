"""def spin configuration class"""

from math import exp
import numpy as np


class SpinConfig():
    """Define a class of spin configuration with site number N.

    Parameters
    ----------
    N: integer , optional
        The total site number of a spin list.

    Returns
    -------
    SpinConfig : class
        A class of spin with site number N, with total possible spin configuration iMax = 2**N

    Examples
    --------
    >>> myspin = SpinConfig(4)
    >>> myspin.N
    4
    >>> myspin.iMax
    16
    """



    def __init__(self, N=0):
        self.N = N
        self.iMax = 2**self.N

    def input_decimal(self, decimal_Input):
        """Initialize spin configuration for decimal input.
        
        Parameters
        ----------
        decimal_Input : integar
            The decimal number of a binary spinlist. 

        Returns
        -------
        self.config : list
            A spin list represented in '0':spin down, and '1' : spin up.

        Examples
        --------
        >>> myspin = SpinConfig(8)
        >>> myspin.input_decimal(6)
        [0, 0, 0, 0, 0, 1, 1, 0]
        """
        spinlist = []
        for element in bin(decimal_Input)[2:]:
            spinlist.append(int(element))

        while len(spinlist) < self.N:
            spinlist = [0]+spinlist

        self.config = spinlist

        return self.config



    def input_p_m(self, p_m_Input):
        """Initialize spin configuration for decimal input.
        
        Parameters
        ----------
        p_m_Input: string
            A spin list represented in '+': spin up, and '-': spin down.

        Returns
        -------
        spinlist2 : list
            A spin list represented in '0':spin down, and '1' : spin up.

        Examples
        --------
        >>> myspin = SpinConfig()
        >>> myspin.input_p_m("++-+---+--+")
        [1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1]
        """
        self.p_m_Input = p_m_Input
        spinlist2 = list()
        for element in self.p_m_Input:
            if element == "+":
                spinlist2.append(1)
            elif element == "-":
                spinlist2.append(0)
            else:
                pass

        self.config = spinlist2

        return spinlist2



    def magnetization(self):
        """Initialize spin configuration for decimal input.
        
        Parameters
        ----------

        Returns
        -------

        Examples
        --------
        """
        magnet = 0
        for eachspin in self.config:
            if eachspin == 1:
                magnet += 1
            elif eachspin == 0:
                magnet += -1
            else:
                print("Spin input error")

        return magnet