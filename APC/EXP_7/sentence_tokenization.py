import nltk
nltk.download('punkt_tab')
sent_data="Hello world! Dr. Smith went to the U.S. to attend a conference. It was very successful."
nltk_tokens=nltk.sent_tokenize(sent_data)
print(nltk_tokens)
