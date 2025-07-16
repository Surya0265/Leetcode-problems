def find(s,k):
    stack=[]
    for i,c in enumerate(s):
        while stack and stack[-1]>c and len(stack)+(len(s)-i)>k:
             stack.pop()
        if len(stack)<k:
           stack.append(c)
    return "".join(stack)
print(find("adbcd",3))
