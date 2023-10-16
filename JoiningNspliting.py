import numpy as np
# concatenate()
# The concatenate() function allows you to join two or more arrays into a single array.
# The axis specifies the axis along which the funciton will join the arrays.
# If the axis is None, the function will flatten the arrays before joining

a = np.array([1, 2])
b = np.array([3, 4])

c = np.concatenate((a, b))
print(c)

a = np.array([
    [1, 2],
    [3, 4]
])
b = np.array([
    [5, 6],
    [7, 8]
])
print()
print(np.concatenate((a,b)))
print()
print(np.concatenate((a,b),axis=1))

# Satck
# The numpy.stack() function is used to join a sequence of arrays along a new axis.
# It takes a sequence of arrays and stacks them along a new axis, which can be specified using the axis parameter.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print()
print(np.stack((a,b)))
print()
print(np.stack((a,b),axis=1))

ac = np.array([
    [1, 2],
    [3, 4]
])
bc = np.array([
    [5, 6],
    [7, 8]
])

print()
print(np.stack((ac,bc)))

# vsatck
# In NumPy, numpy.vstack() is a function used to vertically stack
# (i.e., concatenate along the vertical axis) a sequence of input arrays. It's similar to numpy.concatenate()
# with axis=0, but it allows you to stack arrays of different shapes along their first dimensions.

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8, 9],
              [10, 11, 12]])

# Vertically stack the arrays
result = np.vstack((a, b))
print("Vsatck")
print(result)

# hsatck

# In NumPy, numpy.hstack() is a function used to horizontally stack
# (i.e., concatenate along the horizontal axis) a sequence of input arrays.
# It's similar to numpy.concatenate() with axis=1,
# but it allows you to stack arrays of different shapes along their second dimensions

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

# Horizontally stack the arrays
print("hsatck")
result = np.hstack((a, b))
print(result)

# split()

# The numpy.split() function is used to split
# an array into multiple sub-arrays along a specified axis. It returns a list of sub-arrays.
#  the size of the specified axis should be divisible by the number of sections
#  if you're using an integer for indices_or_sections.

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5, 6])

# Split the array into 3 equal parts
result = np.split(arr, 3)
print("split")
print(result)

# Create a 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12]])

# Split along axis 0 (rows) into 2 equal parts
result = np.split(arr, 3, axis=1)
res = np.split(arr, 2, axis=0)
print()
print(result)
print()
print(res)