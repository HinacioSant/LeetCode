# Problem 1672. Richest Customer Wealth:

#  You are given an m x n integer grid accounts where accounts[i][j] is
# the amount of money the i customer has in the j  bank. Return the
# wealth that the richest customer has.  A customer's wealth is the
# amount of money they have in all their bank accounts. The richest
# customer is the customer that has the maximum wealth.

# Solution:
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        answer = 0
        for a in accounts:
            if answer < sum(a):
                answer = sum(a)
        return answer
