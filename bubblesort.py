import numpy as np
import matplotlib.pyplot as plt
import time

def bubbleSort(arr):
    """
    Algorithm to sort array of integers in accending order
    @param arr --- unsorted array
    @returns --- sorted array
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

