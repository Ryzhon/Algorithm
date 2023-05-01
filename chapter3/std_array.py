import array

N =10

def insert(arr, index, val):
    for i in range(N-1, index, -1):
        arr[i] = arr[i-1]
    
    arr[index] =val

def delete(arr, index):
    for i in range(index, N -1):
        arr[i] = arr[i+1]
        print("iの要素", i)
        print("配列の要素",arr)

    arr[N-1] = -1

if __name__== "__main__":
    arr = array.array('i', [6,2,3,7,8,-1,-1,-1,-1,-1])
    print("初期値: ", arr)
    x = arr[2]
    print("arr[2]=",x)
    insert(arr,2,10)
    print("要素の挿入後：", arr)

    delete(arr,2)
    print("要素の削除後:", arr)

