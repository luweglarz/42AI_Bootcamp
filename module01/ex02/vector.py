import numpy as np

class Vector:
    def __init__(self, *args):
        if isinstance(args[0], int):
            self.values = np.arange(float(args[0]))
            self.shape = (args[0], 1)
        elif isinstance(args[0], list) and len(args) == 1:
            self.values = np.array(args[0])
            self.shape = np.shape(self.values)
        elif isinstance(args, tuple) and len(args) > 1:
            self.values = np.array(args)
            self.shape = (1, len(self.values))

    def __add__(self, rarg):
        if isinstance(rarg, Vector) and self.shape == rarg.shape:
            return self.values + rarg.values
        elif isinstance(rarg, int):
            return self.values + rarg
        else:
            print("Wrong operation")
    def __radd__(self, larg): #__radd__(nb, self)
            return self.__add__(larg , self)

    def __sub__(self, rarg):
        if isinstance(rarg, Vector) and self.shape == rarg.shape:
            return self.values - rarg.values
        elif isinstance(rarg, int):
            return self.values - rarg
        else:
            print("Wrong operation")
    def __rsub__(self, larg):#__rsub__(nb, self)
        return self.__sub__(larg , self)

    def __mul__(self, rarg):
        if isinstance(rarg, Vector) and self.shape == rarg.shape:
            return self.values * rarg.values
        elif isinstance(rarg, int):
            return self.values * rarg
        else:
            print("Wrong operation")
    def __rmul__(self, larg): #__rmul__(nb, self)
        return self.__mul__(larg , self)

    def __truediv__(self, rarg):
        if isinstance(rarg, Vector) and self.shape == rarg.shape:
            return self.values / rarg.values
        elif isinstance(rarg, int):
            return self.values / rarg
        else:
            print("Wrong operation")
    def __rtruediv__(self, larg):#__rtruediv__(nb, self)
        return self.__truediv__(larg , self)  

    def dot(self, vector):
        if isinstance(vector, Vector) and self.shape == vector.shape:
            return np.dot(np.squeeze(np.asarray(self.values)), np.squeeze(np.asarray(vector.values)))
        else:
            print("Wrong operation")

    def T(self):
        self.shape = np.transpose(self.values).shape