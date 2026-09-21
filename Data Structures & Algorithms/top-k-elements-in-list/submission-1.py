class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}

        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1
        answer = []
        while k > 0:
            best = 0
            bestKey = 0
            for key, val in freqDict.items():
                if val > best and key not in answer:
                    bestKey = key
                    best = val
            answer.append(bestKey)
            k-=1
        return answer


        
