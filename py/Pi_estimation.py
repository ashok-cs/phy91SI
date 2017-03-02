import random

def Pi_Estimation(n):
    inside=0
    
    for i in range(n):
        x=random.random()
        y=random.random()
        if x**2+y**2 <= 1:
            inside+=1
    return inside*4.0/n
    
#Test
N=100000
pi=Pi_Estimation(N)
print(pi)    