def GenerateSubSet(Ind,Arr,Res,N):
    if(Ind >= N):
        print(Res)
        return
    Res.append(Arr[Ind])
    GenerateSubSet(Ind+1,Arr,Res,N)
    Res.pop()
    GenerateSubSet(Ind+1,Arr,Res,N)


Arr = [3,1,2] 
N = len(Arr)
GenerateSubSet(0,Arr,[],N)
