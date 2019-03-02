# steelhacks-2019


## get_memes.py 
*  executable downloads all the memes into a folder
* USAGE: `python3 get_memes.py output_folder`

## categorize_memes.py  
* seperate files in given folder based on similarity (template discovery)
* USAGE: `python3 categorize_memes.py meme_dir`

## get_text.py
* uses ocr to get text from images in given directory, splits image in half, separates top and bottom text with sentinel value
* USAGE `python3 get_text.py meme_input_dir output_dir`

## train_meme.py
* uses the train model
* USAGE: `python3 train_meme.py meme_template_folder out_model.pkl`

## gen_meme.py
* uses model for specific template to predict/generate text for a new meme
* USAGE: `python3 gen_meme.py model.pkl background.jpg`
