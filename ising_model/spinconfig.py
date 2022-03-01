"""def spin configuration class"""
class SpinConfig():

    def __init__(self, N=0):
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
        spinlist = []
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

        magnet = 0
        for eachspin in self.config:
            if eachspin == 1:
                magnet += 1
            elif eachspin == 0:
                magnet += -1
            else:
                print("Spin input error")

        return magnet