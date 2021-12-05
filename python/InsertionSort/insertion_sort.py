def insertion_sort(arr):
    n = len(arr)
    for i in range(n-1):
        _min = i
        j = i + 1
        for ii in range(n):
            if arr[j] < arr[_min]:
                _min = j
            j +=1
            if j > n - 1:
                break

        temp = arr[_min]
        arr[_min] = arr[i]
        arr[i] = temp
    return arr

if __name__ == "__main__":
    arr = [2,3,5,7,13,11]
    print(insertion_sort(arr))
