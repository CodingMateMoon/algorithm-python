import sys
from typing import List


# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        elements_count = {}
        index = -1
        min_length = -1
        for i in range(len(cards)):
            elements_count[cards[i]] = elements_count.get(cards[i], 0) + 1
            if elements_count[cards[i]] == 2:
                for j in range(len(cards)):
                    if i == j:
                        continue
                    if cards[j] == cards[i]:
                        if min_length == -1:
                            min_length = i - j + 1
                            continue
                        min_length = min(abs(i - j + 1), min_length)
                        print(f"i : {i}/ j: {j}")
                print(f"{cards[i]} count : {elements_count[cards[i]]}/ min_length : {min_length} / i : {i}, index : {index}")
            print(f"test : {cards[i]} : {elements_count[cards[i]]} / i : {i}")

        return min_length


def test_minimumCardPickup():
    """
    1 <= cards.length <= 105
    0 <= cards[i] <= 106
 3, 4, 2, 3
 4, 2, 3, 4 등 값이 같은 숫자가 있는 최소 부분 집합
 요소별 숫자 개수 및 위치 관리. dict에 숫자별 count 관리하면서 count=2가 됐을 때 해당 숫자 첫번째 위치와 현재 위치를 통해 length 계산 후 최소값 갱신.
    """
    solution = Solution()
    assert solution.minimumCardPickup([3, 4, 2, 3, 4, 7]) == 4
    assert solution.minimumCardPickup([1, 0, 5, 3]) == -1
    assert solution.minimumCardPickup([70,37,70,41,1,62,71,49,38,50,29,76,29,41,22,66,88,18,85,53]) == 3
    assert solution.minimumCardPickup([95,11,8,65,5,86,30,27,30,73,15,91,30,7,37,26,55,76,60,43,36,85,47,96,6]) == 3
