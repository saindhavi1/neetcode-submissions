class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers)-1
        pt1 = numbers[index1]
        pt2 = numbers[index2]

        while (index1 < index2):
            if (pt1 + pt2 > target):
                pt2 = numbers[index2-1]
                index2 -=1
            elif (pt1 + pt2 < target):
                pt1 = numbers[index1+1]
                index1 += 1
            else:
                return [index1+1, index2+1]