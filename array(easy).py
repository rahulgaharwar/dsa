def largest_element(arr):
    #can be done using sort()
    largest = arr[0]
    n = len(arr)
    for i in range (n):
        if arr[i]>largest:
            largest = arr[i]
    return largest

def second_largest(arr):
    largest = arr[0]
    slargest = -1
    n = len(arr)
    for i in range (n):
        if arr[i] > largest:
            slargest = largest
            largest = arr[i]
        elif arr[i] <largest and arr[i]>slargest:
            slargest = arr[i]
    return slargest

def second_smallest(arr):
    smallest = arr[0]
    ssmallest = 1000
    n = len(arr)
    for i in range (n):
        if arr[i]<smallest:
            ssmallest = smallest
            smallest = arr[i]
        elif arr[i]> smallest and arr[i]<ssmallest:
            ssmallest=arr[i]
    return ssmallest

def is_sorted(arr):
    n=len(arr)
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True

def remove_dupli(arr):#from sorted array
    j = 1
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            arr[j] = arr[i]
            j+=1
    return j

#by reversing method we can perform rotation
def reverse(arr,start,end):
    while start <= end:
        arr[start],arr[end] = arr[end],arr[start]
        start +=1
        end -=1

def rotate_left(arr,n,k):
    k =k%n
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)

def rotate_right(arr,n,k):
    k=k%n
    reverse(arr,0,n-k-1)
    reverse(arr,n-k,n-1)
    reverse(arr,0,n-1)

def move_zeros(arr):
    j = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            j =i
            break
    
    if j == -1:
        return arr
    
    for i in range(j+1,len(arr)):
        if arr[i] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
    return arr

def linear_search(arr,k):
    for i in range(len(arr)):
        if arr[i]== k:
            return True
    return False

def union(arr1,arr2):
    i,j=0,0
    union = []

    while i <len(arr1) and j<len(arr2):
        if arr1[i] <= arr2[j]:
            if len(union)==0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
        else:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j+=1
    
    while i<len(arr1):
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i+=1
    
    while j<len(arr2):
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j+=1
    return union

def intersection(arr1,arr2):
    i,j=0,0
    intersec=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr1[i]:
            j+=1
        else:
            intersec.append(arr1[i])
            i+=1
            j+=1
    return intersec

def missingNumber1(n, arr):#sum approach(have to use long datatype for big value)
        sum1 = sum(arr)
        sum2 = (n*(n+1))//2
        ans = sum2 - sum1
        return ans

def missingNumber2(n,arr):#xor method
    
    xor1 = 0
    xor2 = 0

    for i in range(n-1):
        xor2 = xor2 ^ arr[i]
        xor1 = xor1 ^ (i+1)
    
    xor1 = xor1 ^ n

    return xor1 ^ xor2

def maxConsecutiveOnes(arr):
    maxi=0
    count=0
    for i in range(len(arr)):
        if arr[i] == 1:
            count +=1
            maxi = max(maxi,count)
        else:
            count = 0

    return maxi

def singleNumberInArrayOfDoubles(arr):
    xorr = 0
    for i in range(len(arr)):
        xorr = xorr^arr[i]
    return xorr

def longestSubarrayWithSumK(arr,k):
    n = len(arr)
    left,right=0,0
    summ = arr[0]
    maxLen = 0
    while right <n:
        while left <= right and summ>k:
            summ -= arr[left]
            left+=1

        if summ == k:
            maxLen = max(maxLen,right-left+1)
        
        right +=1
        if right <n:
            summ +=arr[right]
    return maxLen

        
