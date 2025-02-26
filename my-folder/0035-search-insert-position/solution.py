class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1

        while left_index <= right_index:
            mid = (left_index + right_index) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left_index = mid + 1
            else:
                right_index = mid - 1

        return left_index

#LINEAR SEARCH
        # for index, num in enumerate(nums):
        #     if num == target:
        #         return index
        #     elif nums[0] > target:
        #         return 0
        #     elif nums[-1] < target:
        #         return len(nums)
        #     elif nums[index] < target and nums[index+1] > target:
        #         return index + 1
