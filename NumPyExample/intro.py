import numpy as np

print(np.__version__)
a = np.array(1)
b = np.array([1, 2, 2, 3, 4])
c = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
d = np.array([[[1, 2, 3, 4], [1, 2, 3, 4]], [[1, 2, 3, 4], [1, 2, 3, 4]]])
print(a)
print(type(a))
print(a.ndim)
print(b)
print(type(b))
print(b.ndim)
print(c)
print(type(c))
print(c.ndim)
print(d)
print(type(d))
print(d.ndim)

e = np.array([1, 2, 3, 4], ndmin=5)
print(e)

print("##################################################")

x = np.array([1, 2, 3, 4, 5, 6])
print(x[2])

y = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(y[1, 2])

z = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(z[1, 0, 2])

print("##################################################")
arr1 = np.array([[1, 2, 3, 4, 5], [5, 6, 7, 8, 9]])
print(arr1[0:2, 1:4])
print(arr1[0:2, 1::2])
print(arr1[0:2, ::2])

arr2 = np.array([[[1, 2, 3, 4, 5], [5, 6, 7, 8, 9]], [[10, 20, 30, 40, 50], [50, 60, 70, 80, 90]]])
print(arr2[1, 0, 1:4])
print(arr2[0:2, 1])
print(arr2[0:2, 1, 0::2])

