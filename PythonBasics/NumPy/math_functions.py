from numpy import *

arr1 = array([5, 20, 3, -4])
arr2 = array([5, 6, 7, 8])

print(arr1 + arr2)
print(arr1 - 1)
print(sin(arr1))
print(mean(arr1))
print(abs(arr1))
print(max(arr1))
print(sum(arr2))
print(arr1 >= arr2)
print(arr1 < arr2)
print(any(arr1 > arr2))
print(all(arr1 > arr2))

print(logical_and(arr1 > 5, arr1 < 60))
print(logical_or(arr1 > 5, arr1 < 60))

print(where(arr2%2 != 0, arr2, 0))
print(where(arr1 > arr2, arr1, arr2))

a = array([10,20,30,40])
b = a.view()
print(a)
print(b)

b[2] = 80
print('After modification for view')
print(a)
print(b)

b = a.copy()
b[2] = 300
print('After modification for copy')
print(a)
print(b)

arr = arange(1,12)
print(arr)
print(arr[3:7])
print(arr[3:9:2])
print(arr[2:])


a1 = array([1,2,3])
a2 = array([[1,2,3],[1,2,3]])
a3 = array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])

print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

print(a1.shape)
print(a2.shape)
print(a3.shape)

a2.shape = (3,2)
print(a2)

print(a1.size)
print(a2.size)
print(a3.size)

print(a1.dtype)
print(a1.itemsize)
print(a1.nbytes)


a = arange(12)
print(a)
a1 = reshape(a,(4,3))
print(a1)
a2 = reshape(a,(2,3,2))
print(a2)
a3 = a2.flatten()
print(a3)

print(eye(3))

print(ones((2,3),int))
print(zeros((2,3),int))



