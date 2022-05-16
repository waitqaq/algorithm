def quick_sort(alist, start, end):
    if start > end:
        return
    pivot = alist[end]
    low = start
    high = end
    while low < high:
        while low < high and alist[low] <= alist[high]:
            low += 1
        alist[high] = alist[low]

        while low < high and alist[low] > alist[high]:
            high -= 1
        alist[low] = alist[high]
    alist[low] = pivot
    quick_sort(alist, low+1, high)
    quick_sort(alist, low, high-1)

quick_sort([3,4,2,3], 0, 3)