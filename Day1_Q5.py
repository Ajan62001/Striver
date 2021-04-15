def maxSubArraySum(self,a,size):
        ##Your code here
        
        Sum,newsum =a[0],0
        for ele in a:
            newsum+=ele
            if Sum < newsum:
                Sum = newsum
            if(newsum<0):
                newsum=0
        return Sum