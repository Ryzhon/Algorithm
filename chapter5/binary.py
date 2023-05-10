import math

def binary_search(arr, key, p,r):
    if r < p:
        return None
    else:
        q = math.floor((p+r)/2)
        if arr[q] > key:
            return binary_search(arr, key, p, q-1)
        elif arr[q] < key:
            return binary_search(arr, key, q+1, r)
        else:
            return q