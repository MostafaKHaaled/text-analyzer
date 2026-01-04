import nltk

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
import string
from nltk.corpus import stopwords
nltk.download('punkt_tab')
nltk.download('stopwords')



with open("sample_text.txt", encoding="utf-8", errors="ignore") as file:
    text = file.read()

print ("\nthis is text has Stop Word\n")


sentences = sent_tokenize(text)
sentence_count = len(sentences)
wordswithstop_word = word_tokenize(text)

words = [
    word.lower().strip()
    for word in wordswithstop_word
    if word.strip().isalpha()
]

word_count_withstop_word = len(words)

freq_dist = FreqDist(words)
top_10_words = freq_dist.most_common(10)

print("Sentence count:", sentence_count)
print("Word count:", word_count_withstop_word)
print("\nTop 10 most frequent words:")
for word, count in top_10_words:
    print(f"{word}: {count}")

print('*' * 50)########################################

print ("this does not text has Stop Word\n")
sentences = sent_tokenize(text)
sentence_count = len(sentences)
print("Sentence count:" ,sentence_count)

words_has_stop = word_tokenize(text)
stop_words = set(stopwords.words('english'))

filtered_words = [w for w in words if w.lower().strip() not in stop_words]
print("Word count:",len(filtered_words))

freq_dist_lis = FreqDist(filtered_words)
top_10_words = freq_dist_lis.most_common(10)

print("\nTop 10 most frequent words:")
for word, count in top_10_words:
    print(f"{word}: {count}")