class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        for i in magazine:

            count = magazine_dict.get(i)
            if count == None:
                count = 0
            magazine_dict[i] = count + 1

        #for key, value in magazine_dict.items():
            # print(f"{key} : {value}")

        for i in ransomNote:
            count = magazine_dict.get(i)
            if count == 0 or count == None:
                return False
            magazine_dict[i] = count - 1

        return True




    def canConstruct_1(self, ransomNote: str, magazine: str) -> bool:

        char_magazine_list = list(magazine)
        for i in ransomNote: # O(n)
            isContained = False
            for j in range(0, len(char_magazine_list)):
                if char_magazine_list[j] == i:
                    isContained = True
                    char_magazine_list.remove(char_magazine_list[j] )
                    break
            if isContained == False:
                return False

        return True

    # dictionary
    # time O(m) : magzine.length >= ransomNOte.length
    # O(k) <= 26 -> O(1)








            


if __name__ == '__main__':

    print(Solution().canConstruct("aa", "ab"))
    print(Solution().canConstruct("aa", "aab"))
    print(Solution().canConstruct("aab", "baa"))
    print(Solution().canConstruct("a", "b"))