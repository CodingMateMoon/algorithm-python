from typing import List


#https://leetcode.com/problems/find-the-highest-altitude/description/
"""
n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

"""
class Solution:

    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        # Highest altitude currently is 0.
        highest_point = current_altitude

        for altitude_gain in gain:
            # Adding the gain in altitude to the current altitude.
            current_altitude += altitude_gain
            # Update the highest altitude.
            highest_point = max(highest_point, current_altitude)

        return highest_point

    def largestAltitude_1(self, gain: List[int]) -> int:

        sum = highest_altitude = 0

        for altitude in gain:
            sum += altitude
            highest_altitude = max(highest_altitude, sum)

        return highest_altitude


def test_largestAltitude():
    solution = Solution()
    assert solution.largestAltitude([-5, 1, 5, 0, -7]) == 1
    assert solution.largestAltitude([-4, -3, -2, -1, 4, 3,2]) == 0
