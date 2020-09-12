from ising_class import *

Temp = 0.5        # Temperature
n = 20            # Sites per edge for n x n system
ntrials = 500000  # Number Trials
nequil = 100000   # Equilibration steps

ising1 = ising(Temp,n)
ising1.randomize()

while Temp < 4:
    ising1.changeTemp(Temp)
    ising1.trials(nequil) #equilibration steps
    ising1.resetprops() #reset properties to start at 0
    #run trials
    for i in range(ntrials):
        ising1.trial()
        ising1.addprops()
    ising1.calcprops() #calculate and print properties
    Temp += .2
    
ising1.printsys() #print the model itself
