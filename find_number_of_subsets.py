def subsets(num):
    l = len(num)
    sbsets = []
    nOfSubsets = 2**l 
    for i in range(nOfSubsets):
        subset = []
        for j in range(l):
            if i & (2**j) != 0:
                subset.append(num[j])
        sbsets.append(subset)
    return sbsets


num = "123"
ans = subsets(num)
print(ans)