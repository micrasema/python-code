# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b_precompiled_27 import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    maxPop = 1000
    numViruses = 100
    viruses = []
    finalPopulation = []
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol':False}
    mutProb = 0.005
    
    for i in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))

    numSteps0 = 150
    numSteps1 = 75 # 0 75 150 300
    
    for i in range(numTrials):
        
        patient = TreatedPatient(viruses, maxPop)
        
        for p in range(numSteps1):
            numVirusesNow = patient.update()
        
        patient.addPrescription('guttagonol')
        
        for q in range(numSteps0):
            numVirusesNow = patient.update()
        
        finalPopulation.append(numVirusesNow)
    
    pylab.hist(finalPopulation, numTrials)
    pylab.title("Should you delay your antiviral treatment?")
    pylab.xlabel("Size of Virus Population")
    pylab.ylabel("Number of Trials")
    pylab.show()
    
    






#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    maxPop = 1000
    numViruses = 100
    viruses = []
    trialsYo = numTrials
    
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol':False, 'grimpex':False}
    mutProb = 0.005
    
    numSteps0 = 150
    numSteps1 = 0 # 0 75 150 300
    numSteps2 = 150
    
    finalPopulation = []
    count = 0
    
    for i in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    
    for i in range(numTrials):
        
        patient = TreatedPatient(viruses, maxPop)
        
        for p in range(numSteps0):
            numVirusesNow = patient.update()
        patient.addPrescription('guttagonol')
        
        for q in range(numSteps1):
            numVirusesNow = patient.update()
        patient.addPrescription('grimpex')
        
        for r in range(numSteps2):
            numVirusesNow = patient.update()
        finalPopulation.append(numVirusesNow)
        
        count += 1
        trialsYo -= 1
        
        if count%15 == 0:
            print 'Congratulations, you only have ' + str(trialsYo) + ' trials left!'
    
    pylab.hist(finalPopulation, numTrials)
    pylab.title('Effects of delayed treatment with 2 antivirals')
    pylab.xlabel('Number of viruses in body after treatment')
    pylab.ylabel('Number of trials')
    pylab.show()
