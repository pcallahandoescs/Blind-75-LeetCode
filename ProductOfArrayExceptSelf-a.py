class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length
        for i in range(1, length):
            answer[i] = answer[i-1] * nums[i-1]

        right = nums[-1]
        for i in range(length-2, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer