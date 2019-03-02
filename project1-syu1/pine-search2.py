# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:58:51 2019

@author: samyu
"""
import glob, os, nltk, pandas,string, json, math
from string import digits
from nltk.stem.porter import PorterStemmer
# Setup
porter = PorterStemmer()
remove_digits = str.maketrans('', '', digits)

# Clean word
def clean_words(word_list):
    for i,word in enumerate(word_list):
        word = word.lower()
        word = word.translate(str.maketrans('','',string.punctuation))
        word = porter.stem(word)
        word = word.translate(remove_digits)
        word_list[i] = word
    return word_list

class Weighted:
  def __init__(self, document, num_appearence):
    self.document = document
    self.num_appearence = num_appearence
# Query is going to be a string
def num_words_in_query(query):
    # This is kinda hacky haha I hope you can understand it
    query_count = len(query.split())
    return query_count
def get_words_list(query):
    words_list = query.split()
    return words_list

json_file = open("inverted-index.json","r")
json_file = json.load(json_file)
key_word_file = open("keywords.txt","r")
# Split like this so we can track multiple keywords
key_word_list = key_word_file.read().splitlines()
key_word_list = clean_words(key_word_list)
