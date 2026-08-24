#pattern : 

#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * * 

# key pattern : space decreases , star increase

n = 6 
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="") # printing the spaces // n-i = 6-1 = 5,4,3,2,1,0
    for j in range(i):
        print("*",end=" ") #printing the stars // i 1,2,3,4,5,6
    print()