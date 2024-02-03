from typing import List


# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4661/
class Solution:
    def countElements(self, arr: List[int]) -> int:

        answer = 0

        num_set = set(arr)
        arr = list(num_set)
        arr.sort()
        for i in range(len(arr) - 1):
            if arr[i] + 1 == arr[i + 1]:
                answer += 1
        return answer


def test_countElements():
    """
    x, x+1 연속된 숫자쌍이 있는 경우 구하기
    list 정렬 후 x, x+1 숫자쌍 체크
    연속된 인덱스 상관없이 list안에만 존재하면 count. e.g) 1, 3, 2
    set에서 +-1 값 있는지 탐색
    1 <= arr.length <= 1000
    0 <= arr[i] <= 1000
    """
    solution = Solution()
    # 1,2 / 3,4
    assert solution.countElements([1, 2, 3]) == 2
    assert solution.countElements([1, 1, 3, 3, 5, 5, 7, 7]) == 0
    assert solution.countElements([1, 3, 2, 3, 5, 0]) == 3
    assert solution.countElements([1,1,2,2]) == 2
