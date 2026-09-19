import nltk
nltk.download('stopwords')
nltk.download('punkt') 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 

stop_words = set(stopwords.words('english'))
words = "they are trying hard to win."

tokenized_words = word_tokenize(words.lower()) 

text1 =[] 

for w in tokenized_words:
    if w not in stop_words:
        text1.append(w)
        
print(text1)
