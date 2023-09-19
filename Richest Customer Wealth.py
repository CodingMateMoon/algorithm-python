from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxValue = -1
        for account in accounts:
            sum = 0
            for element in account:
                sum += element
            maxValue = max(maxValue, sum)
        return maxValue






if __name__ == '__main__':
    print(Solution().maximumWealth([[1,2,3],[3,2,1]]))
    print(Solution().maximumWealth([[1,5],[7,3],[3,5]]))
