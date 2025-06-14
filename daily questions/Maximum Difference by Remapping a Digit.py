class Solution:
    def minMaxDifference(self, num: int) -> int:
        string=list(str(num))
        for i in range(len(string)):
            if string[i]!='9':
                     break
        j=string[i]
        for i in range(len(string)):
                if string[i]==j:
                    string[i]=9
        maxi="".join(str(x) for x in string)
        stri=list(str(num))
        for i in range(len(stri)):
            if stri[i]!='0':
                     break
        j=stri[i]
        for i in range(len(stri)):
                if stri[i]==j:
                    stri[i]=0
        mini="".join(str(x) for x in stri)
        return int(maxi)-int(mini)
        


              
        