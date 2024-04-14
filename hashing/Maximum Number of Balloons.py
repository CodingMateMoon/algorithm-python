class Solution:
    # https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4663/
    def maxNumberOfBalloons(self, text: str) -> int:
        standard = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}

        elements_count = {}
        for element in text:
            if element == 'b' or element == 'a' or element == 'l' or element == 'o' or element == 'n':
                elements_count[element] = elements_count.get(element, 0) + 1

        balloon_count = 0
        while True:
            for key, value in elements_count.items():
                if value - standard[key] < 0:
                    return balloon_count
                elements_count[key] -= standard[key]

        return balloon_count


def test_maxNumberOfBalloons():
    """
    text에 있는 알파벳으로 balloon 최대 구성 가능한 횟수
    b : 1
    a : 1
    l : 2
    o : 2
    n : 1
    b, a, l, o, n  각 필수 count를 만족해서 만들 수 있는 balloon 개수 구하기
    :return:
    """
    solution = Solution()
    assert solution.maxNumberOfBalloons("nlaebolko") == 1
    #assert solution.maxNumberOfBalloons("loonbalxballpoon") == 2