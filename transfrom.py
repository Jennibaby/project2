import parser
from lists.meatlist import meatlist
from lists.nonMeatList import nonMeatList
from subList import meatsubList, nonMeatSubList\
    #, nonHealthyDict, healtyDict
from nltk.stem.wordnet import WordNetLemmatizer


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



    def updateingredForIngredient(self,newIng,oldIng):
        newIng["quantity"] = oldIng["quantity"]
        newIng["measurement"] = oldIng["measurement"]

        return newIng



    def toVegetarian(self):
        self.newrecipe = self.oldrecipe
        newingredientlist = []
        cnt = 0
        for ing in self.newrecipe["ingredients"]:
            #print (ing)
            namewords = ing["name"].split()
            flag = True
            for n in namewords:
                if n in meatlist and cnt < len(meatsubList):

                    self.newrecipe["directions"] = self.updateingredForDirection(self.newrecipe["directions"],meatsubList[cnt]["name"],ing["name"])
                    newingredientlist.append(self.updateingredForIngredient(meatsubList[cnt],ing))
                    cnt = cnt + 1
                    flag = False
                    break
            if flag:
                newingredientlist.append(ing)

        self.newrecipe["ingredients"] = newingredientlist

        print (self.newrecipe)


    def fromVegetarian(self):
        self.newrecipe = self.oldrecipe
        newingredientlist = []
        cnt = 0
        for ing in self.newrecipe["ingredients"]:
            # print (ing)
            namewords = ing["name"].split()
            flag = True
            for n in namewords:
                if n in nonMeatList and cnt < len(nonMeatSubList):
                    self.newrecipe["directions"] = self.updateingredForDirection(self.newrecipe["directions"],
                                                                                 nonMeatSubList[cnt]["name"], ing["name"])
                    newingredientlist.append(self.updateingredForIngredient(nonMeatSubList[cnt], ing))
                    cnt = cnt + 1
                    flag = False
                    break
            if flag:
                newingredientlist.append(ing)

        self.newrecipe["ingredients"] = newingredientlist

        print (self.newrecipe)


    # def toHealthy(self):
    #     self.newrecipe = self.oldrecipe
    #     newingredientlist = []
    #     for ing in self.newrecipe["ingredients"]:
    #         # print (ing)
    #
    #         flag = True
    #         if ing["name"] in nonHealthyDict:
    #             self.newrecipe["directions"] = self.updateingredForDirection(self.newrecipe["directions"],
    #                                                                          nonHealthyDict[ing["name"]]["name"], ing["name"])
    #             newingredientlist.append(self.updateingredForIngredient(nonHealthyDict[ing["name"]], ing))
    #             flag = False
    #
    #         if flag:
    #             newingredientlist.append(ing)
    #
    #     self.newrecipe["ingredients"] = newingredientlist

    


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



    def subMethods(self):
        print (self.oldrecipe)
        subDict = {"bake":"boil"}
        self.newrecipe = self.oldrecipe
        newPrimaryList = []
        cnt = 0
        for pcm in self.newrecipe["Methods"]["Primary cooking method"]:

            if pcm in subDict:
                newPrimaryList.append(subDict[pcm])
                self.newrecipe["directions"] = self.updateMethodForDirection(self.newrecipe["directions"], subDict[pcm],pcm)
            else:
                newPrimaryList.append(pcm)



        self.newrecipe["Methods"]["Primary cooking method"] = newPrimaryList

        print (self.newrecipe)
















