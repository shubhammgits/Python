nums = [3,4,2,6,7,10,7,98,43,27]
start = 0
end = len(nums) - 1
largest = 0

while start < end:
    if(nums[start] > nums[end]):
        largest = nums[start]
    else:
        start += 1
        end -= 1
        
    
print("Largest = ", largest)