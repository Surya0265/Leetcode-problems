s=input()
count=[0]*26
for i in range(len(s)):
       count[ord(s[i])-ord('A')]+=1
for i in range(25):
       pairs=count[i]//2
       count[i]=count[i]%2
       count[i+1]+=pairs
res=''
for i in range(26):
       res+=chr(ord('A')+i)*count[i]
       
print(res)