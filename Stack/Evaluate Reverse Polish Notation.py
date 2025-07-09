class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      stack=[]
      arr=tokens
      for i in range(len(arr)):
          if arr[i]=='+':
              a=stack.pop()
              b=stack.pop()
              stack.append(a+b)
          elif arr[i]=='-':
              a=stack.pop()
              b=stack.pop()
              stack.append(b-a)
          elif arr[i]=='*':
              a=stack.pop()
              b=stack.pop()
              stack.append(a*b)
          elif arr[i]=='/':
              a=stack.pop()
              b=stack.pop()
              stack.append(int(b/a))
          else:
              stack.append(int(arr[i]))
      return stack[-1]
        