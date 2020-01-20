import numpy as np
from utils import getXY
from plot import myPlot

#set the seed
np.random.seed(111)

#set the values
MAX_LENGTH = 10**3
STEP = 50


#generating the random array
array = np.random.randint(1,high=500,size=(MAX_LENGTH))

#for the worse case we need array sorted in decending order, so reversing
reversed_array  = array[::-1]



#give message to user
print("Array before being sorted is ",array[:100],"...",array[-100:])
print("Sorting...\nIt may take a while..")


print("For bubblesort")
#FOR BUBBLE SORT
sorted_array,x_data_size,y_time_took = getXY(
    reversed_array,
    MAX_LENGTH,
    STEP,
    sort_type="bubble"
)
print("The sorted array is:",sorted_array[:100],"...",sorted_array[-100:])

#plot x & y
myPlot(x_data_size,y_time_took,x_label="Size of array",y_label="Milliseconds took",title="Worse case of bubble sort")
#bubblesortends



print("For Mergesort")
#FOR MERGE SORT
sorted_array,x_data_size,y_time_took = getXY(
    reversed_array,
    MAX_LENGTH,
    STEP,
    sort_type="merge"
)
print("The sorted array is:",sorted_array[:100],"...",sorted_array[-100:])

#plot x & y
myPlot(x_data_size,y_time_took,x_label="Size of array",y_label="Milliseconds took",title="Worse case of merge sort")
#mergesortends
