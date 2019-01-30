# manually

# load data from file
filename = 'metamorphosis.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

# text split
words = text.split()
print("Just after normal spliting and the length of the list of words is :")
print(len(words))
print(words[:100])

# results
#['One', 'morning,', 'when', 'Gregor', 'Samsa', 'woke', 'from', 'troubled', 'dreams,', 'he', 'found', 'himself', 'transformed', 'in', 'his', 'bed', 'into', 'a', 'horrible', 'vermin.', 'He', 'lay', 'on', 'his', 'armour-like', 'back,', 'and', 'if', 'he', 'lifted', 'his', 'head', 'a', 'little', 'he', 'could', 'see', 'his', 'brown', 'belly,', 'slightly', 'domed', 'and', 'divided', 'by', 'arches', 'into', 'stiff', 'sections.', 'The', 'bedding', 'was', 'hardly', 'able', 'to', 'cover', 'it', 'and', 'seemed', 'ready', 'to', 'slide', 'off', 'any', 'moment.', 'His', 'many', 'legs,', 'pitifully', 'thin', 'compared', 'with', 'the', 'size', 'of', 'the', 'rest', 'of', 'him,', 'waved', 'about', 'helplessly', 'as', 'he', 'looked.', '"What\'s', 'happened', 'to', 'me?"', 'he', 'thought.', 'It', "wasn't", 'a', 'dream.', 'His', 'room,', 'a', 'proper', 'human']
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
# convert to lower case
tokens = [w.lower() for w in tokens]
print("After Using NLTK and converting to lower case : ")
print(words[:100])

# remove all tokens that are not alphabetic
words = [word for word in tokens if word.isalpha()]
print("After discarding all the special letter and keeping the only words, the length is :")
print(len(words))
print(words[:100])

# Even the unnecessary words like the, is , an , fullstop comma can be removed. NLTK is amazing in itselnltk.download('stopwords')
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
print("The stop words present are :")
print(stop_words)

# remove the stopwords
words = [word for word in words if not word in stop_words]
print("The final filtered out :")
print("The length of list decreased to")
print(len(words))
print(words[:100])

#The list of words decreased from 21904 to 9919. Gosh, the data is now relianle and kind of clean. 
#Try to think of a method to keep the adjective only and remove the noun. 