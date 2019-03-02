# USAGE
# python ocr.py --image images/example_01.png 
# python ocr.py --image images/example_02.png  --preprocess blur
# import the necessary packages
from __future__ import division
import pytesseract
from PIL import Image
import cv2
import argparse
import math
import os
import time
import glob
import re
from spellchecker import SpellChecker
import pickle
import string
sentences = []
spell = SpellChecker()
spell.distance = 2
# find those words that may be misspelled

#    Simple image to strin
files_list = glob.glob('input10\*')
def long_slice(image_path, out_name, outdir, slice_size):
    """slice an image into parts slice_size tall"""
    img = Image.open(image_path)
    width, height = img.size
    upper = 0
    left = 0
    slices = int(math.ceil(height/slice_size))
    count = 1
    name_num = 0
    for slice in range(slices):
        #if we are at the end, set the lower bound to be the bottom of the image
        if count == slices:
            lower = height
        else:
            lower = int(count * slice_size)  
        #set the bounding box! The important bit     
        bbox = (left, upper, width, lower)
        working_slice = img.crop(bbox)
        upper += slice_size
        #save the slice
        working_slice.save(os.path.join(outdir, "slice" + out_name + str(name_num)+".tiff"))
        count +=1
        

        if name_num == 3:
            name_num = 0
        name_num = name_num+1


#print (crop_height)
for file in files_list:
    image = Image.open(file)
    width, height = image.size
    crop_height = (height/4) 
    long_slice(file,"",'C:\\Users\\samyu\\OneDrive\\Documents\\Code\\Cloud Computing\\ocr\\slices',crop_height)
    my_count= 0
    while(my_count<2):
        if my_count == 0:
            args = {"image":"C:\\Users\\samyu\\OneDrive\\Documents\\Code\\Cloud Computing\\ocr\\slices\\slice0.tiff","preprocess":"thresh"}
        elif my_count == 1:
            args = {"image":"C:\\Users\\samyu\\OneDrive\\Documents\\Code\\Cloud Computing\\ocr\\slices\\slice3.tiff","preprocess":"thresh"}

        image = cv2.imread(args["image"])
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if args["preprocess"] == "thresh":
            gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
        elif args["preprocess"] == "blur":
            gray = cv2.medianBlur(gray, 3)
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, gray)
        text = pytesseract.image_to_string(Image.open(filename),lang = 'Joh+Impact')
        text_list = re.split(r'\W+', text)
        #print(text_list)
        misspelled = spell.unknown(text_list)
        itemlist = []
        for word in misspelled:
        # Get the one `most likely` answer
            word = word.lower()
            word = word.translate(str.maketrans('','',string.punctuation))
            if word == '':
                continue
            #print(word)
            itemlist.append(word)
            itemlist.append(spell.correction(word))
        sentence = ' '.join(itemlist)
        #sentence = sentence + '\n'
        #print(sentence)
        with open("output5.txt", "a") as f:
            f.write(sentence)
            f.write('\n')
            f.close()
        #time.sleep(.2)
        #print(text)
        os.remove(filename)
        my_count+=1
#print(itemlist)
