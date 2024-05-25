from typing import List


# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        elements_count = {}
        for element in cards:
            elements_count[element] = elements_count.get(element, 0) + 1
            if elements_count[element] == 2:
                print(f"{element} count : {elements_count[element]}")
            print(f"test : {element} : {elements_count[element]}")


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
