#####Function
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

## Return
    if debug:
        return f"\nInput: {str(lambs)}\nGenerous:{str(generous)}\nStingy: {str(stingy)}\nOutput: {abs( len(generous) - len(stingy) )}" # Returns the input as well as the contents of the generous and stingy lists
    else:
        return abs(len(stingy) - len(generous)) # Returns the difference between the number of henchmen receiving lambs via the provided methods
#####Main
var = 13

debug = 1
start= 10
end= 13

if debug:
    for test in range(start,end+1):
        for output in solution(test):
            print(output)
else:
    print(solution(var))
