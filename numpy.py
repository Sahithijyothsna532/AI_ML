# Numpy 
import numpy as np 
numpy.array([1,2,3])  # Creating numpy array 
[1,2,3] # The difference b/w numpy array and list is when u print list elements seperated by comma but in numpy array we won't get comma seperated elements

print(np.arrange(10))

%timeit [i**2 for i in range(10)] # time required to create an array 
a = np.arange(10)
%timeit a**2 #time required will take less time than list 

##2D array 
a = np.array([1,2,3], [5,6,7]) # 2d 
##3D array 
a = np.array([1,2,3],[0,9,8],[6,7,8]) #3d
a.shape ## defines shape 
a.size  ## defines size 
a.dtype ## defines type 
a.ndim ## defines dimension 
