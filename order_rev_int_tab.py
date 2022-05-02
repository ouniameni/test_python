import random


tab=[]

tab=[random.randrange(1,100) for i in range (14)]
   

print(tab)
def tri(tab):
    for t in range (0,14):
        max=t
        for p in range(t+1,14):
    
            if tab[p]>tab[max]:
             max=p
        tmp=tab[t]
        tab[t]=tab[max]
        tab[max]=tmp

tri(tab)
print(tab)