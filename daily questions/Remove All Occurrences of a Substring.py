class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack=[]
        n=len(part)
        for i in s:
            if i!=part[-1]:
                stack.append(i)
            else:
                stack.append(i)
                f="".join(stack[len(stack)-len(part):])
                if(f==part):
                    i=0
                    while(i<len(part)):
                             stack.pop()
                             i=i+1
                else:
                    continue

        stack="".join(stack)
        return stack