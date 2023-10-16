# sum Function

import  numpy as np
a = np.array([1,2,3])
print(a.sum())

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a.sum())
print()
print(a.sum(axis=0))
print(a.sum(axis=1))

arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
])
print()
print(arr.sum(axis=0))
print()
print(arr.sum(axis=1))
print()
print(arr.sum(axis=2))

# mean funciton
print("Mean Function")
print(a.mean())
print()
print(a.mean(axis=0))
print()
print(a.mean(axis=1))

# Varience
# variance of three numbers 1, 2, and 3:
# (1+2+3) / 3 = 2.0 -> calulate mean
# (1-2)^2 + (2-2)^2 + (3-2)^2 = 2
# 2 / 3 ~ 0.667

a = np.array([1, 2, 3])
result = np.var(a)
print(round(result,3))

# Devation
# Standard deviation is the square root of the variance

d = np.array([591, 239, 210, 207, 201, 182,
                      176, 176, 175, 170, 170, 169, 168, ])
result = np.std(d)
print(round(result,3))

# product of array

print()
print(np.prod(a))
print()
# Special case produ function becomes overflow so it returns 0 it will not raise he error
print(np.prod(np.arange(0,100)))

# amin()
# The amin() function returns the minimum element of an array
# or minimum element along an axis. Here’s the syntax of the amin() function:

print(np.amin(a))

# amax()

print(np.amax(a))


# all()
#  the all() function returns True if all numbers are nonzero or False if least one number is zero.
result = np.all(np.array([-1, 2, 3]))
print(result)
result = np.all(np.array([0, 2, 3]))
print(result)

# any()
# any() function returns True if any element in an array is non zero

result = np.any([0, 1, 2, 3])
print(result)