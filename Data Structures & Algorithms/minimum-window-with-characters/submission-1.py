class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count={}
        window={}
        for i in t:
            count[i]=1+ count.get(i,0)
        res=[-1,-1]
        lenR=float('infinity')
        l=0
        have=0
        need=len(count)
        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r],0)
            if s[r] in count and window[s[r]]==count[s[r]]:
                have+=1
            while have==need:
                if (r-l+1)<lenR:
                    res=[l,r]
                    lenR=(r-l+1)
                window[s[l]]-=1
                if s[l] in count and window[s[l]]<count[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if lenR!=float('infinity') else ""