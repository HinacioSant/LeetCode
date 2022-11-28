# Problem 412. Fizz Buzz:

#  Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5. answer[i] ==
# "Fizz" if i is divisible by 3. answer[i] == "Buzz" if i is divisible
# by 5. answer[i] == i (as a string) if none of the above conditions
# are true.

# Solution:
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = 0
        answer = []
        while a != n:
            a += 1
            if (a/3).is_integer() and (a/5).is_integer():
                answer.append("FizzBuzz")
            elif (a/3).is_integer():
                answer.append("Fizz")
            elif (a/5).is_integer():
                answer.append("Buzz")
            else:
                answer.append(str(a))
        return answer
