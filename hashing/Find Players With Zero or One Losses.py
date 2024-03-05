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
        winner_list = []
        loser_dict = {}
        for winner, loser in matches:
            winner_list.append(winner)
            if loser in loser_dict:
                loser_dict[loser] += 1
                continue
            loser_dict[loser] = 1

def test_findWinners():
   solution = Solution()
   """
   항상 이긴 경우, 1번만 진 경우 구하기.
    answer[0] is a list of all players that have not lost any matches.
    answer[1] is a list of all players that have lost exactly one match 
    Players 1, 2, and 10 have not lost any matches.
    Players 4, 5, 7, and 8 each have lost one match.
    Players 3, 6, and 9 each have lost two matches.
    Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
   """
   assert solution.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]) == [[1,2,10],[4,5,7,8]]
   assert solution.findWinners([[2,3],[1,3],[5,4],[6,4]]) == [[1,2,5,6],[]]
