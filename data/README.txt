Missing, because of large file size:
- fil9 (preprocessed wikipedia corpus using wikifil.pl)
- model.bin (language model trained using fasttext and fil9)

(ingredient_dict.pickle was just added as an example. With this set of encoded vectors alone you can't yet run the program, it requires the model!)

To run the code, you can train a model yourself (this might take a few hours depending on your computer and the parameters). 
Simply follow the instructions here: https://fasttext.cc/docs/en/unsupervised-tutorial.html
This tutorial also provides a corpus to train the model on, but feel free to use a different one.
You can also find the code and the parameters we used to do this in 'ingredients.py'.


