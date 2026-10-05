class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        answer = 0

        for right, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1

            # Shrink while the window needs too many replacements.
            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer