class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        arr=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res=[]
        if digits=="":
            return []
        def backtrack(digits,output,k,index):
            if len(output)==k:
                res.append(output)
                return
            key=arr[int(digits[index])]
            for i in range(len(key)):
                  backtrack(digits,output+key[i],k,index+1)
        backtrack(digits,"",len(digits),0)
        return res
            
        