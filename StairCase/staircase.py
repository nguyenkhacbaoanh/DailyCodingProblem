# In the first case, we can climb to staircase by one or two steps with our choise
# We need to count all possible ways
# I found the rule:
#	N = 1 : [1]
#	N = 2 : [1,1], [2]
#	N = 3 : [1,1,1], [1,2], [2,1]
#	N = 4 : [1,1,1,1], [2,1,1], [1,2,1], [1,1,2], [2,2]
# source: dailycodingproblem.com/?ref=csdojo

def stair_case(steps):
	if steps == 0:
		return 0
	elif steps == 1:
		return 1
	elif steps == 2:
		return 2
	else:
		return stair_case(steps-1)+stair_case(steps-2)

# Time complex in function stair_case is O(2^N)

def stair_case2(steps):
	a,b = 1,2
	# loops until only 2 steps, 
	# because i knew the number of unique ways for 2 finals steps
	while steps > 1:
		a,b=b,a+b
		steps -= 1
	return a

# stair_case2 have O(N) complex

#---------------------------------------------------------------------#
# In the 2e case, we define our own capacible step climb              #
# For example, X = {1,3,5}					      # 
#---------------------------------------------------------------------#

def stair_case3(N,X):
	pass
	
if __name__ == "__main__":
	print(stair_case2(4))
