

def getSubsetSum(arr,n, sum):
  
  memo = [[False for i in range(sum + 1)] for j in range(n+1)]

  for i in range(n+1):
    memo[i][0] = True

  for val in range(1,n+1):
    for s in range(1,sum+1):
      if s < arr[val-1]:
        memo[val][s] = memo[val-1][s]
      if s >= arr[val-1]:
        memo[val][s] = memo[val-1][s] or memo[val-1][s-arr[val-1]]

  
  return memo

def display(l):
  print(l)
  

def findSubsetSum(arr, n, memo, sum, l):
  if n == 0 and sum != 0 and memo[n][sum] == True:
    l.append(arr[n])
    print(l)
    del l[:]
    return
  if n ==0 and sum == 0:
    print(l)
    del l[:]
    return
  if memo[n][sum] == True:
    b = []
    b.extend(l)
    findSubsetSum(arr,n-1,memo,sum,b)
  if sum >= arr[n-1] and memo[n-1][sum - arr[n-1]] == True:
    l.append(arr[n-1])
    findSubsetSum(arr,n-1,memo,sum-arr[n-1],l)
  
    
def main():
  arr = [3,34, 4, 12, 5, 2]
  sum = 9
  memo = getSubsetSum(arr,len(arr),sum)
  # print(memo)
  findSubsetSum(arr,len(arr),memo,sum,[])

if __name__ == '__main__': main()


