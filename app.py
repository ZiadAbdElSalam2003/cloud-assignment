import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
import gensim
from gensim.utils import simple_preprocess
file1 = open('C:\\Users\\gate\\OneDrive\\Desktop\\random_paragraphs.txt',"r")
print(file1.readable())
content=file1.read()
english_stopwords=stopwords.words("english")
english_stopwords
text=[]
for word in gensim.utils.simple_preprocess(content):
    if word not in english_stopwords:
        text.append(word) 
file2 = open('C:\\Users\\gate\\OneDrive\\Desktop\\yes.txt',"w") #save the text to sure that no stopwords
file2.write(" ".join(text))
d=dict()
for element in text:
    if element in d:
        d[element]= d[element]+1
    else:
        d[element]=1
print(d)     
