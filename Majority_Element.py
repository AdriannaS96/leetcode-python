class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = {}

        for number in nums:
            if number in count:
                count[number] += 1
            else:
                count[number] = 1

        for number in count:
            if count[number] > len(nums) / 2:
                return number 
        
            

