import numpy as np
# Array operation

# Resahp() frunction
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape it into a 2D array (3 rows, 2 columns)
reshaped_2darr = np.reshape(arr, (3, 2))
reshaped_3darr = np.reshape(arr, (1,3, 2))

print(reshaped_2darr)
print(reshaped_3darr)

# Transpose
# The numpy transpose() function reverses the axes of an array

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.transpose(a)
print("Transpose")
print(b)

# sort
a = np.array([
    [2, 3, 1],
    [5, 6, 4]
])

b = np.sort(a)
print("sorting")
print(b)
c = np.array([
    [5, 3, 4],
    [2, 6, 1]
])
d = np.sort(c,axis=0)
print(d)

# working with structured arrays
dtype = [('name', 'S10'),
         ('year_of_services', float),
         ('salary', float)]
employees = [
    ('Alice', 1.5, 12500),
    ('Bob', 1, 15500),
    ('Jane', 1, 11000)
]

payroll = np.array(employees, dtype=dtype)

result = np.sort(payroll,order=["year_of_services","salary"])
print(result)

# flatten
arr = np.array([[1, 2], [3, 4]])
# by default row major i.e 'C'
ans = arr.flatten()
print("Flatten")
print(ans)
# Column manjor
print(arr.flatten(order='F'))
# This stands for 'Any Order' and allows NumPy to choose the best order for the operation
print(arr.flatten(order='A'))
# his stands for 'Keep Order' and is a special option that tries
# to keep the array in the same order as the original array in memory
print(arr.flatten(order='K'))

# ravel
# The numpy.ravel() function returns a flattened view of the original array whenever possible.
a = np.array([[1, 2], [3, 4]])
b = np.ravel(a)
print("ravel")
print(b)


