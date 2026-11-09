class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        longest_seq = 1
        curr_seq = 1
        print(sort_nums)
        
        if len(nums) == 0:
            return 0

        for i in range(len(sort_nums)-1):
            
            if sort_nums[i+1] == sort_nums[i] + 1:
                curr_seq += 1
            elif sort_nums[i+1] == sort_nums[i]:
                continue
            else:
                curr_seq = 1
            if curr_seq > longest_seq:
                longest_seq = curr_seq
            
        return longest_seq

        