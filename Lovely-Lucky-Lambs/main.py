
#####Functions
# input: number of lambs
# output: an integer which represents the difference between the minimum and maximum number of henchmen who can share the LAMBs
def solution(lambs):
	## Variables
	minimum = 1 # The most junior henchman (with the least seniority) gets exactly 1 LAMB.


	## Number Validator
	def number_is_valid(number, method, style): # Using the provided rules, each input is checked with it's corresponding style
		if style == "stingy":
			if number>=sum(method[-2:number]) and number<=sum(method[-1:number]*2): # Formula for maximum employees per set of lambs
				return True
		elif style == "generous":
			if (number!=minimum) and number>sum(method[-2:number]) and number==sum(method[-1:number]*2): # Formula for maximum lambs per employee
				return True


	## Generous Method
	generous = [minimum] # (There will always be at least 1 henchman on a team.)
	number = minimum
	while sum(generous) + number <= lambs: 
		if number_is_valid(number, generous, "generous"):
			generous.append(number)
		number += 1


	##Stingy Method
	stingy = [minimum] # (There will always be at least 1 henchman on a team.)
	number = minimum
	while sum(stingy) + number <= lambs: 
		if number_is_valid(number, stingy, "stingy"):
			stingy.append(number)
		number += 1


	## Return
	if debug == True:
		return "\nInput: "+str(lambs)+"\n"+"Generous:"+str(generous),"Stingy: "+str(stingy), "Output: "+str(abs(len(generous) - len(stingy))) # Returns the difference between the number of henchmen receiving lambs via the provided methods
	else:
		return abs(len(stingy) - len(generous))


#####Debugging
var = 13

debug = True
top = 13
bot = 10

if debug == True:
	for test in list(range(bot,top+1)):
		for output in solution(test):
			print(output)
else:
	print(solution(var))