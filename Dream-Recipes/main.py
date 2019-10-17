#dream recipe bot - main! This is the 'UI' part

#imports
import sys
import os
import time
#import other scripts for ingredient retrieval & recipe creation
#ingredients.py + recipe.py


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
    specify_ingredients(type)

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
    specify_ingredients(type)

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
    specify_ingredients(type)


#
#
#specifying ingredients if any
def specify_ingredients(type):
    yes_no = input('Oh yes, did you want to include any specific ingredients?\n')
    extra_ingredients = 'none'
    if yes_no == 'yes':
        os.system('clear')
        time.sleep(1)
        ingredients = input('Aha, which ones?\n')
        os.system('clear')
        time.sleep(1)
        print('... I... see. Very well. I will do my best. Will be right back!\n\n')
        extra_ingredients = ingredients
        get_ingredients(type, extra_ingredients)
    elif yes_no == 'no':
        os.system('clear')
        time.sleep(1)
        print('ok, I will be right back!\n\n')
        get_ingredients(type, extra_ingredients)
    else:
        os.system('clear')
        time.sleep(1)
        print('Let me see what I can do with that information... I will be right back!\n\n')
        extra_ingredients = yes_no
        get_ingredients(type, extra_ingredients)


#
#
#give user chance to specify ingredients, function calls 'make_recipe'!
def get_ingredients(type, extra_ingredients):
    time.sleep(2)
    os.system('clear')
    print('[rustling noises]')
    time.sleep(2)
    os.system('clear')
    print('[cursing]')
    time.sleep(1)
    os.system('clear')
    print('AHA! Found it!\n')
    time.sleep(3)
    #
    recipe = make_recipe(type, extra_ingredients)
    #
    if extra_ingredients != 'none':
        print('A '+ type +' that contains '+extra_ingredients+'!\n\n')


#
#
#actually compiling appropriate recipe based on type & extra_ingredients (check for 'none')
#uses external functions
def make_recipe(type, extra_ingredients):
    recipe = []

    #(2) get ingredients: from dataset
    #separately: train word vectors
    #import word vec categories to retrieve similar words from prompt
    # call ingredients.py

    #(3) CFG
    #figure out how to define grammar from tracery
    #variable for ingredient list
    # call recipe.py

    return recipe







#___________________________________________________________________________
#RUN MAIN <3
if __name__ == "__main__":
    print('\n\n\nWelcome to my store! Here you can get a recipe to make any dream come true.')
    time.sleep(1)
    print('\nTell me, what are you looking for today? \n\n ------------')
    time.sleep(1)
    prompt_and_react_1()
