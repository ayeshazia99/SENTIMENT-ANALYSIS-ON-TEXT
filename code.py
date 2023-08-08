

pip install nltk

import nltk
nltk.download('punkt')

pip install textblob

pip install newspaper3k

from textblob import TextBlob
from newspaper import Article
url="https://en.wikipedia.org/wiki/Python_(programming_language)" #enter the url of any site whose sentiment you want to analyze

article=Article(url) #object to get article into script
article.download()
article.parse() #to get all the html out of it
article.nlp() #to prepare it for natural language processing

#text=article.text = displays the entire text
text=article.summary #gives summary of the text
print(text)

#<0 is the most negative score for sentiment
#>0 is the positive score

blob=TextBlob(text)
sentiment=blob.sentiment.polarity #to obtain the sentiment score
print(sentiment)

"""You can even create your text file and then determine its sentiment
Following is an example of how to do so:
"""

#create a sample text file(for e.g:file.txt)

with open('file.txt','r') as f:
  text=f.read

blob=TextBlob(text)
sentiment=blob.sentiment.polairty
print(sentiment)







