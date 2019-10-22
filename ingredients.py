"""
Resources:
https://fasttext.cc/docs/en/unsupervised-tutorial.html
    Note: fasttext has some bugs now, but I'm having trouble installing the
    newer versions or adjustments. That means that I can't use some of the
    extremely handy features like:
    model.get_nearest_neighbors('x')
    model.get_analogies('x')
    --> If I can't find the fix I will just use a different package to
    calculate vector similarity/find nearest neighbours since the output vectors
    are just numpy arrays that can be used without problem.

"""

# ingredient retrieval

#imports -----------------------------------------------------------------------
import fasttext
import numpy as np
import math
from operator import itemgetter
import pickle

#
#
# off-line: training the model -------------------------------------------------
"""
Training the language model with parameters:
    - file: preprocessed chunk of wikipedia corpus
    - type of model: skipgram, better for learning sub-word context
    - epoch: training for 4 epochs, default is 5
    - thread: has to do with how many CPU cores computer has (I have 4),
    so it makes sense to adjust the number of threads fasttext uses to avoid killing your computer...
    - default parameters:
        100 dim vectors
        takes into account subwords between 3-6 characters
        learning rate = 0.05
"""
#model = fasttext.train_unsupervised('data/fil9', "skipgram", epoch = 4, thread=4)
#model.save_model("data/model.bin")


#
#
# off-line: embedding ingredients and saving set of ingredient vectors ---------
"""
model = fasttext.load_model('data/model.bin')
ingredient_list = open('data/ingredients.txt').read().split('\n')[:-1]
print('loaded stuff')

ingredient_arrays = [(x,model.get_word_vector(x.split(',')[0])) for x in ingredient_list]
    #list of tuples with the ingredient arrays (type = numpy.ndarray)
print('got vectors')

#save arrays as dictionary
ingredient_dict = dict(ingredient_arrays)

with open('data/ingredient_dict.pickle', 'wb') as handle:
    pickle.dump(ingredient_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

print('all pickled')
"""

#
#
# online: retrieval! -----------------------------------------------------------
def find_nearest(key_array, n):

    #load ingredient dictionary
    with open('data/ingredient_dict.pickle', 'rb') as handle:
        ingredient_dict = pickle.load(handle)

    #initialize
    choices = [('starter',100)]
    max = ('starter',100) #set max to infinity at the start

    #find n nearest neighbours
    for ingr , arr in ingredient_dict.items():

        #calculate distances
        dist = np.linalg.norm(key_array-arr)

        #only add ingredient to choices if:
        #there are <n ingredients in list
        if len(choices)< n:
            choices.append((ingr,dist))
        #if list is full, check if worst entry can be replaced
        elif dist < max[1]:
            choices.append((ingr,dist))
            choices.remove(max)

        #update max entry either way
        max = choices[0]
        for tup in choices:
            if tup[1] > max[1]:
                max = tup

    return choices


#get ingredients for keywords:
model = fasttext.load_model('data/model.bin')

keywords = ['awake']
number_each = int(10/len(keywords))
result = []
for word in keywords:
    arr = model.get_word_vector(word)
    nearest = find_nearest(arr,number_each)
    result = result + nearest
    print(word + ' : ')
    print(nearest)


print('\nIngredient list:')
print(result)
