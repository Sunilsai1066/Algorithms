class MinSegmentTree:
    
    def __init__(self, InArr):
        self.InArr = InArr
        self.SegTree = [-1]*(4*len(InArr))
        def BuildSegTree(Root, Start, End):
            if(Start == End):
                self.SegTree[Root] = self.InArr[Start]
                return 
            Mid = (Start + End)//2
            BuildSegTree((Root*2)+1, Start, Mid)
            BuildSegTree((Root*2)+2, Mid+1, End)
            self.SegTree[Root] = max(self.SegTree[(Root*2)+1], self.SegTree[(Root*2)+2])
            
        BuildSegTree(0, 0, len(InArr)-1)
        
    def RangeMaximum(self, Left, Right):
        def FindRangeMax(Root, Left, Right, Start, End):
            if(Start > Right or End < Left):
                return float('-inf')
            elif(Start >= Left and End <= Right):
                return self.SegTree[Root]
            Mid = (Start + End)//2
            LVal = FindRangeMax((Root*2)+1, Left, Right, Start, Mid)
            RVal = FindRangeMax((Root*2)+2, Left, Right, Mid+1, End)
            return max(LVal, RVal)
            
        return FindRangeMax(0, Left, Right, 0, len(self.InArr)-1)
        
    
    def UpdateIndex(self, Ind, Val):
        def UpdateSegTree(Root, Start, End, Ind, Val):
            if(Start == End):
                self.SegTree[Root] = Val
                return
            Mid = (Start + End)//2
            if(Ind <= Mid):
                UpdateSegTree((Root*2)+1, Start, Mid, Ind, Val)
            else:
                UpdateSegTree((Root*2)+2, Mid+1, End, Ind, Val)
            self.SegTree[Root] = max(self.SegTree[(Root*2)+1], self.SegTree[(Root*2)+2])
        UpdateSegTree(0, 0, len(self.InArr)-1, Ind, Val)
        
    
#Arr = [1,3,2,6,7,9,0,2,3,7]
Arr = [7,3,9,0,1]
Obj = MinSegmentTree(Arr)
print(Obj.SegTree)
print(Obj.RangeMinimum(0, 3))
print(Obj.RangeMinimum(0, 2))
Obj.UpdateIndex(3, 10)
print(Obj.SegTree)
print(Obj.RangeMinimum(0, 3))
print(Obj.RangeMinimum(0, 2))
