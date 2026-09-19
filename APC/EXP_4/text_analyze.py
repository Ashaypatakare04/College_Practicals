text = input("Enter text: ")

def vowels():
    v = 0
    v1 = "aeiouAEIOU"
    for i in text:
        if i in v1:
            v += 1
    print("Total no. of Vowels :", v)

def words():
    w = text.split()
    print("Total no. of words: ", len(w))

def freq():
    w = text.split()
    counts = {}
    for word in w:
        counts[word] = counts.get(word, 0) + 1
        
    print("\nFrequency of each word:")
    for word, count in counts.items():
        print(f"{word} : {count}")

def top_three():
    w = text.split()
    counts = {}
    for word in w:
        counts[word] = counts.get(word, 0) + 1
    

    sorted_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    
    print("\nTop 3 Most Frequent Words:")
    for word, count in sorted_words[:3]:
        print(f"{word} : {count}")


vowels()
words()
freq()
top_three()
