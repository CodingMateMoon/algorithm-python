class Solution:
    # https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4663/
    def maxNumberOfBalloons(self, text: str) -> int:
        return 1

def test_maxNumberOfBalloons():
    """
    text에 있는 알파벳으로 balloon 최대 구성 가능한 횟수
    :return:
    """
    solution = Solution()
    assert solution.maxNumberOfBalloons("nlaebolko") == 1
    assert solution.maxNumberOfBalloons("loonbalxballpoon") == 2
