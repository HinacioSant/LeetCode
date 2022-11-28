# Problem 1342. Number of Steps to Reduce a Number to Zero:

#  Given an integer num, return the number of steps to reduce it to
# zero.  In one step, if the current number is even, you have to
# divide it by 2, otherwise, you have to subtract 1 from it.

# Solution:
class Solution:
    def numberOfSteps(self, num: int) -> int:
        b = 0
        while num > 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
            b += 1
        return b
