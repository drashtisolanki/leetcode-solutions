"""
LeetCode 796 - Rotate String
Difficulty: Easy
Topic: Strings
"""

class Solution(object):
    def rotateString(self, s, goal):
        return "".join(sorted(s)) == "".join(sorted(goal)) and goal in (s + s)

"""
Optimal Version
"""
class Solution(object):
    def rotateString(self, s, goal):
        return len(s) == len(goal) and goal in (s + s)
