nums=[1, 2, 3, 4, 5, 6, 7, 8]

def rev(nums, left=0, right=None):
    if right==None:
        right=len(nums)-1
    if left>=right:
        return nums
    nums[left], nums[right] = nums[right], nums[left]
    rev(nums, left+1, right-1 )
    return nums
print(rev(nums))