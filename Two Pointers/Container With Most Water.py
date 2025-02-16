class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        start=0
        end=len(height)-1
        while(start<end):
             width=end-start
             if(height[start]<height[end]):
                min_height=height[start]
             else:
                min_height=height[end]
             area=width*min_height
             if(max_area<area):
                  max_area=area

             if(height[start]<height[end]):
                     start+=1
             else:
                end-=1
        return max_area
        