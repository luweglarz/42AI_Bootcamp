import numpy as np
from random import seed
from random import randint

class NumPyCreator:
    def from_list(self, lst):
        return np.array(lst)
    def from_tuple(self, tpl):
        return np.array(tpl)
    def from_iterable(self, itr):
        return np.fromiter(itr, int)
    def from_shape(self, shape, value=0):
        array = np.zeros(shape)
        i = 0
        if value != 0:
            for j in array:
                array[i] = value
                i += 1
        return array
    def random(self,shape):
        return np.random.rand(shape[0], shape[1])
    def identity(self, n):
        return np.identity(n)

npc = NumPyCreator()

lst = [[1,2,3],[6,3,4]]
tpl = (('a', 'b', 'c'))
shape = (3,5)

print(npc.from_list(lst))
print(npc.from_tuple(tpl))
print(npc.from_iterable(range(5)))
print(npc.from_shape(shape))
print(npc.random(shape))
print(npc.identity(4))