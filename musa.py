import random 
REVENUE = random.randint(5, 200)
EBITDAMGN = random.randint(20, 65)/100
MULT = random.randint(5.0, 20.0)
DEBTPCT = random.randint(0, 75)/100
EBCAGR = random.randint(0, 10)/100

ENTRYEQ = REVENUE * EBITDAMGN * MULT *(1-DEBTPCT)
ENTRYDEBT = REVENUE * EBITDAMGN * MULT * (DEBTPCT)
EXITEQ = (REVENUE * EBITDAMGN * ((1+EBCAGR)**5) )* MULT - ENTRYDEBT
PROFIT = EXITEQ - ENTRYEQ
MOIC = EXITEQ/ENTRYEQ

print (REVENUE)
print (EBITDAMGN)
print (MULT)
print (DEBTPCT)
print (EBCAGR)
print (PROFIT)
print (MOIC)