from typing import List

# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        return 4

def minimumCardPickup():
    """
    1 <= cards.length <= 105
0 <= cards[i] <= 106
    """
    solution = Solution()
    assert solution.minimumCardPickup([3,4,2,3,4,7]) == 4
    assert solution.minimumCardPickup([1,0,5,3]) == -1
