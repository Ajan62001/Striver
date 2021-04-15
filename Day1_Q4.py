def merge(self,arr1,arr2,n,m):
        # for array2 traverse from last 
        l = len(arr1)-2
        for i in range(len(arr2)-1,-1,-1):
            last = arr1[-1]
            if last>arr2[i]:
                for j in range(l,-2,-1):
                    if arr1[j]<arr2[i] or j<0:
                        for k in range(len(arr1)-1,j,-1):
                            arr1[k] = arr1[k-1]
                        
                        arr1[j+1] = arr2[i]
                        l = j
                        break
                    
                        
                arr2[i] = last