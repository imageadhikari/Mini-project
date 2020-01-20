from math import *
def merge(arr,start,mid,end):
    L = arr[start:mid]
    R = arr[mid:end]

    L.append(1000)
    R.append(1000)
    i=0
    j=0
    for k in range(start,end):
        if L[i]<=R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1


def mergesort(arr,start,end):
    """
    Algorithm to sort array of integers in accending order
    @param arr --- unsorted array
    @returns --- sorted array
    """
    if start<end:
        mid = floor((start+end)//2)
        mergesort(arr,start,mid)
        mergesort(arr,mid+1,end)
        merge(arr,start-1,mid,end)
    
    return arr


