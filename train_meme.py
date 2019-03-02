import numpy as np
import os
from textgenrnn import textgenrnn

def generate(file_name):
    textgen = textgenrnn()
    textgen.train_from_file(file_name, num_epochs=1)
    textgen.generate()

def load_data():
    path = os.path.join(os.getcwd(), 'sample_text.txt')
    text = open(path).read().lower()
    print('corpus length:', len(text))

# Input:
''' 
Image format
Upvotes
Top text
Bottom text
'''

def get_img(img_name):
    path = os.getcwd() + "/samplememes/"
    img = path + img_name
    return img


def main():
    file_name = os.path.join(os.getcwd(), 'sample_text.txt')
    generate(file_name)

if __name__ == '__main__':
    main()
