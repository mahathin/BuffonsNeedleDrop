""" The experiment set up:
    A x-y plane with lines x = 2n drawn for all n belonging to N.
    
    The Experiment:
    1.  Random theta in the range [0,2pi]
    2.  A random point P(x0,y0) by selecting a random x0 from (-infinity,infinity) and y0 from (-infinity,infinity)

    We will obtain theta only from [0,pi] since it is symmetric.
    We will not select a y0 since the y coordinate of the point will not affect the probability.
"""

import numpy as np
import random
#first program
N_true = 0 #this is a counter for the number of times the needle crosses a line
N_rep = 10000000 #this is the number of times the needle is thrown

for i in range(N_rep):
    theta = random.uniform(0, np.pi) #this is the angle that the needle makes with the negative direction of the closest line on left of the end of the needle that is farther to the right
    x0 = random.uniform(0, 2) #this is the point that the end of the needle that is relatively at thhe left
    #x0 is being chosen from the [0,2] since regardless of where it falls the closest parallel lines can be assigned values x=0 and x=2 and this does not affect the probability
    if x0 + 1.5*np.sin(theta) == 0 or x0 + 1.5*np.sin(theta) >= 2: #condition for needle to cross line
        N_true = N_true + 1
        
Probability = N_true/N_rep
print(Probability)

#BELOW PROGRAM NEEDS MORE WORK TO OBTAIN AN ORGANISED SET OF OF VALUES
#BUT IS INTERESTING TO SEE RESULTS.
"""
# second program
sequence=[]
for a and b in range(1,100):
    p=[]
    N_tru=0
    stepsize1 = 2/a
    stepsize2 =2/b
    x0set = np.arange(0,2,stepsize1)
    thetaset = np.arange(0,np.pi,stepsize2)
    for x0 in x0set:
        for theta in thetaset:
            p = p+[(x0,theta)]
    for k in range(len(p)):
        x0 = p[k][0]
        theta = p[k][1]
        if x0 + 1.5*np.sin(theta) == 0 or x0 + 1.5*np.sin(theta) >= 2:
            N_true = N_true + 1
    Probability = N_tru/(len(p))
    sequence = sequence + [Probability]
print(sequence)"""
