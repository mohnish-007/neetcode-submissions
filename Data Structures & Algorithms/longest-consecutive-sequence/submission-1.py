class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a=set(nums)
        longest=0
        count=0
        small=float("-inf")
        for num in a:
            if num-1 in a:
                continue
            elif num-1 not in a:
                count=1
                small=num
                while small+1 in a:
                    count+=1
                    small+=1
            longest=max(longest,count)
        return longest