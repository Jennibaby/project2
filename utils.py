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


def printRecipeNL(recipe):
    print ("======= recipe in natural language ======")
    print ("ingredients:")
    for i in range(0,len(recipe["ingredients"])):
        depre = list(set(recipe["ingredients"][i]["descriptor"] + recipe["ingredients"][i]["preparation"]))
        tmplist = []
        if str(recipe["ingredients"][i]["quantity"]) != "":
            tmplist.append(str(recipe["ingredients"][i]["quantity"]))

        if recipe["ingredients"][i]["measurement"][0] != "":
            tmplist.append(recipe["ingredients"][i]["measurement"][0])

        if len(depre) > 0:
            tmplist.append(" ".join(depre))

        if recipe["ingredients"][i]["name"] != "":
            tmplist.append(recipe["ingredients"][i]["name"])

        # tmp = str(recipe["ingredients"][i]["quantity"]) + " " + recipe["ingredients"][i]["measurement"][0] + " " + "" ".join(depre) + " " + recipe["ingredients"][i]["name"]
        tmp = " ".join(tmplist)
        print ("ingredient " + str(i+1) +": " + tmp)

    print ("steps:")
    for i in range(0, len(recipe["directions"])):
        print ("step " + str(i+1) + ": " + recipe["directions"][i]["action"])

    print ("")



