def solution(lambs):
	## Variables
	minimum = 1
	stingy = [minimum]
	generous = [minimum]

	## Generous Method - More lambs per employee, less employees included
	number = minimum
	while sum(generous) + number <= lambs: 
		if (number!=minimum) and number>=sum(generous[-2:number]) and number==sum(generous[-1:number])*2:
			generous.append(number)
		number += 1

	## Stingy Method - Less lambs per employee, more employees included
	number = minimum
	while sum(stingy) + number <= lambs: 
		if number>=sum(stingy[-2:number]) and number<=sum(stingy[-1:number])*2:
			stingy.append(number)
		number += 1

	## Returns an integer which represents the difference between the minimum and maximum number of henchmen who can share the LAMBs
	return abs(len(stingy) - len(generous))
