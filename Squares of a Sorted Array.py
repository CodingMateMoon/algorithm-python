"""
-10 -5 1 2 4 7

square : O(n)
sort : O(nLogn)

for loop : O(n)
"""

class Solution(object):

    def sortedSquares(self, nums):
        return sorted(x * x for x in nums)
    def sortedSquares_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1

        for i in range (n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                square = nums[left]
                left += 1
            else:
                square = nums[right]
                right -= 1
            result[i] = square * square

        return result

    def sortedSquares_fail(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[i] > nums[j]):
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        return nums

if __name__ == '__main__':
    print(Solution().sortedSquares([-4,-1,0,3,10]))