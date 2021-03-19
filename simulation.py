#UCL DRAW SIMULATION
clubs = ['LIVERPOOL','MANCHESTER CITY','CHELSEA','BAYERN MUCHEN',
        'BORUSSIA DORTMUND','REAL MADRID','PSG','FC PORTO',]
pairings = []
qf = 0

import random
while (len(clubs) > 0):
    qf += 1
    draw_home = clubs.pop(random.randrange(len(clubs)))
    draw_away = clubs.pop(random.randrange(len(clubs)))
    pairings.append((draw_home, draw_away))
    print('คู่ที่ {}: '.format(qf), draw_home, ' VS ', draw_away)

print('Pairings :' , pairings)