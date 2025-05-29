class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ans1 = []
        ans2 = []
        for i in s:
            if i != "#":
                ans1.append(i)
            else:
                if ans1:
                    ans1.pop()
        for i in t:
            if i != "#":
                ans2.append(i)
            else:
                if ans2:
                    ans2.pop()
        ans1 = "".join(ans1)
        ans2 = "".join(ans2)
        if ans1 == ans2:
            return True
        return False
