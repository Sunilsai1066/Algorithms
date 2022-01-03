def RecursiveCombinationSum(Ind,Arr,SubRes,ResultArr):
    ResultArr.append(SubRes.copy())
    for i in range(Ind,len(Arr)):
        if(i > Ind and Arr[i] == Arr[i-1]):continue
        SubRes.append(Arr[i])
        RecursiveCombinationSum(i+1,Arr,SubRes,ResultArr)
        SubRes.pop()

def RecursiveCombinationSumAll(Ind,Arr,SubRes,ResultArr):
    if(Ind == len(Arr)):
        ResultArr.append(SubRes.copy())
        return
    SubRes.append(Arr[Ind])
    RecursiveCombinationSumAll(Ind+1,Arr,SubRes,ResultArr)
    SubRes.pop()
    RecursiveCombinationSumAll(Ind+1,Arr,SubRes,ResultArr)
        
Arr = [1,2,2]
ResultArr = []
RecursiveCombinationSum(0,Arr,[],ResultArr)
ReslArr = []
RecursiveCombinationSumAll(0,Arr,[],ReslArr)
print(ResultArr)
print(ReslArr)
