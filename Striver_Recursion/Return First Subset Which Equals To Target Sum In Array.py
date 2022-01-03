def GenerateSubSetCheckTarget(Ind,Arr,Res,N,SumVar,target):
    if(Ind >= N):
        if(SumVar == target): 
            print(Res)
            return True
        else:
            return False
    Res.append(Arr[Ind])
    if(GenerateSubSetCheckTarget(Ind+1,Arr,Res,N,SumVar+Arr[Ind],target) == True): return True
    Res.pop()
    if(GenerateSubSetCheckTarget(Ind+1,Arr,Res,N,SumVar,target) == True):return True
    return False

Arr = [1,2,1]
FinRes = []
target = 1
N = len(Arr)
GenerateSubSetCheckTarget(0,Arr,[],N,0,target)
