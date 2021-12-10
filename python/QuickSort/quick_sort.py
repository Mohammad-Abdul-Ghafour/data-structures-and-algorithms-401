[8,4,23,42,16,15]
def quick_sort(arr ,left, right):
    if len(arr)==1:
        return arr
    elif len(arr) > 1:
        if left < right:
            p = partition(arr , left , right)
            quick_sort(arr , left , p - 1)
            quick_sort(arr , p + 1 , right)
    else:
        raise ValueError("This Array Is Empty")
    return arr

def partition(arr, left, right):
    pivot = arr[right]
    low = left - 1
    for i in range(left,right):
        if arr[i] <= pivot:
            low+=1
            swap(arr,i,low)
    swap(arr,right,low+1)
    return low + 1

          
def swap(arr,i,low):
    temp = arr[i]
    arr[i]=arr[low]
    arr[low]=temp

if __name__ == "__main__":
    arr = [8,4,23,42,16,15]
    print(quick_sort(arr,0,len(arr)-1))