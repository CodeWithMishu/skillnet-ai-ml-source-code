import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 4, 3, 2, 4, 5, 6, 7, 89, 995, 4, 3, 5])
# arr1 = np.array(["apple", "banana", "cherry", "date"])
# print(arr.dtype)  # Print the data type of the array
# print(arr1.dtype)  # Print the data type of the array
# arr2 = np.array(['"apple", "banana", "cherry", "date"'])

# arr = np.array([1,2,3,4,5],dtype='S')
# # dtype = 's'
# print(arr.dtype)

# arr = np.array([1,2,3,4,5],dtype='i')
# arr1 = np.array([1.11,2.3,3.7,4.0,5.4],dtype='f4')
# print(arr.dtype)
# print(arr1.dtype)

# arr = np.array([1.1,2.2,3.3,4.4])
# newarr = arr.astype(int)
# print(newarr.dtype)

# arr=np.array([1,0,3])
# newarr=arr.astype(bool)
# print(newarr.dtype)

# arr = np.array([-1,0,1])
# newarr = arr.astype(bool)
# print(newarr)


# arr = np.array([1,2,3,4,5])
# arr[0]=42
# x = arr.copy()
# print(arr)
# print(x)

# arr = np.array([1,2,3,4,5])
# x = arr.view()
# arr[0]=42
# print(arr)
# print(x)
# arr[3]=44
# print(x)

# arr = np.array([1,2,3,4,5,6])
# x=arr.copy()
# y=arr.view()
# print(x.base)
# print(y.base)

# arr = np.array([1,2,3,4],ndmin=5)
# print(arr)
# print("share of array",arr.shape)
# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr = arr.reshape(3,4)
# print(newarr)

# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr = arr.reshape(2,3,2)
# print(newarr)


# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr = (arr.reshape(2,6).base)
# # x = newarr.base
# print(newarr)
# print(x) 

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr = arr.reshape(2,3,-1)
# print(newarr)

# masking and filtering
# a= np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# mask=a>3
# print(a[mask])

# broadcasting
# a=np.array([1,2,3,4,5])
# b=5
# print(a+b)

# print(np.random.rand(3))
# print(np.random.randint(1,10,5))
# print(np.random.randn(3,3))
# print(np.random.seed(42))

# customm indexing
# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# ghochu =[0,2,4]
# print(a[ghochu])

# dtype Un
# we will use n here instead of any number to make our code memory efficient 
# a=np.array((['cat','dog']),dtype='U3')
# print(a.dtype)

# from numpy.linalg import inv,det,eig
# a=np.array([[1,2],[3,4]])
# result =np.dot(a,a)
# # inv(a)
# # det(a)
# # eig(a)
# print(result)
# print(inv(a),det(a),eig(a))


# a=np.array([1,2,3,4])
# np.save('my_array.npy',a)
# np.load('my_array.npy')
# np.savetxt('data.csv',a, delimiter=',')
# np.genfromtxt('data.csv',delimiter=',')

arr = np.array([1,2,3,4,5,'a'])
arr = np.array([np.nan,1,0,2,0])
arr1 = np.array([1,2,'b',4,5,'a'])
print(np.nan)
# print(np.nan_to_num(arr))

import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4, 5, 'a'])
s = pd.to_numeric(arr, errors='coerce')  # 'a' becomes NaN
print(pd.isna(s))  # True for 'a', False for numbers