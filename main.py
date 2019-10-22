#dream recipe bot - main! This is the 'UI' part

#imports
import sys
import os
import time
import random
from nltk import word_tokenize
from nltk.corpus import stopwords
import string
#import other scripts for ingredient retrieval & recipe creation
#ingredients.py + recipe.py
import ingredients
import recipe


#___________________________________________________________________________
#(1) retrieve prompt/cue (chatbot intro with choices)

#
#
#ask user for type of recipe
def prompt_and_react_1():
    prompt1 = '\n 1 - a remedy/protection \n 2 - a poison \n 3 - a potion to enhance your abilities / gain magical powers like concentration or flying! \n\n Type option 1, 2 or 3 to proceed!\n >> '
    text = input(prompt1)
    os.system('clear')
    time.sleep(1)
    try:
        choice = int(text)
        if choice == 1:
            remedy()
        elif choice == 2:
            poison()
        elif choice == 3:
            superpower()
        else:
            print('\nSorry, I do not think I can help you with that. Let me remind you of the options...')
            prompt_and_react_1()
    except:
        print('\nSorry, I do not think I can help you with that. Let me remind you of the options...')
        prompt_and_react_1()


#
#
#ask user for purpose, depending on type
def remedy():
    type = 'remedy'
    print('\nA remedy or protection.. Ah, I hope I can help you, do not fear!\n')
    time.sleep(1)
    remedy = input('What do you need this for?\n')
    time.sleep(1)
    os.system('clear')
    print(remedy+'!\n')
    time.sleep(1)
    print('Well, let me have a look. I am sure I had the right book here just a minute ago...\n')
    time.sleep(1)
    specify_ingredients(type,remedy)

def poison():
    type = 'poison'
    print('\nPOISON! Ok, well, I hope you know what you are doing.\n')
    time.sleep(1)
    poison = input('What should the effect of the poison be?\n')
    time.sleep(1)
    os.system('clear')
    print(poison+'!\n')
    time.sleep(1)
    print('Well, let me have a look. \nYou are really making me go to THAT part of my library, hm?\n')
    time.sleep(1)
    specify_ingredients(type,poison)

def superpower():
    type = 'superpower'
    print('\nAh yes, self improvement! superpowers! Those recipes are in demand these days. Let me see..\n')
    time.sleep(1)
    superpower = input('What power would you like to obtain?\n')
    time.sleep(1)
    os.system('clear')
    print(superpower+'!\n')
    time.sleep(1)
    print('Well, let me have a look. I will find a good recipe for you...\n')
    time.sleep(1)
    specify_ingredients(type,superpower)


#
#
#specifying ingredients if any
def specify_ingredients(type, effect):
    yes_no = input('Oh yes, did you want to include any specific ingredient?\n')
    extra_ingredient = 'none'
    if 'yes' in yes_no or 'yep' in yes_no or 'ok' in yes_no:
        os.system('clear')
        time.sleep(1)
        ingredients = input('Aha, which one?\n')
        os.system('clear')
        time.sleep(1)
        print('... I... see. Very well. I will do my best. Will be right back!\n\n')
        extra_ingredient = ingredients
        compile_ingredients(type, effect, extra_ingredient)
    elif 'no' in yes_no or 'nah' in yes_no or 'nope' in yes_no:
        os.system('clear')
        time.sleep(1)
        print('ok, I will be right back!\n\n')
        extra_ingredient = 'none'
        compile_ingredients(type, effect, extra_ingredient)
    else:
        os.system('clear')
        time.sleep(1)
        print('Let me see what I can do with that information... I will be right back!\n\n')
        extra_ingredient = yes_no
        compile_ingredients(type, effect, extra_ingredient)


#
#
#give user chance to specify ingredients, function automatically triggers recipe.py!
def compile_ingredients(type, effect, extra_ingredient):
    time.sleep(2)
    os.system('clear')
    print('[rustling noises]')
    time.sleep(2)

    #We want the ingredients to be related to the type of recipe and the effect
    keywords = []
    #first choose a type related keyword
    if type == "poison":
        keywords.append(random.choice(['venom','poison','toxin']))
    elif type == "remedy":
        keywords.append(random.choice(['treatment','cure','medicine','drug']))
    else:
        keywords.append(random.choice(['power','super','ability','improvement','boost','']))
    #now remove stopwords from effect
    remove = stopwords.words('english') + list(string.punctuation)
    effect_tok = [i for i in word_tokenize(effect.lower()) if i not in remove]
    keywords = keywords + effect_tok
    #
    print(keywords)
    time.sleep(2)
    #

    os.system('clear')
    print('[cursing]')
    time.sleep(2)
    os.system('clear')

    #Retrieve extra ingredients and sort them into liquid and solid
    ingredient_list = [ing for (ing,num) in ingredients.get_ingredients(keywords)]
    #sort liquid and solid
    liquids = open('data/liquids.txt').read().split('\n')[:-1]
    choice_liq = list(set([ing for ing in ingredient_list if (ing in liquids)]))
    choice_sol = list(set([ing for ing in ingredient_list if not(ing in liquids)]))
    #there is a chance that not enough liquids have been found, so quick fix:
    if len(choice_liq)<2:
        choice_liq = choice_liq + ['aether','toothpaste']
    if len(choice_sol)<2:
        choice_sol = choice_sol + ['bread','doll eyes']
    time.sleep(2)
    #

    print('\nAHA! Found it! Here it is...\n')
    time.sleep(1)
    print('\n\n*********************\n')

    #call generate recipe function from recipe.py
    if extra_ingredient != 'none':
        print('A recipe for a '+ type +' that contains '+extra_ingredient+'!\n\n')
        recipe.generate_recipe([type],[effect], choice_sol, choice_liq, [extra_ingredient])
    else:
        recipe.generate_recipe([type],[effect], choice_sol, choice_liq, ['weirdly solid ice cream','the thing under your bed','socks','wool of a young sheep'])





#___________________________________________________________________________
#RUN MAIN <3
if __name__ == "__main__":
    os.system('clear')
    print('\n\n\nWelcome to my store! Here you can get a recipe to make any dream come true.')
    time.sleep(1)
    print('\nTell me, what are you looking for today? \n\n ------------')
    time.sleep(1)
    prompt_and_react_1()
    print('\n*********************\n\nWell, hope this helps! Bye bye.')
