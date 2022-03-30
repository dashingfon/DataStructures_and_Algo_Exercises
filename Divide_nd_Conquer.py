'''
Divide and Conquer ALgorithm

implementation of quicksort and mergesort
'''

nums = [
    3,
    5,
    2,
    6,
    2,
    8,
    4,
    6,
    7
]

def quickSort(lst):
    if len(lst) < 2:
        return lst
    else:
        nlst = lst[1:]
        pivot = lst[0]

        less = [i for i in nlst if i <= pivot]
        more = [i for i in nlst if i > pivot]
        
        return quickSort(less) + [pivot] + quickSort(more)

def mergeSort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        L = lst[:mid]
        R = lst[mid:]
        
        L = mergeSort(L)
        R = mergeSort(R)

        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j] 
                j += 1
            
            k += 1
        
        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1

        return lst
        
    else:
        return lst


print(quickSort(nums))
print(mergeSort(nums))