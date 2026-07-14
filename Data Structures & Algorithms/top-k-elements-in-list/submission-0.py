class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        solution = []

        for item, count in freq.most_common(k):
            solution.append(item)

        return solution
        

    
        