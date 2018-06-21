


def quick_sort(l1, low, high):

    if low < high:
        pivot = partition(l1, low, high)
        quick_sort(l1, low, pivot-1)
        quick_sort(l1, pivot+1, high)



def partition(l1, low, high):
    pivot_item = l1[low]
    left = low
    right = high
    while left < right:
        print left, right, pivot_item
        while l1[left] <= pivot_item:
            left += 1

        while l1[right] > pivot_item:
            right -= 1

        if left < right:
            #Swap left and right
            temp = l1[left]
            l1[right] = l1[right]
            l1[right] = temp


    # Swap A[right] and A[low]
    l1[low] = l1[right]
    l1[right] = pivot_item
    return right



l1 = [2,4,1,5,8,7,9,6]
quick_sort(l1, 0, len(l1))
print l1
