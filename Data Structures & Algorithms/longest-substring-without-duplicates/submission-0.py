class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        longest = 0

        for right, char in enumerate(s):
            # Shrink until the previous occurrence is removed.
            while char in seen:
                seen.remove(s[left])
                left += 1

            seen.add(char)
            longest = max(longest, right - left + 1)

        return longest