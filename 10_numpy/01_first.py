# import numpy as np
# print(np.__version__)
# arr = np.array([1,2,3,4,5])
# arr1 = [1,2,3,4,5]
# print(arr)
# print(type(arr))
# print(type(arr1))

# import numpy as nm
# arr = nm.array((1,2,3,4,5))
# print(arr)
# print(type(arr))

# import numpy as np
# arr = np.array(42) # zero dimension array
# print(arr)


# import numpy as np
# arr=np.array([1,2,3,4,5,6]) # 1D array
# print(arr)
#  # list prints comma while array does not print commas
# list = [1,2,3,4]
# print(list)

# import numpy as np
# arr = np.array([[1,2,3,4],[1,2,3,7]]) # 2D array
# print(arr)


# import numpy as np
# arr = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
# outer square braces are specifying the dimension of array
# print(arr)

# import numpy as np
# arr = np.array([[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]]),([[1,2,3,4],[1,2,3,4]])
# print(arr)

# import numpy as np
# a = np.array(42)
# b=np.array([1,2,3,4,5])
# c=np.array([[1,2,3,4],[1,2,3,4]])
# d=np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
# print(a.ndim,b.ndim,c.ndim,d.ndim)
# print(a.ndim+b.ndim+c.ndim+d.ndim)

# import numpy as np
# arr = np.array([
#     [[1,2,3,4,5],[6,7,8,9,10],[11,22,13,14,15]],
#     [[66,77,0,0,0],[232,43,0,0,0],[434,55,0,0,0]]
# ])
# print(arr[1,2,1])  # Accesses the first block, second row, fourth element

# slicing
# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8,4,3,2,4,5,6,7,89,995,4,3,5])
# print(arr[-8:-3])

# import numpy as np
# arr=np.array([1,2,3,4,5,78])
# print(arr[::1])


# import numpy as np
# arr = np.array([[[1,2,3,4,5,6],[6,7,8,9,0,11],[22,33,44,55,66,77],[98,76,54,43,32,21]]])
# print(arr[0,3,3:4])
