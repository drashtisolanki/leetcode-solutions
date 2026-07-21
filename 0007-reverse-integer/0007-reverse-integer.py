class Solution(object):
    def reverse(self, x):
        number = abs(x)
        reverse = 0

        while number > 0:
            reminder = number % 10
            reverse = reverse * 10 + reminder
            number = number // 10

        if x < 0:
            reverse = -reverse

        if reverse < -2**31 or reverse > 2**31 - 1:
            return 0

        return reverse