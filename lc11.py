def maxArea(height: list[int]) -> int:
    l = 0
    r = len(height) -1
    highest_area = 0
    while r > l:
        length = min(height[l],height[r])
        width = r - l
        area = length * width
        highest_area = max(highest_area,area)
        if height[l] > height[r]:
            r-=1
        elif height[l] <= height[r]:
            l+=1
    return highest_area
            
print(maxArea([1,8,100,2,100,4,8,3,7]))