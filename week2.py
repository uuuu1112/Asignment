def calculate(min,max):
    summin=0
    summax=0
    for i in range(min):
        summin+=i
    for j in range(max+1):
        summax+=j
    return summax-summin

print(calculate(1,3))
print(calculate(4,8))

def avg(data):
    sum=0
    for x in data["employees"]:
        sum=sum+x["salary"]
    return sum/data["count"]

print(avg(
    {
        "count":3,
        "employees":[{"name":"John","salary":30000},{"name":"Bob","salary":60000},{"name":"Jenny","salary":50000}]
        }
    ))

def maxProduct(nums):
    product=[]
    for x in nums:
        for y in nums:
            if y !=x:
                product.append(x*y)
    return max(product)

print(maxProduct([5,20,2,6]))
print(maxProduct([10,-20,0,3]))

def twoSums(nums,target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i<j:
                if nums[i]+nums[j] == target:
                    return [i,j]
    
result=twoSums([2,11,7,15],9)
print(result)

def maxZeros(nums):
    nums.insert(0,1)
    nums.append(1)
    zeronumsi=[]
    zeronums=[]
    
    for i in range(len(nums)):
        if nums[i] != 0:
            zeronumsi.append(i)
    for i in range(len(zeronumsi)):
        if i>0:
            zeros=zeronumsi[i]-zeronumsi[i-1]
            zeronums.append(zeros)
    return max(zeronums)-1
    
print(maxZeros([0, 1, 0, 0]))
print(maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]))
print(maxZeros([1, 1, 1, 1, 1]))
   
