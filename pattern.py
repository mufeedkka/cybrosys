n=6
m = (2 * n) - 4
a = (2 * n) - 4
for i in range(1,n):
    for j in range(0,m):

        print(end=" ")
    m=m-1
    for j in range(0,i*2):
        print("*",end="")
    print("")
    for j in range(0,a):

        print(end=" ")
    a=a-1
    for j in range(0,i*2):
        print("*",end="")
    print("")