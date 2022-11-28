# Problem 1005:

#  Given an integer array nums and an integer k, modify the array in the
# following way:  choose an index i and replace nums[i] with -nums[i].
# You should apply this process exactly k times. You may choose the
# same index i multiple times.  Return the largest possible sum of the
# array after modifying it in this way.

# Solution:
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0 or k == 0:
                break
            nums[i] = -nums[i]
            k -= 1
        print(sum(nums), "|-|", (k % 2) * min(nums) *2)
        return sum(nums) - (k % 2) * min(nums) * 2
