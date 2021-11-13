from vector import Vector

v1 = Vector([ [0.0], [1.0], [2.0]])
print(v1.values)
print("Operation with real number:")
print("add:\n", v1 + 2)
print("sub:\n", v1 - 2)
print("mul:\n", v1 * 2)
print("div:\n", v1 / 2)
v2 = Vector([ [1.0], [2.0], [3.0]])
print("Operation with vector:")
print("add:\n", v1 + v2)
print("sub:\n", v1 - v2)
print("mul:\n", v1 * v2)
print("div:\n", v1 / v2)

print(v1.dot(v2))

print(v1.shape)
v1.T()
print(v1.shape)
