# https://leetcode.com/problems/group-anagrams/description/
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        length = len(strs)
        isUsed = [False] * length
        for i in range (length):
            sorted_string = sorted(strs[i])
            same_elements = [strs[i]]
            for j in range(i + 1, length):
                if sorted_string == sorted(strs[j]) and isUsed[j] is False:
                    same_elements.append(strs[j])
                    isUsed[j] = True

            answer.append(same_elements)

        return answer

def test_groupAnagrams():
    """"
    nat, tan 동일한 알파벳으로 구성된 문자열 그룹화. e, a, t로 구성된 문자열 탐색 및 그룹화.
    aet 정렬한 값 일치하는지 비교. 26개 알파벳 중에서 개수 체크. pop, add.
    """
    solution = Solution()
    assert solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]