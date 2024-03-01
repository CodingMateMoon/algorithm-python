from typing import List

#https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4606/
"""
Constraints:

1 <= matches.length <= 105
matches[i].length == 2
1 <= winneri, loseri <= 105
winneri != loseri

matches[i] = [winner(i), loser(i)]
"""
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        return [[1,2,10],[4,5,7,8]]

def test_findWinners():
   solution = Solution()
   assert solution.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]) == [[1,2,10],[4,5,7,8]]
   assert solution.findWinners([[2,3],[1,3],[5,4],[6,4]]) == [[1,2,5,6],[]]
