def CreateSegmentTree(Arr,Queries):
    Len = len(Arr)
    Start, End = 0, Len-1
    SegTree = [-1]*(4*Len)
    def BuildSegmentTree(Root, Low, High):
        if(Low == High):
            SegTree[Root] = Arr[Low]
            return
        Mid = (Low + High)//2
        BuildSegmentTree((2*Root)+1, Low, Mid)
        BuildSegmentTree((2*Root)+2, Mid+1, High)
        SegTree[Root] = SegTree[2*Root+1] + SegTree[2*Root+2]
        
    def QueryCheck(Root, Start, End, Low, High):
        if(Start >= Low and End <= High):
            return SegTree[Root]
        elif(End < Low or High < Start):
            return 0
        Mid = (Start + End)//2
        Right = QueryCheck((2*Root)+1, Start, Mid, Low, High)
        Left = QueryCheck((2*Root)+2, Mid+1, End, Low, High)
        return Right + Left
        
    def UpdateValue(Root, Start, End, Ind, NewVal):
        if(Start == End == Ind):
            SegTree[Root] = NewVal
            return
        Mid = (Start + End)//2
        if(Ind <= Mid):
            UpdateValue((2*Root)+1, Start, Mid, Ind, NewVal)
            SegTree[Root] = SegTree[(2*Root)+1] + SegTree[(2*Root)+2]
        else:
            UpdateValue((2*Root)+2, Mid+1, End, Ind, NewVal)
            SegTree[Root] = SegTree[(2*Root)+1] + SegTree[(2*Root)+2]
        
    
    BuildSegmentTree(0, Start, End)
    #UpdateValue(0, 0, Len-1, 0,3) #Updating 0th Index Value To 3
    Res = []
    for Low, High in Queries:
        subRes = QueryCheck(0, 0, Len-1, Low, High)
        Res.append(subRes)
    return Res

Arr = [9,-8]
Queries = [(0,1),(1,1)] #(100, 70, 30, 50)
print(CreateSegmentTree(Arr, Queries))
