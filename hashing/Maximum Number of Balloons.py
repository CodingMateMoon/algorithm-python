class Solution:
    # https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4663/
    def maxNumberOfBalloons_1(self, text: str) -> int:
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
            balloon_count += 1

        return balloon_count
    def maxNumberOfBalloons_2(self, text: str) -> int:
        b_count = a_count = l_count = o_count = n_count = 0
        for element in text:
            if element == "b":
                b_count += 1
            elif element == "a":
                a_count += 1
            elif element == "l":
                l_count += 1
            elif element == "o":
                o_count += 1
            elif element == "n":
                n_count += 1

        l_count /= 2
        o_count /= 2

        return min(b_count, min(a_count, min(l_count, min(o_count, n_count))))

    def maxNumberOfBalloons(self, text: str) -> int:
        pattern = "balloon"
        return self.findMaxNumberOfPattern(text, pattern)

    def findMaxNumberOfPattern(self, text: str, pattern: str):
        freq_in_text = [0] * 26
        freq_in_pattern = [0] * 26
        return 1


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
    assert solution.maxNumberOfBalloons("loonbalxballpoon") == 2
