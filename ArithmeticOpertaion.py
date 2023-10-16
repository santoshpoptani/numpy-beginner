
# Add
import numpy as np
import numpy as np

a = np.array([1, 2])
b = np.array([2, 3])

# c = a+b
c = np.add(a, b)

print(c)
print()
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = np.add(a, b)
print(c)

# subtract
a = np.array([1, 2])
b = np.array([3, 4])

c = np.subtract(b, a)

print("Subtract")
print(c)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

c = np.subtract(b, a)
print(c)

# multiply
a = np.array([1, 2])
b = np.array([3, 4])

c = np.multiply(a, b)
print("Multipky")
print(c)

# Divide
a = np.array([8, 6])
b = np.array([2, 3])

c = np.divide(a, b)
print("divide")
print(c)

# Boadcasting
# To perform arithmetic operations on arrays of different shapes, NumPy uses a technique called broadcasting.

# Rules for broadcasing

# Broadcasting only works with compatible arrays. NumPy compares a set of array dimensions from right to left.
#
# Every set of dimensions must be compatible with the arrays to be broadcastable.
# A set of dimension lengths is compatible when
#
# one of them has a length of 1 or
# they are equal

# array1 = shape(6, 7)
# array2 = shape(6, 1)

# Here, array1 and array2 are arrays with different dimensions (6,7) and (6,1) respectively.
#
# The dimension length 7 and 1 are compatible because one of them is 1.
#
# Similarly, 6 and 6 are compatible since they are the same.
#
# As both sets of dimensions are compatible, the arrays are broadcastable.

# For more example go t programing miz

p = np.array([1,2,4])
q = 4
ans = np.add(p,q)
print("broadcasting")
print(ans)
print()

q = np.array([[3],[1],[1]])
print(p.shape)
print(q.shape)
print(np.add(p,q))

p = np.array([[1,2,3],[1,3,5]])
q = np.array([[3,1,1],[1,2,2]])
print(p.shape)
print(q.shape)
print(np.add(p,q))