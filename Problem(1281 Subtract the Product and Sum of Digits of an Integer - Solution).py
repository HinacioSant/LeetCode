# Problem 1281:
# Given an integer number n, return the difference between the product of its digits and the sum of its digits.


# Solution:
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = list(map(int, str(n)))
        answer = 1
        for i in a:
            answer = answer * i
        return answer - sum(a)
