import nltk
nltk.download('punkt_tab')
word_data="It originated from idea"
nltk_tokens=nltk.word_tokenize(word_data)
print(nltk_tokens)