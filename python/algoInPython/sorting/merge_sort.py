l2 = [2,4,1,5,8,7,9,6]

def mergeSort(l1, start, end):
    print start, end
    #divide
    if end > start:
        mid = (start + end)/2
        mergeSort(l1, start, mid)
        mergeSort(l1, mid+1, end)
        merge(l1, l2, start, mid, end)


def merge(l1, l2, start, mid, end):
    temp_ind = start
    right_start = mid+1
    size = end-start+1

    while start <= mid and right_start <= end:
        if l1[start] <= l1[right_start]:
            l2[temp_ind] = l1[start]
            temp_ind += 1
            start += 1
        else:
            l2[temp_ind] = l1[right_start]
            temp_ind += 1
            right_start += 1

    while start <= mid:
        l2[temp_ind] = l1[start]
        temp_ind += 1
        start += 1

    while right_start <= end:
        l2[temp_ind] = l1[right_start]
        temp_ind += 1
        right_start += 1

    for index in range(size):
        l1[end] = l2[end]
        end = end - 1



l1 = [2,4,1,5,8,7,9,6]
mergeSort(l1,0,len(l1)-1)
print l1
