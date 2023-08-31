def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1 
        else: 
            result.append(right[j])
            j += 1 

    result.extend(left[i:])
    result.extend(right[j:])

    return result 

def mergeSort(mylist):
    # base condition : single element lists are already sorted! 
    if (len(mylist) <= 1): 
        return mylist 
    
    # divide the list into two parts
    mid = len(mylist) // 2   
    left = mylist[:mid]
    right = mylist[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    result = merge(left, right)
    return result 

mylist = [5, 6, 11, 3, 15, 2]
result = mergeSort(mylist)

print(result)
