"""
Author: Kevin J Dolan (Github: kdolan)
Date: 2/17/2013
Purpose: PseudoRandom Github Project. Generate sudo random numbers in python.
"""

import time
def random(seed, a, c, n, interations):
    randomNumbers = []
    for i in range(0, interations):
        if i == 0:
            #First case. use seed
            randomNumbers.append(seed)
        else:
            lastValue = randomNumbers[(len(randomNumbers)-1)]
            randomNumber = (a*lastValue+c)%n
            randomNumbers.append(randomNumber)
    return randomNumbers
    
def randomTimeSeed(a, c, n, interations):
    """Modified from using seconds to using miliseconds to make automatic caculations have different seeds."""
    randomNumbers = []
    for i in range(0, interations):
        if i == 0:
            mills = int(round(time.time() * 1000))
            print("Time: "+str(mills))
            seed = mills%n
            randomNumbers.append(seed)
        else:
            lastValue = randomNumbers[(len(randomNumbers)-1)]
            randomNumber = (a*lastValue+c)%n
            randomNumbers.append(randomNumber)
    return randomNumbers