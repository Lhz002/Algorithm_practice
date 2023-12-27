"""
This solution uses a dic to store the elements in nums and through searching the elements
in the list to find the most frequency element
"""

def majorityElement(self, nums: List[int]) -> int:

    threshold = len(nums) / 2
    dic = {}
    ans = []
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for key in dic:
        if dic[key] > threshold:
            ans.append(key)

    return ans[0]


def solution2(self, nums: List[int]) -> int:
    votes = 0
    for num in nums:
        if votes == 0: x = num
        votes += 1 if num == x else -1
    return x

