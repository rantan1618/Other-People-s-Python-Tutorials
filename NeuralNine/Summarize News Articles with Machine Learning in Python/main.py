import tkinter as tk
import nltk
# from textblob import Textblob
from newspaper import Article

nltk.download('punkt')


url = "https://www.cnn.com/2022/10/11/politics/joe-biden-interview-cnntv/index.html"

article = Article(url)

article.download()

article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')

analysis = Textblob
