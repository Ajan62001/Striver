def findDupli(Arr):
    length = len(arr)
    newArr = []
    duplset = {}
    for ele in arr:
        try:
            duplset[ele]+=1
        except:
            duplset[ele]=1
    for key,value in duplset.items():
        if value>1:
            newArr.append(key)
    return newArr

arr = [ 12, 11, 40, 12, 5, 6, 5, 12, 11 ]
print(findDupli(arr))