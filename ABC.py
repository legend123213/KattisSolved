number = [int(i) for i in input().split()]
number.sort(reverse=False)
order =  input()
k = ['A','B','C']
kp = {k[i]:number[i] for i in range(len(k))}

# for i in range(len(number)):
#     kp[k[i]] = number[i]

output =[kp[order[i]] for i in range(len(k))]

print(*output)