from ising_class2 import *

Temp = .1        # Temperature
n = 20            # Sites per edge for n x n system
ntrials = 500000  # Number Trials
nequil = 100000   # Equilibration steps

ising1 = ising(Temp,n)
ising1.randomize()

while Temp < .2:
    ising1.changeTemp(Temp)
    ising1.trials(nequil) #equilibration steps
    ising1.resetprops() #reset properties to start at 0
    #run trials
    for i in range(ntrials):
        ising1.trial()
        ising1.addprops()
    ising1.calcprops() #calculate and print properties
    Temp += .1
    
ising1.printsys() #print the model itself
