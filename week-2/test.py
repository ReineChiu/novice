#要求六：
#def maxZeros(nums):
#    total_num = [ ] 
#    length = len(nums) #length=4
##    count = 1              #?列表中只有0、1 所以一開始設變數count=1
#    count = 0
#    for i in range(length - 1):  
#        if nums[i]==0 and nums[i+1]==0 and nums[i] == nums[i+1]:
#            count += 1
        
##        elif nums[i]!=0 and nums[i+1]!=0: #此路不通
##            count -= 1                    #此路不通

##        if nums[i] == nums[i+1]: #前一位的數跟下一位的數做比較
##            count += 1           #若前後位數(連續)相等,count+1,即有幾個連續數
#        else: 
#            total_num.append(count) 
##            count = 1 
#            print(total_num)
##    print(count)
##    print(total_num)

# 請用你的程式補完這個函式的區塊 
#maxZeros([0, 1, 0, 0]) # 得到 2
#maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4 
#maxZeros([1, 1, 1, 1, 1]) # 得到 0 
#maxZeros([0, 0, 0, 1, 1]) # 得到 3



def maxZeros(nums):
    maxcount = 0 #目前最長連續數 的個數
    count = 0 #目前連續 個數
    for i in nums:
        if i == 0:
            count = count+1
            maxcount = max(maxcount,count)#max(,)先把兩數做最大值比較
        else:
            count = 0 #此0代表遇到i!=0時 重新計算
#        print(count)
#        print(maxcount)
    print(maxcount)


#maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4 
#maxZeros([1, 1, 1, 1, 1]) # 得到 0 
#maxZeros([0, 0, 0, 1, 1]) # 得到 3




#List=[1,2,2,2,2,3,3,3,4,4,4,4,2,2]
#a = {}
#for i in List:
#    if List.count(i)>1:
#        a[i] = List.count(i)
#print (a)
#此法計算列表中重複出現的數 有幾次
#沒有計算連續性

