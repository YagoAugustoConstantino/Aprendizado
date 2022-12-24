inicial = int(input('Qual numero vc quer a tabuada?'))
tabuada = int(input(' ate qual tabuada?'))
x=inicial
y=0
while y < tabuada:
    y=y+1
    if y<tabuada*x:
        print('a tabuada de {} X {} é igual a :{}'.format(x,y,x*y))
from pandas import * 

