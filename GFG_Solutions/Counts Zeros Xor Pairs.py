from collections import Counter
def calculate (arr, n) : 
    Res = 0
    Count = Counter(arr)
    for K,V in Count.items():
        if(V >= 2):
            Res += (V*(V-1))//2
    return Res
