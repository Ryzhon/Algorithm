def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def bubble_sort(arr,n):
    for i in range(0, n-1):
        for j in range(n-1, i, -1):
            if arr[j] < arr[j-1]:
                swap(arr, j, j-1)

                