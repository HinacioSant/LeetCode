# Problem 231:
# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.



# Solution:
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        b = 0
        answer = self.answer(b,n)
        return answer
    def answer(self, b, n):
        a = 2**b
        if a < n:
            b += 1
            answer = self.answer(b, n)
        elif a == n:
            answer = True
        else:
            answer = False

        return answer
       
