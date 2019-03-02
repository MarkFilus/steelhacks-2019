import os
from textgenrnn import textgenrnn
import pickle
import sys


def generate(file_name):
    textgen = textgenrnn()
    textgen.train_from_file(file_name, num_epochs=1, return_as_list=True)
    return textgen.generate()


def load_data():
    path = os.path.join(os.getcwd(), 'sample_text.txt')
    text = open(path).read().lower()
    print('corpus length:', len(text))


def get_img(img_name):
    path = os.getcwd() + "/samplememes/"
    img = path + img_name
    return img


def main():
    generate_list = generate(sys.argv[1])
    with open('list.pkl', 'wb') as f:
        pickle.dump(generate_list, f)


if __name__ == '__main__':
    main()
