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


# def printRecipeNL(recipe):
#     print ("======= recipe in natural language ======")
#     print ("ingredients:")
#     for i in range(0,len(recipe["ingredients"])):
#         depre = list(set(recipe["ingredients"][i]["descriptor"] + recipe["ingredients"][i]["preparation"]))
#         tmplist = []
#         if str(recipe["ingredients"][i]["quantity"]) != "":
#             tmplist.append(str(recipe["ingredients"][i]["quantity"]))
#
#         if recipe["ingredients"][i]["measurement"][0] != "":
#             tmplist.append(recipe["ingredients"][i]["measurement"][0])
#
#         if len(depre) > 0:
#             tmplist.append(" ".join(depre))
#
#         if recipe["ingredients"][i]["name"] != "":
#             tmplist.append(recipe["ingredients"][i]["name"])
#
#         # tmp = str(recipe["ingredients"][i]["quantity"]) + " " + recipe["ingredients"][i]["measurement"][0] + " " + "" ".join(depre) + " " + recipe["ingredients"][i]["name"]
#         tmp = " ".join(tmplist)
#         print ("ingredient " + str(i+1) +": " + tmp)
#
#     print ("steps:")
#     for i in range(0, len(recipe["directions"])):
#         print ("step " + str(i+1) + ": " + recipe["directions"][i]["action"])
#
#     print ("")

def printRecipeNL(recipe):
    print ("======= recipe in natural language ======")
    print ("====ingredients:====")
    for i in range(0,len(recipe["ingredients"])):
        if recipe["ingredients"][i]["name"] == "":
            name = "None"
        else:
            name = recipe["ingredients"][i]["name"]

        if str(recipe["ingredients"][i]["quantity"]) == "":
            quantity = "None"
        else:
            quantity = str(recipe["ingredients"][i]["quantity"])

        if recipe["ingredients"][i]["measurement"][0] == "":
            measurement = "None"
        else:
            measurement = recipe["ingredients"][i]["measurement"][0]

        if len(recipe["ingredients"][i]["descriptor"]) > 0:
            descriptor = ", ".join(recipe["ingredients"][i]["descriptor"])
        else:
            descriptor = "None"

        if len(recipe["ingredients"][i]["preparation"]) > 0:
            preparation = ", ".join(recipe["ingredients"][i]["preparation"])
        else:
            preparation = "None"

        print ("ingredient " + str(i + 1) + ": ========")
        print ("name: " + name)
        print ("quantity: " + quantity)
        print ("measurement: " + measurement)
        print ("descriptor: " + descriptor)
        print ("preparation: " + preparation)
        print ("")

    if len(recipe["Methods"]["Primary cooking method"]) > 0:
        PCM = ", ".join(recipe["Methods"]["Primary cooking method"])
    else:
        PCM = "None"
    print ("Primary cooking method :" + PCM + "\n")

    print ("====steps:====")
    for i in range(0, len(recipe["directions"])):

        if len(recipe["directions"][i]["ingredients"]) == 0:
            ingredients = "None"
        else:
            ingredients = ", ".join(recipe["directions"][i]["ingredients"])

        if len(recipe["directions"][i]["methods"]) == 0:
            methods = "None"
        else:
            methods = ", ".join(recipe["directions"][i]["methods"])

        if len(recipe["directions"][i]["tools"]) == 0:
            tools = "None"
        else:
            tools = ", ".join(recipe["directions"][i]["tools"])

        if len(recipe["directions"][i]["time"]) == 0:
            time = "None"
        else:
            time = ", ".join(recipe["directions"][i]["time"])

        print ("step " + str(i+1) + ": =========")
        print ("ingredients: " + ingredients)
        print ("methods: " + methods)
        print ("tools: " + tools)
        print ("time: " + time)
        print ("")



