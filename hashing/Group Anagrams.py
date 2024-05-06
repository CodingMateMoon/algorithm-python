# https://leetcode.com/problems/group-anagrams/description/
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        for str in strs:
            sorted_string = ''.join(sorted(str))
            print(f"{str} : {sorted_string}")


        return None

def test_groupAnagrams():
    """"
    nat, tan 동일한 알파벳으로 구성된 문자열 그룹화. e, a, t로 구성된 문자열 탐색 및 그룹화.
    aet 정렬한 값 일치하는지 비교. 26개 알파벳 중에서 개수 체크. pop, add.
    """
    solution = Solution()
    assert solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]