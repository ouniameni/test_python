import random


tab=[]

tab=[random.randrange(1,100) for i in range (14)]
   

print(tab)
def tri(tab):
    for t in range (0,14):
        min=t
        for p in range(t+1,14):
    
            if tab[p]<tab[min]:
             min=p
        tmp=tab[t]
        tab[t]=tab[min]
        tab[min]=tmp

tri(tab)
print(tab)