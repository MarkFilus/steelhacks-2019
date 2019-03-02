import os
from textgenrnn import textgenrnn
import pickle
import sys




def load_data():
    path = os.path.join(os.getcwd(), 'sample_text.txt')
    text = open(path).read().lower()
    print('corpus length:', len(text))


def get_img(img_name):
    path = os.getcwd() + "/samplememes/"
    img = path + img_name
    return img


def main():
    textgen = textgenrnn()
    textgen.train_from_file(sys.argv[1], num_epochs=1, temperature=[1.0])
    with open('model.pkl', 'wb') as f:
        pickle.dump(textgen, f)


if __name__ == '__main__':
    main()
