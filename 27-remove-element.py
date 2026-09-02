# 27. Remove Element
# LeetCode - Easy

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        result = []

        for number in nums:
            if number != val:
                result.append(number)

        nums[:len(result)] = result

        return len(result)
