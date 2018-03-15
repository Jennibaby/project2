import parser
from meatlist import meatlist
from nonMeatList import nonMeatList
from subList import meatsubList, nonMeatSubList, nonHealthyDict, healtyDict, mexicanSubDict, non_mexican,\
nonMexicanSpicyList,nonMexicanSpicySubDict,commonSpicesList,mexicanSpicyList,nonIndianDict,indianSpciyList
from nltk.stem.wordnet import WordNetLemmatizer
import json
import utils
import copy


methodSubDict = {"boil":"bake","bake":"roast","fry":"bake","grill":"fry","steam":"pressure-cook","pan-fry":"boil","sear":"bake"}

class transform(object):
    def __init__(self,recipe):
        self.oldrecipe = recipe
        self.newrecipe = None

    def updateingredForDirection(self,directionlist,newName,oldName):


        newDirectionList = []
        for direction in directionlist:
            newdirection = {}
            newdirection["methods"] = direction["methods"]
            newdirection["tools"] = direction["tools"]
            newdirection["time"] = direction["time"]
            newdirection["ingredients"] = []
            newdirection["action"] = ""
            ing = direction["ingredients"]
            action = direction["action"]

            for ingred in ing:
                words = ingred.split()
                flag = True
                for w in words:
                    if w in oldName.split():
                        newdirection["ingredients"].append(newName)
                        flag = False
                        break
                if flag:
                    newdirection["ingredients"].append(ingred)

            flag = True
            words = action.split()
            newAction = ""
            for w in words:
                if w in oldName.split():
                    if flag:
                        newAction = newAction + " " + newName
                        flag = False

                else:
                    flag = True
                    newAction = newAction + " " + w

            newdirection["action"] = newAction

            newDirectionList.append(newdirection)

        return newDirectionList



    def removeingredForDirection(self,directionlist,oldName):


        newDirectionList = []
        for direction in directionlist:
            newdirection = {}
            newdirection["methods"] = direction["methods"]
            newdirection["tools"] = direction["tools"]
            newdirection["time"] = direction["time"]
            newdirection["ingredients"] = []
            newdirection["action"] = direction["action"]
            ing = direction["ingredients"]

            for ingred in ing:
                words = ingred.split()
                flag = True
                for w in words:
                    if w in oldName.split():
                        flag = False
                        break
                if flag:
                    newdirection["ingredients"].append(ingred)

            newDirectionList.append(newdirection)

        return newDirectionList


    def updateingredForIngredient(self,newIng,oldIng,quantityHalf):
        if quantityHalf != None:
            newIng["quantity"] = oldIng["quantity"]*quantityHalf
        else:
            newIng["quantity"] = oldIng["quantity"]
        newIng["measurement"] = oldIng["measurement"]

        return newIng



    def toVegetarian(self):
        print ("transfomation from non-healthy recipe to healthy recipe")
        self.newrecipe = copy.deepcopy(self.oldrecipe)
        newingredientlist = []
        cnt = 0
        i = 1
        for ing in self.newrecipe["ingredients"]:
            #print (ing)
            namewords = ing["name"].split()
            flag = True
            for n in namewords:
                if n in meatlist and cnt < len(meatsubList):

                    self.newrecipe["directions"] = self.updateingredForDirection(self.newrecipe["directions"],meatsubList[cnt]["name"],ing["name"])
                    newTemp = self.updateingredForIngredient(meatsubList[cnt], ing, None)
                    newingredientlist.append(newTemp)

                    print ("sub" + str(i))
                    i += 1
                    print ("original ingredient:")
                    utils.printDict(ing)
                    print ("new ingredient:")
                    utils.printDict(newTemp)
                    print ("\n")

                    cnt = cnt + 1
                    flag = False
                    break
            if flag:
                newingredientlist.append(ing)

        self.newrecipe["ingredients"] = newingredientlist
        if i == 1:
            print ("can not find anything that can change from Non-Vegetarian to Vegetarian")



    def fromVegetarian(self):
        print ("transfomation from non-healthy recipe to healthy recipe")
        self.newrecipe = copy.deepcopy(self.oldrecipe)
        newingredientlist = []
        cnt = 0
        i = 1
        for ing in self.newrecipe["ingredients"]:
            # print (ing)
            namewords = ing["name"].split()
            flag = True
            for n in namewords:
                if n in nonMeatList and cnt < len(nonMeatSubList):
                    self.newrecipe["directions"] = self.updateingredForDirection(self.newrecipe["directions"],
                                                                                 copy.deepcopy(nonMeatSubList[cnt]["name"]), ing["name"])
                    newTemp = self.updateingredForIngredient(nonMeatSubList[cnt], ing, None)
                    newingredientlist.append(newTemp)
                    print ("sub" + str(i))
                    i += 1
                    print ("original ingredient:")
                    utils.printDict(ing)
                    print ("new ingredient:")
                    utils.printDict(newTemp)
                    print ("\n")

                    cnt = cnt + 1
                    flag = False
                    break
            if flag:
                newingredientlist.append(ing)

        self.newrecipe["ingredients"] = newingredientlist
        if i == 1:
            print ("can not find anything that can change from Vegetarian to Non-Vegetarian")



    def toHealthy(self):
        print ("transfomation from non-healthy recipe to healthy recipe")
        self.newrecipe = copy.deepcopy(self.oldrecipe)
        newingredientlist = []
        i = 1
        for ing in self.newrecipe["ingredients"]:
            # print (ing)

            flag = True
            if ing["name"] in nonHealthyDict:
                if ing["name"] == "butter" or ing["name"] == "sugar":
                    halfquantity = 0.5
                else:
                    halfquantity = None
                self.newrecipe["directions"] = self.updateingredForDirection(self.newrecipe["directions"],
                                                                             nonHealthyDict[ing["name"]]["name"], ing["name"])
                newTemp = self.updateingredForIngredient(nonHealthyDict[ing["name"]], ing,halfquantity)
                newingredientlist.append(newTemp)
                print ("sub" + str(i))
                i += 1
                print ("original ingredient:")
                utils.printDict(ing)
                print ("new ingredient:")
                utils.printDict(newTemp)
                print ("\n")
                flag = False

            if flag:
                newingredientlist.append(ing)

        if i == 1:
            print ("can not find anything non-healthy that can change to something healthy")
        self.newrecipe["ingredients"] = newingredientlist




    def fromHealthy(self):
        print ("transfomation from healthy recipe to non-healthy recipe")
        self.newrecipe = copy.deepcopy(self.oldrecipe)
        newingredientlist = []
        i = 1
        for ing in self.newrecipe["ingredients"]:
            # print (ing)

            flag = True
            if ing["name"] in healtyDict:
                if ing["name"] == "butter" or ing["name"] == "sugar":
                    halfquantity = 2
                else:
                    halfquantity = None

                need = False
                for dep in healtyDict[ing["name"]]["descriptor"]:
                    if dep not in ing["descriptor"]:
                        need = True
                if need:
                    self.newrecipe["directions"] = self.updateingredForDirection(self.newrecipe["directions"],
                                                                                 healtyDict[ing["name"]]["name"], ing["name"])

                    newTemp = self.updateingredForIngredient(healtyDict[ing["name"]], ing,halfquantity)
                    newingredientlist.append(newTemp)
                    print ("sub" + str(i))
                    i += 1
                    print ("original ingredient:")
                    utils.printDict(ing)
                    print ("new ingredient:")
                    utils.printDict(newTemp)
                    print ("\n")
                    flag = False

            if flag and (ing["name"] == "butter" or ing["name"] == "sugar"):
                halfquantity = 2
                newTemp = self.updateingredForIngredient(copy.deepcopy(ing), ing, halfquantity)
                newingredientlist.append(newTemp)
                print ("sub" + str(i))
                i += 1
                print ("original ingredient:")
                utils.printDict(ing)
                print ("new ingredient:")
                utils.printDict(newTemp)
                print ("\n")
                flag = False

            if flag:
                newingredientlist.append(ing)
        if i == 1:
            print ("can not find anything healthy that can change to something non-healthy")
        self.newrecipe["ingredients"] = newingredientlist

    def toMexican(self):
        print ("transfomation to make recipe more mexican")
        self.newrecipe = copy.deepcopy(self.oldrecipe)
        newingredientlist = []
        i = 1
        cnt = 0
        for ing in self.newrecipe["ingredients"]:
            # print (ing)

            flag = True
            if ing["name"] in non_mexican:
                self.newrecipe["directions"] = self.updateingredForDirection(self.newrecipe["directions"],
                                                                             mexicanSubDict[ing["name"]]["name"],
                                                                             ing["name"])

                newTemp = self.updateingredForIngredient(mexicanSubDict[ing["name"]], ing, None)
                newingredientlist.append(newTemp)
                print ("sub" + str(i))
                i += 1
                print ("original ingredient:")
                utils.printDict(ing)
                print ("new ingredient:")
                utils.printDict(newTemp)
                print ("\n")
                flag = False

            elif ing["name"] in nonMexicanSpicyList:
                self.newrecipe["directions"] = self.updateingredForDirection(self.newrecipe["directions"],
                                                                             nonMexicanSpicySubDict[ing["name"]][
                                                                                 "name"],
                                                                             ing["name"])

                newTemp = self.updateingredForIngredient(nonMexicanSpicySubDict[ing["name"]], ing, None)
                newingredientlist.append(newTemp)
                print ("sub" + str(i))
                i += 1
                print ("original ingredient:")
                utils.printDict(ing)
                print ("new ingredient:")
                utils.printDict(newTemp)
                print ("\n")
                flag = False

            if flag:
                newingredientlist.append(ing)

        if i == 1:
            cnt = 0
            for ing in self.newrecipe["ingredients"]:
                flag = True
                if ing["measurement"][0] in ["teaspoon", "teaspoons", "taste", "pinch", "dash"] and cnt < len(
                        mexicanSpicyList):
                    self.newrecipe["directions"] = self.updateingredForDirection(self.newrecipe["directions"],
                                                                                 copy.deepcopy(
                                                                                     mexicanSpicyList[cnt]["name"]),
                                                                                 ing["name"])
                    newTemp = self.updateingredForIngredient(mexicanSpicyList[cnt], ing, None)
                    newingredientlist.append(newTemp)
                    print ("sub" + str(i))
                    i += 1
                    print ("original ingredient:")
                    utils.printDict(ing)
                    print ("new ingredient:")
                    utils.printDict(newTemp)
                    print ("\n")
                    flag = False
                    cnt = cnt + 1

                if flag:
                    newingredientlist.append(ing)
        if i == 1:
            print ("can not find anything that can make recipe more mexican")

        self.newrecipe["ingredients"] = newingredientlist


    def toIndian(self):
        print ("transfomation to make recipe more indian")
        self.newrecipe = copy.deepcopy(self.oldrecipe)
        newingredientlist = []
        i = 1
        cnt = 0
        for ing in self.newrecipe["ingredients"]:
            # print (ing)

            flag = True
            if ing["name"] in nonIndianDict:
                self.newrecipe["directions"] = self.updateingredForDirection(self.newrecipe["directions"],
                                                                             nonIndianDict[ing["name"]]["name"],
                                                                             ing["name"])

                newTemp = self.updateingredForIngredient(nonIndianDict[ing["name"]], ing, None)
                newingredientlist.append(newTemp)
                print ("sub" + str(i))
                i += 1
                print ("original ingredient:")
                utils.printDict(ing)
                print ("new ingredient:")
                utils.printDict(newTemp)
                print ("\n")
                flag = False
            elif ing["measurement"][0] in ["teaspoon", "teaspoons", "taste", "pinch", "dash"] and cnt < len(
                        mexicanSpicyList):
                self.newrecipe["directions"] = self.updateingredForDirection(self.newrecipe["directions"],
                                                                             copy.deepcopy(
                                                                                 indianSpciyList[cnt]["name"]),
                                                                             ing["name"])
                newTemp = self.updateingredForIngredient(indianSpciyList[cnt], ing, None)
                newingredientlist.append(newTemp)
                print ("sub" + str(i))
                i += 1
                print ("original ingredient:")
                utils.printDict(ing)
                print ("new ingredient:")
                utils.printDict(newTemp)
                print ("\n")
                flag = False
                cnt = cnt + 1

            if flag:
                newingredientlist.append(ing)

        if i == 1:
            print ("can not find anything that can make recipe more indian")

        self.newrecipe["ingredients"] = newingredientlist


    def DIY(self):
        print ("transfomation to make recipe easier")
        self.newrecipe = copy.deepcopy(self.oldrecipe)
        newingredientlist = []
        i = 1
        cnt = 0
        for ing in self.newrecipe["ingredients"]:
            flag = True
            if ing["measurement"][0] in ["teaspoon", "teaspoons", "taste", "pinch", "dash"]:
                need = True
                for cp in commonSpicesList:
                    if cp in ing["name"]:
                        need = False
                        break
                if need:
                    self.newrecipe["directions"] = self.removeingredForDirection(self.newrecipe["directions"],ing["name"])
                    print ("remove" + str(i))
                    i += 1
                    print ("remove ingredient:")
                    utils.printDict(ing)
                    print ("\n")
                    flag = False
                    cnt = cnt + 1

            if flag:
                newingredientlist.append(ing)

        if i == 1:
            print ("can not find anything that can make recipe easier")

        self.newrecipe["ingredients"] = newingredientlist


    def updateMethodForDirection(self,directionlist,newMethod,oldMethod):
        newDirectionList = []
        for direction in directionlist:
            newdirection = {}
            newdirection["ingredients"] = direction["ingredients"]
            newdirection["tools"] = direction["tools"]
            newdirection["time"] = direction["time"]
            newdirection["methods"] = []
            newdirection["action"] = ""
            met = direction["methods"]
            action = direction["action"]

            for method in met:
                if method == oldMethod:
                    newdirection["methods"].append(newMethod)
                    continue
                newdirection["methods"].append(method)

            words = action.split()
            newAction = ""
            for w in words:
                if WordNetLemmatizer().lemmatize(w,'v') == method:
                    newAction = newAction + " " + newMethod
                    continue
                newAction = newAction + " " + w

            newdirection["action"] = newAction

            newDirectionList.append(newdirection)

        return newDirectionList




    def subMethods(self,subDict):
        self.newrecipe = copy.deepcopy(self.oldrecipe)
        newPrimaryList = []
        i = 1
        for pcm in self.newrecipe["Methods"]["Primary cooking method"]:
            if pcm in subDict:
                newPrimaryList.append(subDict[pcm])
                self.newrecipe["directions"] = self.updateMethodForDirection(self.newrecipe["directions"], subDict[pcm],pcm)

                print ("sub:" + str(i))
                print ("original method:")
                utils.printDict(pcm)
                print ("new method:")
                utils.printDict(subDict[pcm])
                print ("\n")

                i += 1

            else:
                newPrimaryList.append(pcm)




        self.newrecipe["Methods"]["Primary cooking method"] = list(set(newPrimaryList))

        # print (self.newrecipe)
        # print (json.dumps(self.newrecipe, indent=4))

        if i == 1:
            print ("can not find a cooking method that can be replaced")


















