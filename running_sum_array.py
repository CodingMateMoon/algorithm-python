from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(1, len(nums) + 1):
            #print(f"i : {i}")
            sum = 0
            for j in range (0, i):
                sum += nums[j]
            #print(sum)
            answer.append(sum)
        return answer





if __name__ == '__main__':
    solution = Solution()
    print(solution.runningSum([1,2,3,4]))
    print(solution.runningSum([1,1,1,1,1]))
    print(solution.runningSum([3,1,2,10,1]))
