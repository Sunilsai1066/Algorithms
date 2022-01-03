def RecursiveCombinationSum(Ind,Arr,Sum,ResultArr):
    if(Ind >= len(Arr)):
        ResultArr.append(Sum)
        return
    RecursiveCombinationSum(Ind+1,Arr,Sum+Arr[Ind],ResultArr)
    RecursiveCombinationSum(Ind+1,Arr,Sum,ResultArr)

Arr = [3,1,7,8,9,10]
ResultArr = []
RecursiveCombinationSum(0,Arr,0,ResultArr)
ResultArr.sort()
print(ResultArr)
