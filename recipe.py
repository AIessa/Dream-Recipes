#CFG to compile information into a recipe
import json
import tracery
from tracery.modifiers import base_english
import pathlib

rules = {}
with open('rules.json', 'r') as f:
    rules.update( json.load(f))
grammar = tracery.Grammar(rules)


# rules = {

# "origin": ["#[myThing:#concreteNoun#][mySub:#substance#][myRec:#recipeType#]saying# Welcome to Dream Recipes. ...#[recDesc:#recDescription#][mainIngr:#animal#]intro# Happy cooking!"
# + "\n\nYou will need:"+ "\n#squant# #mainIngr# " #this sometimes gives things like "2 raven"
# + "\n#lquant.capitalize# of #liquid#."
# + "\n#lquant# #crazyIngred# "
# + "\n#lquant# of #liquid# "
# + "\n#solid.capitalize# for garnish "
# + "\nA medium-sized cauldron"

# + "\n\nMethods"+ "\n1. Take the #squant# #mainIngr#, and shred into #solAdj# pieces using a couple of forks. "
# + "\n2. Heat the cauldron over a flame, and add #lquant# of #liquid#. Add #squant# of #solAdj# #solid#, and #lquant# of #crazyIngred# to the mix."
# + "\n3. Once the pot starts to boil, add the #mainIngr# meat. Fry for 5 mins until crisp. "
# + "\n4. Stir the concoction until it reaches a #glowing#, #color#...now add #lquant# of #liquid#. We'll see it #glowing#, #color#...well, more of #color#ish #color#. "
# + "\n5. Cook for 15 mins to soak the #mainIngr# in the broth. You might need to add an extra ladleful of #liquid# to ensure the #myRec# is #totally# potent. "

# + "\n\n Our tried-and-true formula is sure to be a keeper. Simple ingredients, easy directions, and plenty of #concept# and #concept# make the #myRec# more #evaluationAdjBare# than ever. Best of all, it's totally customizable—add your favorite nutritious mix-ins such as fresh #crazyIngred#, sliced #substance#, or a dollop of #substance#."
# + "\n#concl# It won't be long until the effect takes place. Until then, goodnight, dear reader. And sweet dreams."],

# ## this is where user input gets passed
# "effectVerb":["conjure", "reveal", "repel", "lift", "mend", "transform", "increase"],
# "effect":["aging drinker temporarily", "causing a powerful infatuation within the drinker", "increasing one's brain power", "healing bruises in an hour", "causing the drinker to become infatuated with the giver of the potion"],

# #Intro and Conclusion
# "intro":["If you follow the steps of your chosen  #myRec#, it will achieve the desired effect of #recDesc#. The best time to administer this #myRec# is when #beingWith# the #natureNoun#. "],
# "concl":[" This was a simple recipe, one that you can try with your own #relative#, #youKnow#, #someday#. If not, #vagueReaction#."],

# }


def generate_recipe(category, effect, solid, liquid, main_ingredient):
	# check the category type and pass in rules
	rules_add = {
		#generate title with "effect" keyword
        "recipeType" : category,
        "effect": effect,
		"title": ["#recipeType.capitalize# : #effect#"],
		"origin": ["#[myThing:#concreteNoun#]title# \n\nWelcome to Dream Recipes. #[recDesc:#effect#][myRec:#recipeType#][liq1:#liquid#][liq2:#liquid#][cray:#crazyIngred#][crazy_quant:#squant#][liq2_quant:#lquant#][sol1:#solid#][sol2:#solid#]intro# Happy cooking! \n\nYou will need:\n#squant# of #mainIngr# \n#lquant.capitalize# of #liq1#\n#cray.capitalize# (#crazy_quant#)\n#sol1.capitalize#\n#liq2.capitalize# (#liq2_quant#) \n#sol2.capitalize# for garnish \nA medium-sized cauldron \n\nMethods\n1. Take #squant# of #mainIngr#, and shred into pieces using a couple of forks. \n2. Heat the cauldron over a flame, and add the #liq1# while stirring. Add the #solAdj# #sol1#, and #crazy_quant# of #cray# to the mix.\n3. Once the pot starts to boil, add the #mainIngr#. Fry for 5 mins until crisp.\n4. Stir the concoction until it reaches a #glowing#, #color#...now add #liq2_quant# of #liq2#. We'll see it #glowing#, #color#...well, more of #color#ish #color#.\n5. Cook for 15 mins to soak the #mainIngr# in the broth. You might need to add an extra ladleful of #liq1# to ensure the #myRec# is #totally# potent. \n6. Finally, transfer to bowl and garnish with #sol2#.\n\n#concl# It won't be long until the #myRec# will work its magic."],

		#pass ingredients to recipe, after splitting to solids and liquids
		# update with new lists
		#"ingred_list": ["\n\nYou will need:\n#squant# #mainIngr# \n#lquant.capitalize# of #liq1#\n#crazyIngred.capitalize# \n#solid1.capitalize#\n#lquant# of #liq2# \n#solid2.capitalize# for garnish \nA medium-sized cauldron"],
		"solid": solid,
		"liquid": liquid,
       	 	"mainIngr":main_ingredient,
		"concl":["Our tried-and-true formula is sure to be a keeper. Simple ingredients, easy directions, and plenty of #concept# and #concept# make the #myRec# more #evaluationAdjBare# than ever. Best of all, it's totally customizable — add your favorite nutritious mix-ins such as fresh #crazyIngred#, sliced #substance#, or a dollop of #substance#. This was a simple recipe, one that you can try with your own #relative#, #youKnow#, #someday#. If not, #vagueReaction#."]
	}

	for rule, options in rules_add.items():
		grammar.push_rules( rule, options )



	grammar.add_modifiers(base_english)
	print(grammar.flatten("#origin#"))


#generate_recipe(["remedy"], effect, solid, liquid, main_ingredient)
