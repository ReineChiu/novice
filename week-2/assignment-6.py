#要求六：
def maxZeros(nums):
    maxcount = 0 #目前最長連續數 的個數
    count = 0 #目前連續 個數
    for i in nums:
        if i == 0:
            count = count+1
            maxcount = max(maxcount,count)#max(,)先把兩數做最大值比較
        else:
            count = 0 #此0代表遇到i!=0時 重新計算
    print(maxcount)


maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4 
maxZeros([1, 1, 1, 1, 1]) # 得到 0 
maxZeros([0, 0, 0, 1, 1]) # 得到 3