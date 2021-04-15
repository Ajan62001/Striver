def sort012(arr):
    c0,c1 =0,0
    for ele in arr:
        if ele == 0:
            c0+=1
        elif ele == 1:
            c1+=1
    print(c0,c1)
    for i in range(len(arr)):
        arr[i] = 0 if i<c0 else 1 if i<c1+c0 else 2
    return arr

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
print(sort012(arr))

        