import pandas as pd
print(pd.__version__)

datal = ['a','b','c','d','e']
print(datal)
print("자료형:", type(datal))

srl = pd.Series(datal)
print("자료형:", type(srl))

print(srl)

print(srl.loc[0])

print(srl.loc[1:3])

