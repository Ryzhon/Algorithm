def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def partition(arr, p, r):
    pivot = arr[r]
    i = p
    for j in range(p,r):
        if arr[j] <= pivot:
            swap(arr, i, j)
            i +=1
    swap(arr, i, r)

    return i

def quick_sort(arr, p, r):
    if p<r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q-1)
        quick_sort(arr, q+1, r)
        