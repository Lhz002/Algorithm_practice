class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # 将 nums2 的元素插入到 nums1 的指定位置
        nums1[m:m+n] = nums2[:n]
        # 排序 nums1 中的前 m+n 个元素
        self.bubble_sorting(nums1, m + n)

    def bubble_sorting(self, nums, k):
        # 只对前 k 个元素进行冒泡排序
        for i in range(k):
            swapped = False
            for j in range(0, k - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            # 如果在这一轮排序中没有发生交换，说明剩余部分已经有序，可以提前退出
            if not swapped:
                break
