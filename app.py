import pandas as pd
df = pd.DataFrame({ "Name": ["Alice", "Bob"], "Cgpa": [9.5, 8.7] })
s = pd.Series([23, 24, 25, 26]) 
print(s) 
print(type(s)) 

# Indexing
print(s[0]) # 23
print(s[2]) # 25 
print(s.index)# all labels