b1={'apple','terminal','view'}
b2={'explorer','terminal','chat'}
print("all unique words used in each book: ",b1.union(b2))
print("common words between both books: ",b1.intersection(b2))
print("words that are unique to each book: \n","book1: ",b1.difference(b2),"\nbook2: ",b2.difference(b1))
u=0
for i in b1.union(b2):
    u+=1
print("the total number of unique words across both books: ",u)
