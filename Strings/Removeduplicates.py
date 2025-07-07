freq=[0]*256
s=input()
res=[]
for i in s:
    if freq[ord(i)]==0:
        res.append(i)
        freq[ord(i)]+=1
    else:
        freq[ord(i)]+=1
result=''.join(res)
print(result)