import numpy as np
import time

from bubblesort import bubbleSort
from merge_sort import mergesort

def getXY(array,MAX_LENGTH,STEP,sort_type="bubble"):
    x_data_size = []
    y_time_took = []

    sorted_array = []
    for i in range(0,MAX_LENGTH,STEP):
        #get the sub set of array
        sub_array = array[:i]

        tok = time.time()
        #sort it 
        if(sort_type == "merge"):
            sorted_array = mergesort(sub_array.tolist(),1,len(sub_array))

        else:
            bubbleSort(sub_array)
            sorted_array = sub_array
        tik = time.time()
        time_took = tik - tok

        #update the array
        x_data_size.append(i)
        y_time_took.append(time_took)

        
    return sorted_array,x_data_size,y_time_took
