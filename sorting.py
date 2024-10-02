def selection_sort(arr): #selecting the smallest and putting it infront
    n = len(arr)
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if arr[j] < arr[mini]:
                mini = j
        arr[mini], arr[i] = arr[i], arr[mini]

    for i in arr:
        print(i, end=' ')
    print()

def bubble_sort(arr): #selecting the biggest and putting it in back
    n = len(arr)
    for i in range (n-1,-1,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j+1] , arr[j] = arr[j], arr[j+1]
    
    for num in arr:
        print(num,end=' ')
    print()

def insertion_sort(arr): #selecting the shortest element in a small range
    n=len(arr)
    for i in range(n):
        j = i
        while j>0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j],arr[j-1]
            j -= 1
    for i in range (n):
        print(arr[i],end=' ')
    print()

#break the array into equal parts then sort them and combine them
def merge(arr, low, mid, high):
    temp = []  # temporary list
    left = low  # starting index of the left half of the array
    right = mid + 1  # starting index of the right half of the array

    # storing elements in the temporary list in a sorted manner
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # if elements on the left half are still left
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # if elements on the right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1

    # transferring all elements from the temporary list back to the original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)  # left half
    merge_sort(arr, mid + 1, high)  # right half
    merge(arr, low, mid, high)  # merging sorted halves

# Test the function
if __name__ == "__main__":
    arr = [9, 4, 7, 6, 3, 1, 5]
    n = len(arr)

    print("Before Sorting Array:")
    print(arr)

    merge_sort(arr, 0, n - 1)

    print("After Sorting Array:")
    print(arr)

#pick any element as pivot, compare elements to pivot and place left or right
def partition(arr,low,high):
    pivot = arr[low]
    i=low
    j=high

    while i<j:
        while i<=high-1 and arr[i] <=pivot:
            i+=1
        while j>=low+1 and arr[j]>pivot:
            j-=1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

def qs(arr,low,high):
    if low<high:
        p_index=partition(arr,low,high)
        qs(arr,low,p_index-1)
        qs(arr,p_index+1,high)

def quick_sort(arr):
    qs(arr,0,len(arr)-1)
    return arr

#running
arr = [4, 6, 2, 5, 7, 9, 1, 3]
sorted = quick_sort(arr)
print(sorted)
