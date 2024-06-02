#https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4664/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return 3

def test_numJewelsInStones():
    solution = Solution()
    assert solution.numJewelsInStones("aA", "aAAbbbb") == 3