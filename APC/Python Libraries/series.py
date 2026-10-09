import pandas as pd
d= pd.read_csv("std.csv")
series=d["Name"]
print("Series:\n")
print(series)

print("\nDataframes:\n")
df=pd.DataFrame(d)
print(df)