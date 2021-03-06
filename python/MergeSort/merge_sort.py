def mergeSort(arr):
    if len(arr)==1:
        return arr
    elif len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        merge(L,R,arr)
    else:
        raise ValueError("This Array Is Empty")
    return arr

def merge(L,R,arr):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
  
  
  
if __name__ == '__main__':
    arr = [8,4,23,42,16,15]
    print(mergeSort(arr))
  