#You are given an array arr of size n. You need to print the array elements from start to end using given recursive function.
#Input:
#n = 5
#arr[] = {1,2,3,4,5}
#Output: 1 2 3 4 5



class Solution:
    def printArrayRecursively(self,arr,n):
        #code here
        if n > 0:
            print(arr[0], end=" ")
            self.printArrayRecursively(arr[1:], n-1)
            
sol = Solution()
sol.printArrayRecursively([5,2,6,8,9,4,3], 7)
