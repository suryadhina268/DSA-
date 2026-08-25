# * * * *
#  * * *
#   * *
#    *

n = 4

for i in range(0,n):
    for j in range(i):
        print(" ",end="")
    for j in range(n-i):
        print("*",end=" ")
    print()


