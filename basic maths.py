def count_digits(num):
    count = 0
    while num>0:
        last = num%10
        num = num//10
        count = count +1
    return(count)
def rev_digits(num):
    revno=0
    while num>0:
        last = num%10
        num = num//10
        revno = (revno*10) +last 
    return(revno)
def palindrome(num):
    temp = num
    revno=0
    while num>0:
        last = num%10
        num = num//10
        revno = (revno*10) +last 
    if revno == temp:
        return True
    else:
        return False
def armstrong(n):
    #try 153
    #sum of digits raised to the power of number of digits
    sum = 0
    temp = n
    while n>0:
        last = n%10
        n = n//10
        sum = sum + pow(last,3)
    if sum == temp:
        return True
    else:
        return False
def divisor(n):
    """for i in range(1,n+1):
        if n%i ==0:
            print(i,end=', ')"""
    divlist = []
    for i in range(1,int(n**0.5)):
        if n %i ==0:
            divlist.append(i)
            if n//i != i:
                divlist.append(n//i)
    divlist.sort()
    return(divlist)
def prime(n):
    count = 0
    for i in range (1,int(n**0.5)+1):
        if n%i == 0:
            count = count+1
            if n//i!=i:
                count=count+1
    if count==2:
        return True
    else:
        return False
def gcd(n,m):
    gcd = 1
    for i in range(min(n,m),1,-1):
        if n%i ==0 and m%i==0:
            return i
            break
def euclidean_gcd(n,m):
    #states that gcd(a,b) = gcd(a-b,b)
    #keep subtracting until one is 0 then other is gcd
    #instead of subtracting using modulus
    while n>0 and m>0:
        if n>m:
            n= n%m
        else:
            m= m%n
    if n==0:
        return m
    else:
        return n 


print(euclidean_gcd(20,400))