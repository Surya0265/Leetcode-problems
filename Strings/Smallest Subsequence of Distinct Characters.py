class Solution:
    def smallestSubsequence(self, s: str) -> str:
        check={c:i for i,c in enumerate(s)}
        stack=[]
        seen=set()
        for i ,c in enumerate(s):
              if c in seen:
                continue
              while(stack and c<stack[-1] and check[stack[-1]]>i):
                 seen.remove(stack.pop())
              seen.add(c)
              stack.append(c)
        result=''.join(stack)
        return result