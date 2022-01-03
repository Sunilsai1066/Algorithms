#Using 2 Pointers
def Palindrome2Pointer(Str,L,R):
    if(L > R): return
    if(Str[L] == Str[R]): 
        return True
    else: 
        return False
    Palindrome2Pointer(Str,L+1,R-1)

#Using 1 Pointer
def Palindrome1Pointer(Str,L,N):
    if(L > (N//2)): return
    if(Str[L] == Str[N-1-L]): 
        return True
    else: 
        return False
    Palindrome1Pointer(Str,L+1,N)

Str = "MADAM"
N = len(Str)
L,R = 0,len(Str)-1
print(Palindrome2Pointer(Str,L,R))
print(Palindrome1Pointer(Str,L,N))
