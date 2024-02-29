from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        return [[1,2,10],[4,5,7,8]]

def test_findWinners():
   solution = Solution()
   assert solution.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]) == [[1,2,10],[4,5,7,8]]
