import matplotlib.pyplot as pyplot
from scipy.stats import rv_continuous
print("Doing Analysis for M-M Equation")
print("Possible Reaction that can take place")
print("\n")
print("1. E + S -->  ES , with K1 rate constant")
print("2. ES -->  E + S , with K2 rate constant")
print("3. E + P -->  ES , with K3 rate constant")
print("4. ES --> E + P , with K4 rate constant")
print("\n")
print("Here E , S , ES and P are the fundamental species which we need track")
number_of_chemical_species = 4
number_of_possible_reaction = 4
time_vector = []
rate_of_reaction = [2 , 1 , 3 , 4]
X = [233 , 403 , 133 , 189]
a_ut = [ X[0]*X[1]*rate_of_reaction[0] , rate_of_reaction[1]*X[1] , rate_of_reaction[2]*X[0]*X[3] , rate_of_reaction[3]*X[2] ]
a0t = sum(a_ut) 
tinit = 0
time_vector.append(tinit)
tend = 10