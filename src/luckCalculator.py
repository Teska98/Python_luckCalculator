from random import randrange
sumaNovca=int(input())
ciljaniIznos=int(input())
ulog=int(input())
pocetniUlog= ulog
pocetnaSumaNovca=sumaNovca

tacniRezultati=0
for i in range(0,10000):
    sumaNovca=pocetnaSumaNovca
    ulog=pocetniUlog
    while ulog<ciljaniIznos:
        sansa=randrange(0,100)
        if sansa<=49:
            ulog=ulog*2
        if sansa >49:
            ulog=pocetniUlog
            sumaNovca=sumaNovca - pocetniUlog
            if sumaNovca < 0:
                break
    if sumaNovca<0:
        continue
    tacniRezultati += 1
sansaZaDobitak= float(tacniRezultati/10000)
print("Sansa za dobitak ", sansaZaDobitak)
