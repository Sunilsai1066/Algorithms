class SegmentTree:
    
    def __init__(self, nums):
        self.nums = nums
        self.SegTree = [-1]*(len(self.nums)*4)
        def BuildSegTree(Ind, Start, End):
            if(Start == End):
                self.SegTree[Ind] = self.nums[Start]
                return
            Mid = (Start + End)//2
            BuildSegTree((Ind*2)+1, Start, Mid)
            BuildSegTree((Ind*2)+2, Mid+1, End)
            self.SegTree[Ind] = self.SegTree[(Ind*2)+1] + self.SegTree[(Ind*2)+2]
        BuildSegTree(0, 0, len(self.nums)-1)
        
    def RangeSum(self, Left, Right):
        def CalculateSum(Root, Start, End, Left, Right):
            if(Start >= Left and End <= Right):
                return self.SegTree[Root]
            elif(End < Left or Right < Start):
                return 0
            Mid = (Start + End)//2
            Sum1 = CalculateSum((Root*2)+1, Start, Mid, Left, Right) 
            Sum2 = CalculateSum((Root*2)+2, Mid+1, End, Left, Right)
            return Sum1 + Sum2
                
        return CalculateSum(0, 0, len(self.nums)-1, Left, Right)
        
    def UpdatePoint(self, Ind, Val):
        def SegPointUpdate(Root, Start, End, Ind, Val):
            if(Start == End):
                self.SegTree[Root] = Val
                return
            Mid = (Start + End)//2
            if(Ind <= Mid):
                SegPointUpdate((Root*2)+1, Start, Mid, Ind, Val)
            else:
                SegPointUpdate((Root*2)+2, Mid+1, End, Ind, Val)
            self.SegTree[Root] = self.SegTree[(Root*2)+1] + self.SegTree[(Root*2)+2]
        SegPointUpdate(0, 0, len(self.nums)-1, Ind, Val)
        
        
        
nums = [10, 20, 30, 40]
Obj = SegmentTree(nums)
print(Obj.SegTree)
print(Obj.RangeSum(0,2))
print(Obj.RangeSum(0,3))
Obj.UpdatePoint(1,30)
print(Obj.SegTree)