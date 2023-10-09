from typing import List


class Solution:
    """
    k만큼 0->1 바꿔서 연속된 1이 가장 길게 나오는 경우 찾기
    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
    0 <= k <= nums.length
    1. 값이 0인 인덱스 정보 탐색 O(n)
    2. i번째 0부터 시작 j번째 0
    1,2,..k만큼 재귀호출 후 가장 길이가 긴 경우 구하기
    0을 k개만큼 허용하는 연속된 1 구하기
    index 0부터 시작해서 0이 나올 경우 1로 변경하고 count++, count=k 됐을 때부터 다음에 나오는 값이 0일 경우 가장 첫번째 0의 index를 빼고 커서에 위치한 0의 index를 저장
    """

    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0
        result = 0
        zero_list = []
        for i in len(nums):
            if i == 1:
                result += 1
            else:
                if count < k:
                    count += 1
                    result += 1


if __name__ == '__main__':
    print(Solution().longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
    print(Solution().longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
