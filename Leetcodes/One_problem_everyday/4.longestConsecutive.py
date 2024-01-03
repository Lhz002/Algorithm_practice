from typing import List


def longestConsecutive(nums: List[int]) -> int:
    nums.sort()
    ans = []
    k = 0
    for i in range(k, len(nums) - 1):
        if nums[i] == nums[i + 1] - 1:
            ans.append(nums[i])
            if nums[i] not in ans:
                ans.append(nums[i])
            if nums[i + 1] not in ans:
                ans.append(nums[i + 1])
        else:
            k = i + 1  # Update k to the next starting index after the break
            break  # 'break' will exit the loop, so 'k' will not be used anymore in this loop
    return len(set(ans))  # Use set to avoid duplicates



if __name__ == "__main__":
    ans = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(ans))
