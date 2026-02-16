
nums=[2,3,4,5,6,1,2,3,4,5,5,5,56,6,6,62,1,3]

frequency_map={} # or you can frequency_map=dict()
for i in range (0, len(nums)):
    if nums[i] in frequency_map:
        frequency_map[nums[i]]+=1
    else:
        frequency_map[nums[i]]=1
print(frequency_map)