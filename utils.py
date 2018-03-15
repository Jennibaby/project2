import json

def printDict(d):
    print (json.dumps(d, indent=4, separators=(',', ':')))

def writeDict(d,file):
    f = open(file, 'w')
    f.write(json.dumps(d, indent=4, separators=(',', ':')))
    f.close()

def recipeAddNumber(recipe):
    newRecipe = {}
    newRecipe["ingredients"] = {}
    for i in range(0,len(recipe["ingredients"])):
        newRecipe["ingredients"][str(i+1)] = recipe["ingredients"][i]
    newRecipe["Tools"] = recipe["Tools"]
    newRecipe["Methods"] = recipe["Methods"]
    newRecipe["steps"] = {}
    for i in range(0,len(recipe["directions"])):
        newRecipe["steps"][str(i+1)] = recipe["directions"][i]

    return newRecipe