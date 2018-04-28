
# goldMine = ((1, 3, 3), (2, 1, 4), (0, 6, 4))

# def printMax(gold, m, n):
#   print(maxGoldMine(gold, m, n))

# def maxGoldMine(goldMine, m, n):
#   goldTable = [[0 for i in range(n)] for j in range(m)]

#   for col in range(n-1, -1, -1):
#     for row in range(m):
#       if col == n-1:
#         right = 0
#       else:
#         right = goldTable[row][col+1]
#       if row == 0 or col == n-1:
#         right_up = 0
#       else:
#         right_up = goldTable[row-1][col+1]
#       if row == m-1 or col == n-1:
#         right_down = 0
#       else:
#         right_down = goldTable[row+1][col+1]

#       goldTable[row][col] = goldMine[row][col] + max(right, max(right_up, right_down))

#   print(goldTable)    
#   res = 0
#   for i in range(n):
#     res = max(res, goldTable[i][0])
#   return res

# if __name__ == '__main__': printMax(goldMine,3,3)

# Write your code here

# r, c = [int(x) for x in input().split()]

# ar = []
# for i in range(r):
#   ar.append(tuple(int(x) for x in input().split()))

# print(ar)

from sys import stdin, stdout

def main():
  # input via readline method
  row, col = [int(x) for x in stdin.readline().split()]

  goldMine = []

  for i in range(row):
    goldMine.append(list([int(x) for x in stdin.readline().split()]))
  
  memo = [[0 for x in range(row+1)] for y in range(col+1)]

  for r in range(1, row+1):
    for c in range(1, col+1):
      memo[r][c] = memo[r-1][c] + memo[r][c-1] - memo[r-1][c-1] + goldMine[r-1][c-1]
  
  for query in range(int(input())):
    x1,y1,x2,y2 = [int(x) for x in stdin.readline().split()]

    stdout.write(memo[x2][y2] - memo[x1-1][y2] - memo[x2][y1-1] + memo[x1-1][y1-1])
 
 
if __name__ == '__main__': main()