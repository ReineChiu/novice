#要求一：函式與流程控制
def calculate(min,max,step):
    sum=0
    n=min
    for n in range(min,max+1,step):
        sum=sum+n
    print(sum)

calculate(1,3,1)
calculate(4,8,2)
calculate(-1,2,2)

#要求二：python字典與列表
def avg(data):
    for value in data:
        ini_dic=data[value] #>>>  印出employees對應的值[{},{},{},{}]
        count=0 
        total=0
        for d in ini_dic:               
            if d.get("manager")==False:
                count=count+1
                total=total+d.get("salary")
                avg=total/count
        print(avg)     

avg({"employees":[{"name":"Jhon","salary":30000,"manager":False},
            {"name":"Bob","salary":60000,"manager":True},
            {"name":"Jenny","salary":50000,"manager":False},
            {"name":"Tony","salary":40000,"manager":False}]})

#要求三：
def func(a):
    def mul(num1,num2):
        return a+(num1*num2)
    return mul

result=func(2)(3, 4) 
result1=func(5)(1, -5)
result2=func(-3)(2, 9)
print(result)
print(result1)
print(result2)

func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14 
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0 
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15 
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

#要求四：
def maxProduct(nums):
    x= len(nums)
    newlist = [ ] 
    for i in range(x):        
        for j in range(i+1,x):
            if nums[i]==nums[j]:
                continue
            mul=(nums[i]*nums[j])
            newlist.append(mul)
    print(max(newlist))


maxProduct([5, 20, 2, 6]) # 得到 120 
maxProduct([10, -20, 0, 3]) # 得到 30 
maxProduct([10, -20, 0, -3]) # 得到 60 
maxProduct([-1, 2]) # 得到 -2 
maxProduct([-1, 0, 2]) # 得到 0 
maxProduct([5,-1, -2, 0]) # 得到 2 
maxProduct([-5, -2]) # 得到 10

#要求五：
def twoSum(nums, target):
    x = len(nums)
    
    for i in range(x):
        for j in range(i+1,x):
           if nums[i]+nums[j] == target:
                return [i,j]  

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9