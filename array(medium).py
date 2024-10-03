from collections import Counter #for counting?
import sys  #used in setting sys.maxsize
from typing import List
from collections import defaultdict
def twoSum(arr,k):#returns yes or no
    left = 0
    right= len(arr)-1
    arr.sort()
    while left<right:
        total = arr[left] + arr[right]
        if total == k:
            return ("Yes")
        elif total < k:
            left+=1
        else:
            right-=1
    return ("No")

def twoSum2(arr,k):#returns index of the numbers
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] == k - arr[i]:
                return [i,j]

def sortZeroOneTwo(arr):#Dutch National Flag algorithm
    low=0
    mid=0
    high=len(arr)-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid] == 1:
            mid+=1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high -=1
    return arr

def majorityElement(arr):#using counter
    n = len(arr)
    counter = Counter(arr)

    for num, count in counter.items():
        if count > (n//2):
            return num
    return -1

def majorityElement2(arr):#moore's voting algorithm
    n = len(arr)
    count = 0
    element = None

    for i in range(n):
        if count ==0:
            count =1
            element = arr[i]
        elif element == arr[i]:
            count +=1
        else:
            count -=1
        
        count1 =0
        for i in range (n):
            if arr[i] == element:
                count1+=1
        if count1>(n/2):
            return element
        return -1

def maxSubarraySum(arr):#kadane's algorithm
    maxi = -sys.maxsize-1 #used initialize the samllest possible integer value in python
    sum=0
    n = len(arr)
    for i in range(n):
        sum += arr[i]

        if sum>maxi:
            maxi = sum
        if sum<0:
            sum=0

    return maxi

def maxProfit(arr):#stock buy and sell
    maxProfit = 0
    minPrice = float('inf')
    for i in range(len(arr)):
        minPrice = min(minPrice,arr[i])
        maxProfit = max(maxProfit,arr[i]-minPrice)
    return maxProfit
     
def rearrangeBySign(arr):
    n = len(arr)
    ans = [0]*n
    posIndex = 0
    negIndex = 1
    for i in range (n):
        if arr[i]<0:
            ans[negIndex] = arr[i]
            negIndex+=2
        else:
            ans[posIndex] = arr[i]
            posIndex+=2
    
    return ans

def rearrangeBySign(arr):#negetives and positive are not equal in number
    pos=[]
    neg=[]
    for i in range(len(arr)):
        if arr[i] <0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])    
    if len(pos) < len(neg):
        for i in range(len(pos)):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]

        index = len(pos) *2
        for i in range (len(neg) - len(pos)):
            arr[index] = neg[len(pos)+i]
            index+=1
    
def nextGreaterPermutation(arr):
    n = len(arr)

    ind = -1
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            ind = i
            break
    
    if ind == -1:
        arr.reverse()
        return arr
    
    for i in range(n-1,ind,-1):
        if arr[i]>arr[ind]:
            arr[i],arr[ind] = arr[ind],arr[i]
            break
    
    arr[ind+1:] = reversed(arr[ind+1:])

    return arr

def printLeaders(arr):
    n =len(arr)
    ans =[]
    max_element = arr[n-1]
    ans.append(arr[n-1])

    for i in range(n-2,-1,-1):
        if arr[i]>max_element:
            ans.append(arr[i])
            max_element = arr[i]
    ans.reverse()
    return ans

def longestSuccessiveElements(arr):
    n = len(arr)
    if n==0:
        return 0

    longest = 1
    st=set()

    for i in range(n):
        st.add(arr[i])

    for it in st:
        if it-1 not in st:
            count = 1
            x = it
            while x+1 in st:
                x+=1
                count+=1
            longest = max(longest,count)
    return longest

def zeroMatrix(matrix,n,m):
    col0 = 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] ==0:
                matrix[i][0]=0

                if j!=0:
                    matrix[0][j] =0
                else:
                    col0=0
    
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j] != 0:
                if matrix[i][0]== 0 or matrix[0][j]==0:
                    matrix[i][j]=0

    if matrix[0][0]==0:
        for j in range(m):
            matrix[0][j]=0
    if col0==0:
        for i in range(n):
            matrix[i][0]=0
    return matrix

def rotateMatrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i].reverse()

def printSpiral(mat):
    ans=[]
    n=len(mat)
    m=len(mat[0])
    top = 0
    left=0
    bottom = n-1
    right = m-1

    while (top<=bottom and left<=right):
        for i in range(left,right+1):
            ans.append(mat[top][i])
        top+=1

        for i in range(top,bottom+1):
            ans.append(mat[i][right])
        right-=1

        if(top<=bottom):
            for i in range(right,left-1,-1):
                ans.append(mat[bottom][i])
            bottom -=1
        
        if(left<=right):
            for i in range(bottom,top-1,-1):
                ans.append(mat[i][left])
            left+=1
    
    return ans

def findAllSubarraysWithGivenSum(arr,k):
    n=len(arr)
    mpp=defaultdict(int)
    preSum=0
    cnt=0

    mpp[0]=1
    for i in range(n):
        preSum+=arr[i]
        remove=preSum-k
        cnt+=mpp[remove]
        mpp[preSum]+=1
    return cnt


"""
from collections import Counter
from typing import List 
import heapq
num=list(map(int, input("Enter the elements of the array separated by space: ").split()))
"""