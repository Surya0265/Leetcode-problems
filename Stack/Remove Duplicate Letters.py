class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        count={}
        stack=[]
        instack={}
        for ch in s:
            if ch not in count:
                  count[ch]=1
            else:
                count[ch]+=1
        for ch in s:
            count[ch]-=1
            if ch in  instack and  instack[ch]:
                continue
            while stack and ch<stack[-1] and count[stack[-1]]>0:
                rchar=stack.pop()
                instack[rchar]=False
            stack.append(ch)
            instack[ch]=True

        stack="".join(stack)
        return stack