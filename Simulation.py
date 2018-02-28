import random
import matplotlib.pyplot as plt
import numpy as np
d={};
l=['E','S','P','ES']
# 4 species

d['E']=[20]
d['S']=[30]
d['P']=[40]
d['ES']=[50]

R1=1/3;
R2=1/3;
R3=1/3;

a=[]

EndTime=100;

t=0;
i=1


while(t<EndTime):
    x=random.randrange(1,4);      # The reaction is randomly picked.
    RandomTime=random.random();    # Time is  randomly generated.
    if(x==1):
        # E + S -> ES
        
        d['E'].append(d['E'][i-1]-1);
        d['S'].append(d['S'][i-1]-1);        
        d['ES'].append(d['ES'][i-1]+1);
        d['P'].append(d['P'][i-1]);
        i=i+1;
        t=t+RandomTime
        a.append(t)

        
    if(x==2):
       # ES -> E + S
        
        d['ES'].append(d['ES'][i-1]-1);
        d['E'].append(d['E'][i-1]+1);        
        d['S'].append(d['S'][i-1]+1);
        d['P'].append(d['P'][i-1]);
        i=i+1;
        t=t+RandomTime
        a.append(t)

    if(x==3):

       # ES -> E + P
        
        d['ES'].append(d['ES'][i-1]-1);
        d['E'].append(d['E'][i-1]+1);        
        d['P'].append(d['P'][i-1]+1);
        d['S'].append(d['S'][i-1]);
        i=i+1;
        t=t+RandomTime
        a.append(t)

#print(len(a))
#print(len(d['E'][:len(a)]))
plt.xlabel('Time')
plt.ylabel('No. of Molecules')
plt.title('Count of the number of molecules')
plt.plot(d['E'][:len(a)],a,marker='o',label='E')
plt.legend()
plt.show()

plt.xlabel('Time')
plt.ylabel('No. of Molecules')
plt.plot(d['S'][:len(a)],a,marker='o',label='S')
plt.legend()
plt.show()

plt.xlabel('Time')
plt.ylabel('No. of Molecules')
plt.plot(d['P'][:len(a)],a,marker='o',label='P')
plt.legend()
plt.show()

plt.xlabel('Time')
plt.ylabel('No. of Molecules')
plt.plot(d['ES'][:len(a)],a,marker='o',label='ES')
plt.legend()
plt.show()

# The pics in folder are for one such example.
