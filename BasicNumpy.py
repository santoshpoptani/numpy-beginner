import numpy as np
a = np.array([1,2,3,4,5])

print(type(a))
# property ndim gives the dimension of array
print(a.ndim)
# dtype property gives the data type of elements in array
print(a.dtype)
print(a)

# this way we can change the datatype of elements in array
b = np.array([1,2,3], dtype=np.float64)
print(b.dtype)
print(b)

# 2-D Arrays

c = np.array([
    [1,3,4],
    [1,2,6]
])
print(c.ndim)
print(c)

# 3-D Array

d = np.array([
    [
        [1,23,4,5],
        [7,8,9,5]
    ],
    [
        [1,2,3,5],
        [2,3,4,1]
    ]
])
print(d.ndim)
print(d)

# Gettings Shapes of array
# Shapes are returned in forms of tuple
print(a.shape)
print(c.shape)
print(d.shape)

# arrange function creats new array with start, stop , step parameter

a = np.arange(1,10,2,dtype=np.float64)
print(a)



