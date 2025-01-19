#TC - O(n)
#Sc - O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 2 pointer method with one at right anf one left 
        # the formula to calculate would be length - right-left+1 * min(left,right)
        # store in a varible and for increment the pointer which is less than the other and each step keep on checking

        right,left = len(height)-1 , 0 
        maxArea = 0
        while left<right:
            currentArea = (right-left) * min(height[left], height[right])
            maxArea = max(currentArea, maxArea)
            if height[left]>=height[right]:
                right-=1
            else:
                left+=1  
        return maxArea          

        
