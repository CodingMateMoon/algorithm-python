# https://leetcode.com/problems/group-anagrams/description/
import collections
from typing import List


class Solution:
    def groupAnagrams_1(self, strs: List[str]) -> List[List[str]]:
        answer = []
        length = len(strs)
        isUsed = [False] * length
        for i in range (length):
            sorted_string = sorted(strs[i])
            same_elements = []
            if isUsed[i] is False:
                same_elements.append(strs[i])
            for j in range(i + 1, length):
                if sorted_string == sorted(strs[j]) and isUsed[j] is False:
                    same_elements.append(strs[j])
                    isUsed[j] = True

            if len(same_elements) > 0:
                answer.append(same_elements)

        return answer
    def groupAnagrams_1(self, strs: List[str]) -> List[List[str]]:
        answer = collections.defaultdict(list)
        for s in strs:
            answer[tuple(sorted(s))].append(s)
        return answer.values()
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            answer[tuple(count)].append(s)
        return answer.values()

def test_groupAnagrams():
    """"
    nat, tan 동일한 알파벳으로 구성된 문자열 그룹화. e, a, t로 구성된 문자열 탐색 및 그룹화.
    aet 정렬한 값 일치하는지 비교. 26개 알파벳 중에서 개수 체크. pop, add.
    """
    solution = Solution()
    assert solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]