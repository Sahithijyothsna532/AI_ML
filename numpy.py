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

#generate arrays
np.arrange(10) ##generate elements as like range
np.linspace(0,1,5) #start, end , no of points [0., 0.25, 0.5, 0.75, 1] 

np.ones((3,3)) ##creates all elements as ones in the given dimension 
np.zeros((3,3)) ##creates all the elements as zeros in the given dimension 

np.eye(3) ## creates diagonal elements with ones in 3d array as in square matrix 
np.diag([1,2,3,4]) ## creates elemets as diagonal 

np.full((2,3), 7) ##creates 2x3 matrix with all values as 7

np.random.rand(4) ##generate random 4 element arrays 

a = np.arrange(10)
a.dtype() #gives type of numpy array 

# U can store any data type in the arrary by explicitly defining the data type 

a = np.array([1,2,[1,2], "sahithi", np.array([1,2,3])], dtype = 'O')
