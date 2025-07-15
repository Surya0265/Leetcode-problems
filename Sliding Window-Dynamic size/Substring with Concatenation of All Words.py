class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        count={}
        total=len(words[0])*len(words)
        eno=len(words[0])
        length=len(words)
        ans=[]
        for word in words:
              if word not in count:
                count[word]=1
              else:
                count[word]+=1
        for i in range(len(s)-total+1):
            seen={}
            for j in range(length):
                word=s[i+j*eno:i+(j+1)*eno]
                seen[word]=seen.get(word,0)+1
                if word in count:
                   if seen[word]>count[word]:
                     break
                else:
                    break
            else:
                ans.append(i)
        return ans
                

               
        