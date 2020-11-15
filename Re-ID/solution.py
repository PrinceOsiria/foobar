#############################################################################################
# Documentation: solution.py
# solution.py contains the function "solution(*args)" which is used in the Google foobar Challenge; "Re-ID"
# Coded by Tyler Pryjda
#############################################################################################
#####readme.txt#####
"""
Re-ID
==========
There's some unrest in the minion ranks: minions with ID numbers like "1", "42",
and other "good" numbers have been lording it over the poor minions who are stuck
with more boring IDs. To quell the unrest, Commander Lambda has tasked you with reassigning
everyone new, random IDs based on her Completely Foolproof Scheme.

She's concatenated the prime numbers in a single long string: "2357111317192329...".
Now every minion must draw a number from a hat. That number is the starting index in that
string of primes, and the minion's new ID number will be the next five digits in the string.
So if a minion draws "3", their ID number will be "71113".

Help the Commander assign these IDs by writing a function solution(n)
which takes in the starting index n of Lambda's string of all primes, and
returns the next five digits in the string. Commander Lambda has a lot of minions,
so the value of n will always be between 0 and 10000.

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution(0)
Output:
    23571

Input:
Solution.solution(3)
Output:
    71113

-- Python cases --
Input:
solution.solution(0)
Output:
    23571

Input:
solution.solution(3)
Output:
    71113
    """
#####NOTES.txt#####
"""
Hello, World!

Maybe I went a little overboard with this one, but I think from a scalable  standpoint, if Commander Lambda wanted to, 
she could compile a csv of indices, parse it, generate IDs, assign them names from the csv, attach names and ids to a dictionary, and export the dictionary as a csv
This approach would be ideal if she used google forms to generate the csv, sending the form to all of her minions

ID Generation is based on a previous script of mine, namely "Prime Miner". The original script returns a list of all primes within 0:arg, while the modified version returns arg primes

Thanks for reading!

Tyler Pryjda
"""
#############################################################################################
#####Functions
#############################################################################################

# Prime Miner
def prime_mine(depth, init):
    prime = init
    i=3

    # If the number isn't even or a false prime, append, else skip
    while len(prime) <= (depth-1):
        if (i % 2 != 0) and (not is_false_prime(i, prime)):
            prime.append(i)
            i = i + 2
        else:
            i = i + 2

    return prime


# Is the odd number evenly divisible by any previous prime numbers?
def is_false_prime(i, prime):
    n = 0
    while n < len(prime):
        if i % prime[n] == 0:
            return True
        n = n + 1
    return False


def solution(input):

    #Generates ID
    def generate_ID(index):                                                                 # Generates ID from Index
        depth = index+idLength
        primeString = "".join([str(elem) for elem in prime_mine(depth+idLength, [2, 3])])
        return primeString[index:index+idLength]


#Failsafe
    if type(input) is (not (list or int)) :                                                 # Failsafe which prevents inputs that are not of type list or int
        print("input must be of type int or list")
        return type(input)

#If input is a list, Program Mode #1
    if type(input) is list:                                                                 # if input is a list:
        outputList = []                                                                     #   Define outputList

        for index in input:                                                                 #   for each item in the input list:
            if type(index) is int:                                                          #       if the item is an int:
                outputList.append(generate_ID(index))                                       #           generate an ID with it as an index, and append it to the outputList
            else:
                try:
                    outputList.append(generate_ID(int(index)))                              #       if the item is not an int, attempt converting it
                except:
                    print("input must be of type int or list")
                    return

        return (outputList)                                                                 #   returns outputList as a list of strings

#If input is an int, Program Mode #2
    if type(input) is int:                                                                  # if the input is an int:
        outputString = generate_ID(input)                                                   #   Generate ID from input as index and assign to outputString
        return (outputString)                                                               #   return outputString

#Tests various different output types
def test_outputs(programMode):                                                              # Function designed for use in debugging & testing
    if programMode == inputOptions[0]:                                                      # programMode = 0 - None, script is being used as a module
        return

    elif programMode == inputOptions[1]:                                                      # programMode = 1 - List, function will return a list containing all IDs
        print(solution(args))

    elif programMode == inputOptions[2]:                                                      # programMode = 2 - Int, function will return a str containing an ID
        for input in range(len(args)):
            try:
                print(solution(int(args[input])))
            except:
                print("input must be of type int")

    elif programMode == inputOptions[3]:                                                      # programMode = 3 - DEBUG, recursively loop through all input types
        for modes in range(len(inputOptions) - 1):
            test_outputs(inputOptions[modes])
    else:                                                                                     # Prevents DEBUG from attempting to select impossible options
        print("ERROR: InputOptions indicates non-existent options")
        return


#############################################################################################
#####Variables
#############################################################################################
args = [0, 3, 5, 7, 9, 11, 13]

inputOptions = [
    "0",        #0 - None, script is being used as a module
    "1",        #1 - List, function will return a list containing all IDs
    "2",        #2 - Int, function will return a str containing an ID
    "DEBUG"     #3 - DEBUG, loop through all input types)
]

idLength = 5
programMode = "0"
#############################################################################################
#####Main
#############################################################################################
test_outputs(programMode)


