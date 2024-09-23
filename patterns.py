def pattern1(n):
    for i in range(n):
        for j in range(n):
            print('*', end=' ')
        print()

def pattern2(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end=' ')
        print()

def pattern3(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end=' ')
        print()

def pattern4(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1,end=' ')
        print()

def pattern5(n):
    for i in range(n):
        for j in range(n-i):   #if count starts from 1 then n-i+1
            print('*',end=' ')
        print()

def pattern6(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end=' ')
        print()

def pattern7(n):
    for i in range(n):
        #space
        for j in range(n-i):
            print(' ',end=' ')
        #stars
        for j in range(2*i-1):
            print('*',end= ' ')
        #space
        for j in range(n-i):
            print(' ',end=' ')
        print()

def pattern8(n):
    for i in range(n):
        #space
        for j in range(i):
            print(' ',end=' ')
        #stars
        for j in range(2*n-(2*i+1)):
            print('*',end=' ')
        #space
        for j in range(i):
            print(' ',end=' ')
        print()

def pattern9(n):
    pattern7(5)
    pattern8(5)

def pattern10(n):
    for i in range(1,2*n):
        stars = i
        if i>n:
            stars = 2*n-i
        for j in range(stars):
            print('*',end=' ')
        print()

def pattern11(n):
    for i in range(n):
        if i%2 ==0:
              start=1
        else:
            start=0
        for j in range(i+1):
            print(start, end= ' ')
            start=1-start
        print()

def pattern12(n):
    space = 2*(n-1)
    for i in range(n):
        #numbers:
        for j in range(1,i+1):
            print(j,end=' ')
        #space:
        for j in range(space):
            print(' ',end= ' ')
        #numbers:
        for j in range(i,0,-1):
            print(j,end=' ')
        print()
        space = space-2

def pattern13(n):
    num = 1
    for i in range(n):
        for j in range (i):
            print(num,end=' ')
            num=num+1
        print()

def pattern14(n):
    for i in range(n):
        for j in range(i):
            print(chr(65+j), end=' ')
        print()

def pattern15(n):
    for i in range(n,0,-1):
        for j in range(i):
            print(chr(65+j), end=' ')
        print()

def pattern16(n):
    for i in range(n):
        for j in range(i):
            print(chr(65+i-1),end=' ')
        print()

def pattern17(n):
    
pattern17(5)