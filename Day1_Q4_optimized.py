def merge(self,arr1,arr2,n,m):
        i,k,j=0,n-1,0
        while(i<=k and j<m):
            if(arr1[i]>arr2[j]):
                arr1[k],arr2[j] =arr2[j],arr1[k]
                k-=1
                j+=1
            else:
                i+=1
        arr1.sort()
        arr2.sort()