# Problem: Minimum Size Subarray Sum
# Topic: Sliding Window
#
# Key Idea:
# Maintain a sliding window and shrink it whenever the sum is large enough.
#
# Approach:
# - Expand the window by moving the right pointer and adding to the running sum.
# - Once the window sum is greater than or equal to target, try to shrink
#   the window from the left to find the minimum valid length.
# - Track the smallest valid window length.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

def minimumSizeSubarraySum(target: int, nums: list[int]) -> int:
	windowSum = 0
	left = 0
	answer = float("inf")
	for right in range(len(nums)):
		windowSum += nums[right]
		while windowSum >= target:
			answer = min(answer, right - left + 1)
			windowSum -= nums[left]
			left += 1
	return 0 if answer == float("inf") else answer
    
if __name__ == "__main__":
    print(minimumSizeSubarraySum(7, [2, 3, 1, 2, 4, 3]))  # 2
    print(minimumSizeSubarraySum(4, [1, 4, 4]))           # 1
    print(minimumSizeSubarraySum(11, [1, 1, 1, 1]))       # 0
