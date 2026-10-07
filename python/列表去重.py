def unique_nums(nums):
    s=set()
    ans=[]
    for i in range (0,len(nums)) :
        if nums[i] not in s:            
            s.add(nums[i])
            ans.append(nums[i])
    return ans        
def unique_nums2(nums):
    nums2= dict.fromkeys(nums,)
    return list(nums2)
nums1=[1,1,2,3,1,3,4,6,1,4,4,2,3,6,6]
print(unique_nums(nums1)==unique_nums2(nums1))