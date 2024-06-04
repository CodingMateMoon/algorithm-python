#https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4664/
class Solution:
    def numJewelsInStones_1(self, jewels: str, stones: str) -> int:
        answer = 0
        for stone in stones:
            if stone in jewels:
                answer += 1
        return answer
    def numJewelsInStones_2(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        Jset = set(jewels)
        return sum(s in Jset for s in stones)

def test_numJewelsInStones():
    """
    1 <= jewels.length, stones.length <= 50
    jewels and stones consist of only English letters.
    All the characters of jewels are unique.
    """
    solution = Solution()
    assert solution.numJewelsInStones("aA", "aAAbbbb") == 3