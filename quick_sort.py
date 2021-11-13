def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    print('Original Array ', arr)

    pivot = arr[len(arr) // 2]
    print('pivot ' ,pivot)

    left = [x for x in arr if x < pivot]
    print('left ', left)

    middle =  pivot
    print('middle ',middle)

    right = [x for x in arr if x > pivot]
    print('right ', right)

    return quick_sort(left) + [middle] + quick_sort(right)

array = [2,54,6,224,56,78,90,0,23,10,40,95,9,17,13]
print(quick_sort(array))
