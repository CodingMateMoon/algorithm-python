from typing import List


# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4661/
class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr.sort()
        count = 0
        run_length = 1
        for i in range(len(arr)):
            if arr[i - 1] != arr[i]:
                if arr[i - 1] + 1 == arr[i]:
                    count += run_length
                run_length = 0
            run_length += 1
            run_length += 1
        return count
    def countElements_2(self, arr: List[int]) -> int:
        hash_set = set(arr)
        count = 0
        for x in arr:
            if x + 1 in hash_set:
                count += 1
        return count
    
    def countElements_1(self, arr: List[int]) -> int:

        answer = 0

        for i in range(len(arr)):
            if arr[i] + 1 in arr:
                answer += 1

        return answer

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
