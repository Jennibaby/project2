import random

from bs4 import BeautifulSoup
import requests
import nltk
import json
import keyWords
import re
from fractions import Fraction
import string
#from en import verb
from nltk.stem.wordnet import WordNetLemmatizer
from collections import OrderedDict

indian = [
    ["ajwain"],
    ["amchoor"],
    ["asafoetida"],
    ["black cumin seends"],
    ["black mustard seeds", "brown mustard seeds"],
    ["cardamom"],
    # ["brown cardamom", "black cardamom"],
    # ["turmeric"],
    ["nigella"],
    ["whiite poppy seeds"],
    ["smoked turkey"],
    ["turkey breast"], # swapped places of turkey breast and turkey so will replace above first
    ["turkey bacon"],
    ["turkey sausage"],
    ["turkey"],
    ["lamb"],
    ["ground lamb"],
    ["lamb ribs"],
    ["lamb shank"],
    ["lamb shoulder"],
    ["sirloin chop lamb"],

# ["Boneless lamb leg"],
# ["Bone-in Lamb leg"],

    ["Naan"]

]

non_indian = [
    ["dried thyme", "mild oregano"], # marjoram, dried tarragon, cumin
    ["lime juice", "lime powder"],
    ["garlic powder"],
    ["sesame seeds"],
    ["wasabi", "horseradish"],
    ["1/2 cinnamon, 1/2 nutmeg", "1/2 cinnamon, 1/2 ginger", "1/2 cinnamon, 1/2 ground cloves"], #nutmeg
    # [""],
    # [""],
    ["celery seeds", "oregano", "sesame seeds"], # cumin seeds
    ["poppy seeds"], # consider removing
    ["ham"],
    ["pork chop", "pork loin"], # TODO consider removing pork substitutions
    ["bacon"],
    ["pork sausage"],
    ["pork"], # for pork substitute for equivalent turkey eg "pork" sausage -> "turkey" sausage
    ["beef"],
    ["ground beef"],
    ["beef ribs"],
    ["beef shank"],
    ["beef shoulder", "beef chuck"],
    ["beef sirloin"],

    # ["beef brisket"],
    # ["beef short plate"],
    # ["beef flank"],
    # ["beef loin"],
    # ["beef round"],

    ["bread"] # TODO turn to list
]


test_recipe_Ingredients = [
    "5 tablespoons butter, divided",
    "6 boneless thick-cut pork chops",
    "salt and ground black pepper to taste",
    "2 teaspoons dijon mustard",
    "2 teaspoons dried thyme",
    "3 tablespoons all-purpose flour",
    "2 cups chicken broth",
    "1/2 cup half-and-half",
    "6 potatoes, peeled and thinly sliced, divided",
    "1/2 cup diced onion, divided",
    "1 cup shredded cheddar cheese, divided",
    "pork sausage"
]


# To Indian
contains_non_indian = []
indian_replaceent = []
for x in test_recipe_Ingredients:
    #print(x)
    place = -1
    for n in non_indian:
        #print(n)
        place = place + 1
        for i in n:
            #print(i)
            if i in x:
                print("contains " + i)
                replacement = indian[place]
                print(replacement)
                a = x.replace(i, replacement[0])
                print(x)
                print(a)
                contains_non_indian.append(i)
                indian_replaceent.append(replacement)
              #  print("replacement " + replacement)
        #    print(place)
        #place = place + 1

steps = [{'ingredients': [], 'methods': ['bake', 'grease', 'preheat'], 'tools': ['tablespoon', 'dish', 'baking dish', 'oven'], 'time': [], 'action': 'preheat oven to 350 degrees f (175 degrees c). grease a 9x13-inch baking dish with 1 tablespoon butter.'},
         {'ingredients': [], 'methods': ['heat', 'melt', 'salt', 'season'], 'tools': ['tablespoon', 'skillet'],
          'time': ['3'],
          'action': 'melt 1 tablespoon butter in a skillet over medium heat. season pork chops with salt and pepper; cook in skillet until browned, 3 to 5 minutes per side.'},
         {'ingredients': [],
          'methods': ['season', 'whisk', 'remove', 'flour', 'stir', 'salt', 'heat', 'melt', 'thicken'],
          'tools': ['saucepan', 'whisk', 'wooden spoon'], 'time': ['5'],
          'action': 'melt remaining 3 tablespoons butter in a small saucepan over medium-high heat. stir mustard and thyme into the butter; season with salt and pepper. whisk flour into the butter mixture to make a thick paste. slowly whisk chicken broth and half-and-half into the paste mixture until smooth. continue to cook, stirring occasionally, until it begins to thicken into a sauce, about 5 minutes; remove from heat.'},
         {'ingredients': [], 'methods': ['layer', 'arrange', 'pour', 'sprinkle', 'cover', 'bake', 'dice', 'prepare'],
          'tools': ['baking dish', 'dish', 'oven', 'knife'], 'time': [],
          'action': 'cover the bottom of the prepared baking dish with about half the potato slices and diced onion. sprinkle about half the cheddar cheese over the potato mixture. arrange the pork chops over cheese layer. layer remaining potatoes and onion atop the pork chops. pour the sauce evenly over the potato mixture.'},
         {'ingredients': [], 'methods': ['bake', 'preheat', 'broil'], 'tools': ['dish', 'oven'], 'time': ['5', '1'],
          'action': 'bake in preheated oven for 1 hour. top dish with remaining cheddar cheese, switch oven to broil, and continue baking until the top is browned and bubbly, about 5 minutes.'}]
for step in steps:
    index = -1
    for n in contains_non_indian:
        index = index + 1
        s = step.get('action')
        if n in s:
            s = s.replace(n, indian_replaceent[index][0])
            step['action'] = s

print(steps)


# From Indian
def fromIndian(ingredients, steps):
    contains_indian = []
    non_indian_replacement = []
    for x in ingredients:
        place = -1
        for n in indian:
            place = place + 1
            for i in n:
                if i in x:
                    replacement = non_indian[place]
                    a = x.replace(i, replacement[random.randint(0, len(replacement))])
                    contains_indian.append(i)
                    non_indian_replacement.append(replacement)

    for step in steps:
        index = -1
        for n in contains_indian:
            index = index + 1
            s = step.get('action')
            if n in s:
                s = s.replace(n, non_indian_replacement[index][0])
                step['action'] = s

