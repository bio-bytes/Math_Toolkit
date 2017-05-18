import matplotlib.pyplot as pyplot
from scipy.stats import *
import numpy as np
import math
import random

print("Doing Analysis for M-M Equation")
print("Possible Reaction that can take place")
print("\n")
print("1. E + S -->  ES , with K1 rate constant")
print("2. ES -->  E + S , with K2 rate constant")
print("4. ES --> E + P , with K4 rate constant")
print("\n")
print("Here E , S , ES and P are the fundamental species which we need track")

number_of_chemical_species = 4
number_of_possible_reaction = 4

r1 = 20
r2 = 30
r3 = 100

E_current = 0.00001
S_current = 0.001
Es_current = 0
P_Current = 0

time_initial = 0

max_reaction = 10000
max_time = 1

E_array = np.zeros(max_reaction+1)
S_array = np.zeros(max_reaction+1)
P_array = np.zeros(max_reaction+1)
ES_array = np.zeros(max_reaction+1)
tt_array = np.zeros(max_reaction+1)

a1 = r1*E_current*S_current
a2 = r2*Es_current
a3 = r3*P_Current

a0 = a1 + a2 + a3

r_counter = 0

while r_counter < max_reaction and time_initial < max_time:

	E_array[r_counter] = E_current
	S_array[r_counter] = S_current
	P_array[r_counter] = P_Current
	ES_array[r_counter] = Es_current

	r_counter = r_counter + 1

	rn1 = round(random.uniform(0.1, 1.0), 10)
	rn2 = round(random.uniform(0.1, 1.0), 10)
	
	t_next = (1/a0)*(math.log(1/rn1))
	tt_array[r_counter]=t_next 

	time_initial = time_initial + t_next

	if rn2 >= 0 and rn2 < a1/a0:

		E_current = E_current - 1
		S_current = S_current - 1
		Es_current = Es_current + 1

	elif rn2 >= a1/a0  and rn2 < (a1+a2)/a0:

		Es_current = Es_current - 1
		E_current = E_current + 1
		S_current = S_current + 1

	elif rn2 >= (a1+a2)/a0 and rn2 < (a1+a2+a3)/a0:

		E_current = E_current - 1
		P_Current = P_Current - 1
		Es_current = Es_current + 1

	elif rn2 >= (a1+a2+a3)/a0 and rn2 < 1:

		Es_current = Es_current - 1
		E_current = E_current + 1
		P_Current = P_Current + 1

pyplot.plot(E_array)
pyplot.plot(S_array)
pyplot.plot(ES_array)
pyplot.plot(P_array)
pyplot.show()