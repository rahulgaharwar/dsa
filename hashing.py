def not_hashing(n,arr):
#brute force, time complexity high
    count = 0
    for i in arr:
        if i == n:
            count = count + 1
    print (count)

# hashing
# it prestores the information beforehand and then just fetches it when needed

def array_hashing():

    #size of the array
    n = int(input("Size of the array: "))
    
    #read the array elements
    arr = list(map(int,input("enter the array: ").split()))

    hash = [0] * 13
    for num in arr:
        hash[num] += 1

    #read the number of queries
    q = int(input("how many numbers would u like to find: "))

    for i in range (q):
        number = int(input("which number would u like to find: "))

        print("number of times present:",hash[number])
 
def char_array_hashing():
    s = input("Enter the string: ")

    hash = [0] * 300
    for i in s:
        hash[ord(i)] += 1

    p = int(input("number of queries to be performed: "))

    for j in range (p):
        q = input("which character would you like to search: ")
        print("number of times it appears is: ", hash[ord(q)])
    
def dictionary_hashing():
    n = int(input("Enter the size of array: "))
    
    arr = list(map(int,input("Enter the array elements: ").split()))

    freq_map = {}
    for num in arr:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    q = int(input("number of queries to be performed: "))

    for i in range(q):
        p = int(input("enter the number: "))
        print("number of times its present: ", freq_map.get(p,0))
