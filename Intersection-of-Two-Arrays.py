class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        seen = set()
        result = []

        for number in nums1:
            if number in nums2 and number not in seen:
                result.append(number)
                seen.add(number)
        return result
                

        
