import matplotlib.pyplot as pyplot
import numpy as np
import math
import random

print("Consider the following set of Equations ")
print(" E + S --> ES with K1 rate ")
print(" ES --> E + S with K2 rate ")
print(" ES --> E + P with rate K3 ")

r1 = 0.000001
r3 = 0.111
r2 = 12

E_current = 25
S_current = 583
ES_current = 5
P_current = 13

a1 = r1*E_current*S_current
a2 = r2*ES_current
a3 = r3*ES_current

a0 = a1 + a2 + a3 

time_initial = 0
max_reaction = 10000
max_time = 1

E_array = []
S_array = []
ES_array = []
P_array = []
tt_array = []


r_counter = 0

while r_counter < max_reaction and time_initial < max_time:

	E_array.append(E_current)
	S_array.append(S_current)
	ES_array.append(ES_current)
	P_array.append(P_current)

	r_counter = r_counter + 1

	rn1 = round(random.uniform(0.1, 1.0), 10)
	rn2 = round(random.uniform(0.1, 1.0), 10)
	
	t_next = (1/a0)*(math.log(1/rn1))
	time_initial = time_initial + t_next
	tt_array.append(time_initial)

	print(rn2,a1/a0,(a1+a2)/a0,(a1+a2+a3)/a0)

	if rn2 >= 0 and rn2 < a1/a0:

		E_current = E_current - 1
		S_current = S_current - 1
		ES_current = ES_current + 1

	elif rn2 >= a1/a0  and rn2 < (a1+a2)/a0:

		ES_current = ES_current - 1
		E_current = E_current + 1
		S_current = S_current + 1

	elif rn2 >= (a1+a2)/a0 and rn2 < 1:

		ES_current = ES_current - 1
		E_current = E_current + 1
		P_current = P_current + 1

pyplot.plot(E_array)
pyplot.plot(S_array)
pyplot.plot(ES_array)
pyplot.show()