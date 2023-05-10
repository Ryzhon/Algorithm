def linear_search(arr, key):
    for i in range(0, len(arr)):
        if arr[i] == key:
            return i
        
    return None