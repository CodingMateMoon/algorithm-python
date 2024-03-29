from typing import List

#https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4606/
"""
Constraints:

1 <= matches.length <= 105
matches[i].length == 2
1 <= winneri, loseri <= 105
winneri != loseri

matches[i] = [winner(i), loser(i)]
"""
class Solution:

    def findWinners_1(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        loser_dict = {}
        losers = []
        for winner, loser in matches:
            winners.add(winner)
            if loser in loser_dict:
                loser_dict[loser] += 1
                continue
            loser_dict[loser] = 1

        for key, value in loser_dict.items():
            print(f"loser / {key} : {value}")

        copy_of_set = winners.copy()

        for winner in copy_of_set:
            if winner in loser_dict:
                winners.remove(winner)

        for key, value in loser_dict.items():
            if value == 1:
                losers.append(key)
        losers.sort()
        winners_list = list(winners)
        winners_list.sort()
        return [winners_list, losers]

    # Time : O(N * logN)
    # Space : O(N)
    def findWinners_2(self, matches: List[List[int]]) -> List[List[int]]:
        zero_loss = set()
        one_loss = set()
        more_losses = set()

        for winner, loser in matches:

            if winner not in one_loss and winner not in more_losses:
                zero_loss.add(winner)

            if loser in more_losses:
                continue

            if loser in zero_loss:
                zero_loss.remove(loser)
                one_loss.add(loser)
            elif loser in one_loss:
                one_loss.remove(loser)
                more_losses.add(loser)
            else:
                one_loss.add(loser)

        return [sorted(list(zero_loss)), sorted(list(one_loss))]


    # Time : O(N * logN)
    # Space : O(N)
    def findWinners_3(self, matches: List[List[int]]) -> List[List[int]]:
        seen = set()
        losses_count = {}

        for winner, loser in matches:
            seen.add(winner)
            seen.add(loser)
            losses_count[loser] = losses_count.get(loser, 0) + 1

        zero_lose, one_lose = [], []
        for player in seen:
            count = losses_count.get(player, 0)
            if count == 0:
                zero_lose.append(player)
                continue
            if count == 1:
                one_lose.append(player)

        return [sorted(zero_lose), sorted(one_lose)]

    def findWinners_4(self, matches: List[List[int]]) -> List[List[int]]:
        losses_count = {}

        for winner, loser in matches:
            losses_count[winner] = losses_count.get(winner, 0)
            losses_count[loser] = losses_count.get(loser, 0) + 1

        zero_loss, one_loss = [], []
        for player, count in losses_count.items():
            if count == 0:
                zero_loss.append(player)
            elif count == 1:
                one_loss.append(player)

        return [sorted(zero_loss), sorted(one_loss)]

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses_count = [-1] * 100001

        for winner, loser in matches:
            if losses_count[winner] == -1:
                losses_count[winner] = 0
            if losses_count[loser] == -1:
                losses_count[loser] = 1
                continue
            losses_count[loser] += 1

        answer = [[], []]
        for player in range(100001):
            if losses_count[player] == 0:
                answer[0].append(player)
                continue
            if losses_count[player] == 1:
                answer[1].append(player)

        return answer



            







def test_findWinners():
   solution = Solution()
   """
   항상 이긴 경우, 1번만 진 경우 구하기.
    answer[0] is a list of all players that have not lost any matches.
    answer[1] is a list of all players that have lost exactly one match 
    Players 1, 2, and 10 have not lost any matches.
    Players 4, 5, 7, and 8 each have lost one match.
    Players 3, 6, and 9 each have lost two matches.
    Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
   """
   assert solution.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]) == [[1,2,10],[4,5,7,8]]
   assert solution.findWinners([[2,3],[1,3],[5,4],[6,4]]) == [[1,2,5,6],[]]
