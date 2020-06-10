class Solution:
    def searchInsert(self, nums, target):
        i = 0
        while i < len(nums)-1:
            if target <= nums[i]:
                return i
            elif target > nums[i] and target <= nums[i+1]:
                return i+1
            i+=1
        if target > nums[-1]:
            return len(nums)
        else:
            return len(nums)-1


answer = Solution().searchInsert([1,3,5,6],7)
print(answer)

##binary search solution
if target>nums[-1]: #if target is greater than largest element
            return len(nums)
if target<nums[0]: # if target is lesser than smallest element
    return 0

start=0
end=len(nums)-1

while(start<=end):
    mid=(start+end)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]>target: # if target is lesser than mid element search first half of nums
        end=mid-1
    else:
        start=mid+1 # else search last half of nums
return start