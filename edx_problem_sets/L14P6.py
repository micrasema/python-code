import random


def pick(yourlist):
    pick = random.choice(yourlist)
    yourlist.remove(pick)
    return pick
    
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
   
    success = 0
    trials = 0
    
    for i in range(numTrials):
        
        balls = ['r', 'r', 'r', 'g', 'g', 'g']
        count_red = 0
        count_green = 0
        
        for i in range(3):
            guess = pick(balls)
            if guess == 'r':
                count_red += 1
            else:
                count_green += 1
        
        if count_red == 3 or count_green == 3:
            success += 1.0
            trials += 1.0
        
        else:
            trials += 1.0
    
    return success/trials
        
            
         
        