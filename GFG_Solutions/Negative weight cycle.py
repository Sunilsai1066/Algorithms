#https://practice.geeksforgeeks.org/problems/negative-weight-cycle3504/1#
class Solution:
    def NegativeWtCycle(self,edges,NegCycleArr):
        for In,Out,Wt in edges:
            if((NegCycleArr[In]+Wt) < NegCycleArr[Out]):
                NegCycleArr[Out] = NegCycleArr[In]+Wt
        return NegCycleArr

    def CheckDistances(self,Dist,CycleDist):
        Len = len(Dist)
        for i in range(Len):
            if(Dist[i] != CycleDist[i]):
                return 1
        return 0

	def isNegativeWeightCycle(self, n, edges):
		DistArr = [float('inf')]*n
        DistArr[0] = 0
        for i in range(n-1):
            for In,Out,Wt in edges:
                if((DistArr[In]+Wt) < DistArr[Out]):
                    DistArr[Out] = DistArr[In]+Wt
        NegCycleArr = self.NegativeWtCycle(edges,DistArr[:])
        return self.CheckDistances(DistArr,NegCycleArr)

