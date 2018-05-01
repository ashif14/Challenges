
seq = [1,-2,3,4,0,0]
n = len(seq)
visited = [False for i in range(n)]

max_sum = 0
for j in range(1,n-1,1):
  
  if visited[j] == True:
    continue
  print("visiting"+str(seq[j]))
  p = j-1
  q = j
  r = j+1
  _sum = 0
  while p >= 0 and r <= n-1:
    print('{},{},{}'.format(p,q,r))
    if visited[r] == True:
      r += 1
    elif visited[p] == True:
      p -= 1
    elif seq[q]**2 < seq[p]*seq[r]:
      p -= 1
    elif seq[q]**2 > seq[p]*seq[r]:
      r += 1
    else:
      print("in gp: {},{},{}".format(p,q,r))
      visited[p] = True
      _sum += seq[p]
      p = q
      q = r
      r += 1
  print("Out of while: {},{},{}, {}".format(p,q,r,_sum))
  if p >=0:
    visited[p] = True
    visited[q] = True
    max_sum = max(max_sum, _sum+seq[p]+seq[q])
  print("Max Sum:{}".format(max_sum))
  
print(max_sum)

