class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count=0
        sum1=0
        sum2=0
        for i in range(low,high+1):
             if len(str(i))%2==1:
                continue
             else:
                  string=str(i)
                  sum1=sum(list(int(x) for x in string[0:len(string)/2]))
                  sum2=sum(list(int(x) for x in string[len(string)/2:]))
                  if(sum1==sum2):
                    count=count+1
                  sum1=0
                  sum2=0
        return count

        