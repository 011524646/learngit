import sys
def avg(nums):
    sum=0
    for i in nums:
        sum+=i
    return float(sum/len(nums))  
def highest(nums):
    ans=nums[0]
    for i in nums:
        if i>ans:
            ans=i
    return ans            
scores=[]
for tok in sys.stdin.read().split():     
    n = int(tok)
    scores.append(n)
print (avg(scores))
print (highest(scores))