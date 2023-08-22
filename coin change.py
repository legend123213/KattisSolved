coins = [2,3,5,10]
goal = 15
arr2d =[[0 for i in range(goal)] for i in range(len(coins))]
print(arr2d)
arr2d[0] = [1 if i%coins[0]==0 else 0 for i in range(goal)]

for i in range(len(coins)):
    arr2d[i][0] = 1
print(arr2d)

for j in range(1,len(coins)-2):
   for i in range(1,goal-2):    
        if coins[j]>i:
            arr2d[i][j]=arr2d[i][j-1]
        else:
            pass
            # tmp = arr2d[i-coins[j]][j]
            # arr2d[i][j]=arr2d[i][j-1] + arr2d[i][tmp]
print(arr2d)