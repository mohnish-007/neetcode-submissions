class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        frq=[[] for _ in range(len(nums)+1)]
        for n in nums:
            count[n]=1+count.get(n,0)
        for n,c in count.items():
            frq[c].append(n)
        res=[]
        for i in range(len(frq)-1,0,-1):
            for n in frq[i]:
                res.append(n)
                if len(res)==k:
                    return res