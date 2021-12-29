#Using 2 Pointers
def ArrayReverse2Pointer(Arr,L,R):
    if(L > R): return
    Arr[L],Arr[R] = Arr[R],Arr[L]
    ArrayReverse2Pointer(Arr,L+1,R-1)

#Using 1 Pointer
def ArrayReverse1Pointer(Arr,L,N):
    if(L > (N//2)): return
    Arr[L],Arr[N-L-1] = Arr[N-L-1],Arr[L]
    ArrayReverse1Pointer(Arr,L+1,N)


Arr = [1,2,3,4,5,6,7,8,9]
N = len(Arr)
L,R = 0,len(Arr)-1
#ArrayReverse2Pointer(Arr,L,R)
ArrayReverse1Pointer(Arr,L,N)
print(Arr)
