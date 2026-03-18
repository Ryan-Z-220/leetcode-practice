# Problem: Valid Anagram
# Topic: HashMap
#
# Key Idea:
# Use a hash map to count character frequencies and cancel them out.
#
# Approach:
# - If lengths are different, return False immediately.
# - Count the frequency of each character in the first string.
# - Traverse the second string and decrement the counts.
# - If a character is missing or overused, return False.
# - If all counts return to zero, the strings are anagrams.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import Dict


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count: Dict[str, int] = {}

    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for ch in t:
        if count.get(ch, 0) == 0:
            return False

        count[ch] -= 1

        if count[ch] == 0:
            del count[ch]

    return len(count) == 0


if __name__ == "__main__":
    print(isAnagram("anagram", "nagaram"))  # True
    print(isAnagram("rat", "car"))          # False
