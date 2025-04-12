class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)):
              while stack and temperatures[stack[-1]]<temperatures[i]:
                      pind=stack.pop()
                      answer[pind]=i-pind
              stack.append(i)
        return answer
