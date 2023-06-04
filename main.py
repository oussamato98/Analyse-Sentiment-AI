from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import string
import re
import collections

ps = PorterStemmer()
wl = WordNetLemmatizer()

text = "It was one of the worst movies, 56 - ? despite good ."
new_text = "It was one of the worst movies, 56 - ? despite good . the movie was bad. horses, eating!"

print("---------------TEXT--------------")
print(text)
print("")

print("---------------TOKENIZATION AND LOWER CASE--------------")
# convert to lowercase
new_text = new_text.lower()
# tokenize the text into words
tokens = word_tokenize(new_text)
print(tokens)

print("---------------NORMALIZATION--------------")
# normalization
normalized_text = re.sub(r"[^a-zA-Z0-9]", " ", new_text)
# remove numbers
normalized_text = re.sub(r"\b\d+\b", "", normalized_text)
normalized_text = normalized_text.split()
print(normalized_text)

print("---------------REMOVE STOP WORDS--------------")
# load stopwords
stop_words = set(stopwords.words("english"))
# remove stop words
filtered_text = [word for word in normalized_text if word not in stop_words]
print(filtered_text)

print("---------------STEMMING--------------")
# Stemming
stemmed_text = [ps.stem(word) for word in filtered_text]
print(stemmed_text)

print("---------------LEMMATIZING--------------")
# Lemmatizing
lemmatized_text = [wl.lemmatize(word) for word in filtered_text]
print(lemmatized_text)

print("-----------------OCCURRENCES--------------------------------")
# word occurrences
word_counts = collections.Counter(lemmatized_text)
print(word_counts)
print(word_counts['one'])

print("---------------POSITIVITY/NEGATIVITY--------------")
positive_words = open("positive-words.txt", "r").read()
negative_words = open("negative-words.txt", "r").read()
positive_words = positive_words.splitlines()
negative_words = negative_words.splitlines()
positive_score = 0
negative_score = 0
neutral_score = 0

words = lemmatized_text
positive_word_count = 0
negative_word_count = 0

for word in words:
    if word in positive_words:
        positive_score += word_counts[word]
        positive_word_count += 1
        print(word + ": (+" + str(word_counts[word]) + "*1)")
    elif word in negative_words:
        negative_score += word_counts[word]
        negative_word_count += 1
        print(word + ": (-" + str(word_counts[word]) + "*1)")
    else:
        neutral_score += 1
        print(word + ": (0*1)")

score = positive_score - negative_score
print("The score is:", score)

print("Positive word count:", positive_word_count)
print("Negative word count:", negative_word_count)

print("---------------SENTIMENT OF THE TEXT--------------")
# Deciding if it is positive or negative
if positive_word_count > negative_word_count:
    print("The text is positive.")
elif positive_word_count < negative_word_count:
    print("The text is negative.")
else:
    print("The text is neutral.")
