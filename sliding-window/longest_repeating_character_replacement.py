# Problem: Longest Repeating Character Replacement
# Topic: Sliding Window
#
# Key Idea:
# Maintain a sliding window where the number of characters to replace
# does not exceed k.
#
# Approach:
# - Use a hash map to count character frequencies in the current window.
# - Track the highest frequency character in the window.
# - If the number of replacements needed exceeds k, shrink the window
#   from the left.
# - Track the maximum valid window length.
#
# Time Complexity: O(n)
# Space Complexity: O(1)  # or O(charset)

def longestRepeatingCharacterReplacement(s: str, k: int) -> int:
    history = {}
    max_freq = 0
    left = 0
    answer = 0

    for right in range(len(s)):
        history[s[right]] = history.get(s[right], 0) + 1
        max_freq = max(max_freq, history[s[right]])

        while (right - left + 1) - max_freq > k:
            history[s[left]] -= 1
            left += 1

        answer = max(answer, right - left + 1)

    return answer


if __name__ == "__main__":
    print(longestRepeatingCharacterReplacement("ABAB", 2))     # 4
    print(longestRepeatingCharacterReplacement("AABABBA", 1))  # 4
    print(longestRepeatingCharacterReplacement("AAAAA", 1))    # 5
