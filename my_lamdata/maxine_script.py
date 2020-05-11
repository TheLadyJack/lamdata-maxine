from pandas import DataFrame

from my_lamdata.my_mod import enlarge
print("Hello")

df = DataFrame({"A":[1,2,3], "B":[4,5,6]})
print(df.head())

x = 413
print(enlarge(x))