from ising_class import *

Temp = 2.3        # Temperature
n = 20            # Sites per edge for n x n system
ntrials = 500000  # Number Trials
nequil = 100000   # Equilibration steps

ising1 = ising(Temp,n)
ising1.randomize()

ising1.trials(nequil) #equilibration steps
ising1.resetprops() #reset properties to start at 0

#run trials
for i in range(ntrials):
    ising1.trial()
    ising1.addprops()

ising1.calcprops() #caluclate and print properties
ising1.printsys() #print the model itself
