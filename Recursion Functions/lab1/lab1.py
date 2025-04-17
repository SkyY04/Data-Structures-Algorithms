# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Saeha Yoon
# Student Number: 139277222
#

#Function 1:
def wins_rock_scissors_paper(player, opponent):
	#strings may have any casing
	player = player.lower()
	opponent = opponent.lower()

	#rule
	winning_throws_rule = {
		"rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

	if player in winning_throws_rule and winning_throws_rule[player] == opponent:
		return True
	return False

#Function 2:
def factorial(n):

	#only pass a non-negative integer
	if n < 0:
		return ValueError("The input should be a non-negative integer.")
	#0! = 1 by definition
	if n==0 or n==1:
		return 1
	
	number =1
	#n! (factorial) = n*(n-1)*(n-2)...*1 
	for i in range(2,n+1):
		number*=i
	return number

#Function 3:
def fibonacci(n):
	#only pass a non-negative integer
	if n < 0:
		return ValueError("The input should be a non-negative integer.")
	elif n == 0:
		return 0
	elif n == 1 or n==2:
		return 1
	else:
		number = fibonacci(n-1) + fibonacci(n-2)
	return number

#Function 4:
def sum_to_goal(nums, goal):
    total = 0
    for num in nums:
        if num <= goal:
            total += num
    return total

    
#Python Objects
class UpCounter:
	def __init__(self,step_size=1):
		self.step_size=step_size
		self.current_counter=0
	def count(self):
		return self.current_counter
	def update(self):
		self.current_counter+=self.step_size

class DownCounter(UpCounter):
	def update(self):
		self.current_counter-=self.step_size



