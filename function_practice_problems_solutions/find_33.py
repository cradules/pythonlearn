def has_33(nums):
   for y in range(0,len(nums)-1):
       # if nums[y] == 3 and nums[y+1] == 3:
       if nums[y:y+2] == [3, 3]:
           return True
   return False


print(has_33([1, 1, 3]))
