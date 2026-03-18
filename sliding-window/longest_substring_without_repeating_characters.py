# Problem: Longest Substring Without Repeating Characters
# Topic: Sliding Window
#
# Key Idea:
# Use a hash map to record the last seen index of each character.
#
# Approach:
# - Maintain a sliding window with two pointers.
# - Use a hash map to store the most recent index of each character.
# - If a repeated character appears inside the current window,
#   move the left pointer to one position after its last occurrence.
# - Track the maximum window length.
#
# Time Complexity: O(n)
# Space Complexity: O(min(n, charset))

def lengthOfLongestSubstring(s: str) -> int:
    history = {}
    left = 0
    answer = 0

    for right in range(len(s)):
        if s[right] in history and left <= history[s[right]]:
            left = history[s[right]] + 1

        history[s[right]] = right
        answer = max(answer, right - left + 1)

    return answer


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))  # 3
    print(lengthOfLongestSubstring("bbbbb"))     # 1
    print(lengthOfLongestSubstring("pwwkew"))    # 3
