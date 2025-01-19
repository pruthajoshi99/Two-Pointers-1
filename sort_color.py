class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Brute force Approach 
        #Using HashMap for colors and there freq move through them freq and add theat in the array as it is

        #TC - O(n) for hashMap + O(n) from hashmap -> O(n)
        #SC - O(1) ->  as only 3 colorsfor hashmap

        # freqMap = {}
        # freqMap[0] = 0
        # freqMap[1] = 0
        # freqMap[2] = 0

        # for num in nums:
        #     freqMap[num]+=1

        # i=0
        # for key,val in freqMap.items():
        #     for freq in range(val):
        #         nums[i] = key
        #         i+=1
        # return nums    


        ## 2nd Approach
        # 3 pointers 
        #TC - O(n)
        #SC - O(1)

        red = 0
        white = 0
        blue = len(nums)-1

        while white<=blue:

            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                white+=1
                red+=1

            elif nums[white] == 2:
                nums[white],nums[blue] = nums[blue], nums[white]
                blue-=1

            else:
                white+=1            


        
