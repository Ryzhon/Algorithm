import math

INFTY = 2**31 - 1


def merge(arr, p, q, r):
    n = q - p + 1
    m = r - q
    left = [INFTY] * (n + 1)
    right = [INFTY] * (m + 1)
    for i in range(0, n):
        left[i] = arr[p + i]
    for j in range(0, m):
        right[j] = arr[q + j + 1]

    i = j = 0
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1


def merge_sort(arr, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)
