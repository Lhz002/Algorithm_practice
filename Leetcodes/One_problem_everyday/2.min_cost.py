from typing import List

class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        ans = []
        for i in range(len(nums)):
            cost = sum(nums) + i*x
            ans.append(cost)
            Solution.type_change(nums)
        return ans

    def type_change(nums:List[int]) -> List:
        n = len(nums)
        nums = nums[::-1]
        for i in range(0, n - 1):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

        return nums[::-1]

if __name__ == "__main__":
    s = Solution()
    print(s.minCost([20,1,15], 5))
