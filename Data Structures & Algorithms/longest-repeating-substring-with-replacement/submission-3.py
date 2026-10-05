class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        max_freq = 0
        answer = 0

        for right, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            max_freq = max(max_freq, counts[char])

            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer