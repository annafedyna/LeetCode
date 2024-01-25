def subsets(arr):
    res = []
    n = len(arr)
    for i in range(2**n):
        sub = []
        for j in range(n):
            if i & (1 << j) !=0:
                sub.append(arr[j])
        res.append(sub)
    return res

print(subsets([1,2,3]))