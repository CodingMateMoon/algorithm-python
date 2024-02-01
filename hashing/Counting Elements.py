from typing import List

# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4661/
class Solution:
    def countElements(self, arr: List[int]) -> int:

        answer = 0

        for i in range(len(arr) - 1):
            if (arr[i] + 1) == arr[i + 1] or arr[i] == (arr[i + 1] + 1):
                answer += 1
        return answer



def test_countElements():
    """
    x, x+1 연속된 숫자쌍이 있는 경우 구하기
    1 <= arr.length <= 1000
    0 <= arr[i] <= 1000
    """
    solution = Solution()
    # 1,2 / 3,4
    assert solution.countElements([1, 2, 3]) == 2
    assert solution.countElements([1, 1, 3, 3, 5, 5, 7, 7]) == 0
    assert solution.countElements([1,3,2,3,5,0]) == 3
