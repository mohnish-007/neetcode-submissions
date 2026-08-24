class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        opene=['(','{','[']
        for i in s:
            if i in opene:
                stack.append(i)
                
            else:
                if len(stack)==0:
                    return False
                a=stack.pop()
                if i==')' and a!='(':
                    return False
                
                if i=='}' and a!='{':
                    return False
                
                if i==']' and a!="[":
                    return False
                
        return len(stack)==0