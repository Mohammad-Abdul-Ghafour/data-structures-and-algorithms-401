def insertion_sort(arr):
    if len(arr) == 1:
        return arr
    elif len(arr):
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
    else:
        raise ValueError("This array is empty")

if __name__ == "__main__":
    arr = [1]
    print(insertion_sort(arr))
