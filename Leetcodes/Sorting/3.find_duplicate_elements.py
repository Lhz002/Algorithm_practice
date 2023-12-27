from typing import List
def containsDuplicate(nums: List[int]) -> bool:
    n = len(nums)
    if n <= 1:
        return False
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break

    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            return True

    return False



def containsDuplicate(self, nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    nums = [2, 14, 18, 22, 22]
    print(containsDuplicate(nums))

