text = input("Enter text: ")

stopwords = {"is", "and", "the", "a", "an", "of", "to", "in"}

words = text.split()

result = [word for word in words if word.lower() not in stopwords]

print("Cleaned text:", " ".join(result))
