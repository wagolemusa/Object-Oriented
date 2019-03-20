c = "ABCDE"

r = range(0,3)
from  pprint import pprint as pp 

x = [{str(y) + ltr: 'Empty' for ltr in c } for y in r]
x[0]['0A']='musa'
pp(x)