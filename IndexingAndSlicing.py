import numpy as np

# Accesing the array
a = np.array([
    [[1, 2], [3, 4], [5, 6]],
    [[5, 6], [7, 8], [9, 10]],
])

# in 0th row access 1st row acces 1st element
print(a[0, 1, 1])

# slicing

b = np.arange(0, 10)
print("b = ", b)
print("b[2:5] = ", b[2:5])
print("b[:] = ", b[:])
print("b[0:-1] = ", b[0:-1])
print('b[7:] = ', b[7:])
print('b[0:5:2]=', b[0:5:2])
print('b[::-1]=', b[::-1])
print("b[-1] = ", b[-1])

# Slicing multidimensionla array

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# below line selects 5,6 and 8,9 from above array
#  in below example we have selected 1st row to last row
#  at second contion we have slected item select 1st item to last item from each row
print(a[1:, 1:])
print()
# below only last row is selected and 1st to last elements are selected
print(a[-1, 1:])
print()
print(a[0:2,0:2])
print()
print(a[:,[0,2]])

arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
])

# [layer,row,elemet]
print(arr[1,:,1:])
print()
print(arr[0:2,0:2,0:1])

# Fancy indexinxg

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

indices = [0, 2]
selected_elements = arr[:, indices]
print(selected_elements)