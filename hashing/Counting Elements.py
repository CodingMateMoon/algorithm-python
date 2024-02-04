from typing import List


# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4661/
class Solution:
    def countElements(self, arr: List[int]) -> int:

        num_dict = {}
        answer = 0

        for i in range(len(arr)):
            num_dict[arr[i]] += 1

        for value in num_dict:
            print(f"val : {value}")


def test_countElements():
    """
    x, x+1 연속된 숫자쌍이 있는 경우 구하기
    list 정렬 후 x, x+1 숫자쌍 체크
    연속된 인덱스 상관없이 list안에만 존재하면 count. e.g) 1, 3, 2
    중복 숫자쌍 허용
    map 숫자별 count 세기
    1 <= arr.length <= 1000
    0 <= arr[i] <= 1000
    """
    solution = Solution()
    # 1,2 / 3,4
    assert solution.countElements([1, 2, 3]) == 2
    assert solution.countElements([1, 1, 3, 3, 5, 5, 7, 7]) == 0
    assert solution.countElements([1, 3, 2, 3, 5, 0]) == 3
    assert solution.countElements([1, 1, 2, 2]) == 2
