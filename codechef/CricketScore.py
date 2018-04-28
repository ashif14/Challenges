def check():
	tc = int(input())
	
	isValid = True
	runs = 0
	wickets = 0
	
	while tc > 0:
	
	  curr_runs, curr_wickets = [int(x) for x in input().split()]
	  if curr_runs < runs or curr_wickets < wickets:
	    print("NO")
	    return
	  elif wickets == 10 and curr_runs > runs:
	    print("NO")
	    return
	  else:
	    runs = curr_runs
	    wickets = curr_wickets
	    
	  tc -= 1
	 
	print("YES")
check();