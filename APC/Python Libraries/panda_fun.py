import pandas as pd
df=pd.read_csv("data.csv")
print(df)

h=df.head()
print("\nFirst 5 rows:\n",h)

t=df.tail()
print("\nLast 2 rows:\n",t)

s=pd.Series(df['Name'])
print("\nSeries:\n",s)

d=pd.DataFrame(df)
print("\nDataframe:\n",d)

d1=pd.DataFrame(df[["Name","Marks"]])
print(d1)

print("\nNo. of rows & Column:\n",df.shape)

print("\nName of columns:\n",df.columns)

print("\nFiltering student by marks:\n",df[df["Marks"] > 80])

print("Total marks:", df["Marks"].sum())

print("Average marks:", df["Marks"].mean())

print("Highest marks:", df["Marks"].max())

print("Lowest marks:", df["Marks"].min())