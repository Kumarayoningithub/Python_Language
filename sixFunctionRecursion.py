'''def sum(a,b):
    s=a+b
    return s

print(sum(3,4))'''

'''def printhello(a):
    for i in range(a):
        print("hello")

printhello(5)'''


'''cities= ["delhi","chennai","mumbai","kolkata","hyderabad","bangalore"]

def print_len(list):
    print(len(list))

print_len(cities)'''



'''cities= ["delhi","chennai","mumbai","kolkata","hyderabad","bangalore"]

def printl(list):
    n=len(list)
    for i in range(n):
        #print(" ",end=" ")
        print(list[i], end=" ")


printl(cities)'''

'''def fact(n):

    factt =1
    for j in range(1,n+1):
        factt= factt*j
    return factt



s=fact(5)
print(s)'''


########RECURSION##############

'''def show(n):
    if(n == 0):
         return
    print(n)
    show(n-1)
show(5)'''
'''def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)

k = fact(3)
print (k)'''

'''def sum(n):
    if(n==0):
        return 0
    return sum(n-1)+n
print(sum(5))'''

def print_list(list,idx):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
fruits=["apple", "mango", " banana", "grapes"]
print_list(fruits,0)





