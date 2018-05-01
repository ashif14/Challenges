# n = int(input())

# series = [int(x) for x in input().split()]

# count = 0
# visited = [False for i in range(n)]


# for i in range(n):
#     curr = series[i]
#     if visited[i] == True or series[i] == (i+1):
#         continue
#     cycle_size = 0
#     j = i
#     while visited[j] != True:
#         visited[j] = True
#         j = series[j] -1
#         cycle_size += 1
    
#     count += (cycle_size - 1)
    
# print(count)


def reverse(l,i,j):
    while i < j:
        tmp = l[i]
        l[i] = l[j]
        l[j] = tmp
        i += 1
        j -= 1

l = [4,2,3,1]

reverse(l,0,3)

print(l)