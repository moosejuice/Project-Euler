'''
Longest Collatz sequence
Show HTML problem content
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

from datetime import datetime

def oddCalculation(inputNumber):
    return ((3*inputNumber) + 1)

def evenCalculation(inputNumber):
    return (inputNumber /2)

def theCalculation(inputNumber):
    if ( (inputNumber % 2) == 0 ):
        return evenCalculation(inputNumber)
    else:
        return oddCalculation(inputNumber)

# dictionary of starting number and chain length
#

def sequence(number, chainLengths):
    startingNumber = number
    chainLength = 1

    while ( number != 1 ):
        if ( number < startingNumber ):
            remainingChainLength = chainLengths[number]
            return (remainingChainLength + chainLength)
            
        number = theCalculation(number)
        chainLength += 1
    return chainLength

def sequenceWriter(number):
    chainLength = 1
    print ("%d" % number, end='')
    while ( number != 1 ):
        chainLength += 1
        number = theCalculation(number)
        print (" -> %d" % number, end='')
    return chainLength

if __name__ == '__main__':
    start=datetime.now()
    chainDict = {}
    for number in range(1,1000001):
        chainLength = sequence(number, chainDict)
        chainDict[number] = chainLength
    
    
    index = max(chainDict, key=lambda key: chainDict[key])
    print ("Largest chain was for starting number %d, with a length of %d. The chain is below" % (index, chainDict[index]))
    sequenceWriter(index)
    print ("")

    print (datetime.now()-start)
    
