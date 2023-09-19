class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        count = 0
        while True:
            if num == 1:
                count += 1
                break;
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
            count += 1
        return count


if __name__ == '__main__':
    print(Solution().numberOfSteps(14))
    print(Solution().numberOfSteps(8))