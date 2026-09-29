class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        answer = []

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        while (k > 0):
            maxNum = 0
            maxKey = 0
            for key in freq:
                if freq[key] > maxNum:
                    maxNum = freq[key]
                    maxKey = key
            answer.append(maxKey)
            del freq[maxKey]
            k-=1

        return answer
