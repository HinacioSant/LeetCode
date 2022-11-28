# Problem 13. Roman to Integer:

#  Given a roman numeral, convert it to an integer.

# Solution:
class Solution:
    def romanToInt(self, s: str) -> int:
        d ={ "I": 1,"V" : 5,"X" : 10,"L": 50,"C": 100,"D" : 500,"M" : 1000}
        answer = 0
        temp = 1001
        for a in s:
            for key, value in d.items():
                if a == key:
                    if value > temp:
                        answer -= temp*2
                    answer += value
                    temp = value
        return answer
     
