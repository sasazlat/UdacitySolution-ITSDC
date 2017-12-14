#Modify the move function to accommodate the added
#probabilities of overshooting or undershooting
#the intended destination.
p = [1, 2, 3, 4, 5]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = p
    #for i in range(len(p)):
    #    q.append(p[(i - U) % len(p)])


    #U = U % len(p)
    #q = p[-U:] + p[:-U]

    i = U = U % len(p)
    while i > 0:
        q = q[-1:] + q[:-1]
        i -= 1 

    for i in q:
        i = i 
    return q
    

print(move(p, 3))

