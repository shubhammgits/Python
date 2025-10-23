nums = [4,3,-2,5,-1,4,-4,9,-10,0,-3,0,2,-100,-4,-5]
poslist = []
neglist = []
for i in range(len(nums)):
    if(nums[i] >= 0):
        poslist.append(nums[i])
    else:
        neglist.append(nums[i])
    
print(f'Negative Elements = {neglist}')
print(f'Positive Elements = {poslist}')
        
