def print_name(n):
    def rec(i,n):
        if i>=n:
            return
        print("raj")
        rec(i+1,n)
    rec(0,n)
def natural_num(n):
    def rec(i,n):
        if i>n:
            return
        print(i)
        rec(i+1,n)
    rec(1,n)
def reverse_num(n):
    def rec(i,n):
        if i<1:
            return
        print(i)
        rec(i-1,n)
    rec(n,n)
def num_backtrack(n):
    def rec(i,n):
        if i<1:
            return
        rec(i-1,n)
        print(i)
    rec(n,n)
def rev_backtrack(n):
    def rec(i,n):
        if i>n:
            return
        rec(i+1,n)
        print(i)
    rec(0,n)
def sum_of_nums(n): 
    def rec(n):
        if n == 0:
            return 0
        return n + rec(n-1)
    return rec(n)
def fact(n):
    def rec(n):
        if n ==1:
            return 1
        return n * rec(n-1)
    return rec(n)
def rev_of_array(arr,n):
    def printArray(arr,n):
        print ("The reversed array is:")
        for i in range(n):
            print(arr[i],end=' ')
        print()
    def reverseArray(arr,n):
        ans = [0]*n
        for i in range(n-1,-1,-1):
            ans[n-i-1] = arr[i]
        printArray(ans,n)
    reverseArray(arr,n)
def rev_of_array2(arr,n):
    def printArray(arr,n):
        print("The reversed array is:")
        for i in range(n):
            print(arr[i], end=" ")
        print()
    def reverseArray(arr,n):
        p1 =0
        p2 =n-1
        while p1<p2:
            arr[p1],arr[p2] = arr[p2],arr[p1]
            p1 +=1
            p2 -=1
        printArray(arr,n)
    reverseArray(arr,n)
def palindrome_string(i,s):
    if i >= len(s)//2:
        return True
    if s[i] != s[len(s)-i-1]:
        return False
    return palindrome_string(i+1,s)
def palindrome_string2(i,s):
        left = 0
        right = len(s)-1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
def fibonacci_number(n):
    if (n<=1):
        return n
    return fibonacci_number(n-1) + fibonacci_number(n-2)

print(fibonacci_number(7))