def unique_nums(nums):
    s=set()
    ans=[]
    for i in range (0,len(nums)) :
        if nums[i] not in s:            
            s.add(nums[i])
            ans.append(nums[i])
    return ans        