# Problem 1356. Sort Integers by The Number of 1 Bits:

#  You are given an integer array arr. Sort the integers in the array in
# ascending order by the number of 1's in their binary representation
# and in case of two or more integers have the same number of 1's you
# have to sort them in ascending order.  Return the array after
# sorting it.

# Solution:
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = {}
        answer = []
        for i in sorted(arr):
            a = bin(i)[2:]
            a = sum(list(map(int, a)))
            d.setdefault(a,[])
            d[a].append(i)
        for k, v in sorted(d.items()):
            for i in v:
                answer.append(i)
        return answer
