nums=[2,3,4,5,6,1,2,3,4,5,5,5,56,6,6,62,1,3]
hash_map=dict()
n=len(nums)

for i in range(0, n):
    hash_map[nums[i]]=hash_map.get(nums[i], 0)+1