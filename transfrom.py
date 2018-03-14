import parser
from lists.meatlist import meatlist
from lists.nonMeatList import nonMeatList

tofu = parser.ingredient("sliced tofu")
seitan = parser.ingredient("sliced seitan")
tempeh = parser.ingredient("sliced tempeh")
lentil = parser.ingredient("burger patty")
mushroom = parser.ingredient("large portabella mushroom")
texturedVegetableProtein = parser.ingredient("dry Textured Vegetable Protein")

meatsubList = [tofu.ing,seitan.ing,tempeh.ing,lentil.ing,mushroom.ing,texturedVegetableProtein.ing]

slicedBacon = parser.ingredient("slice of bacon")
beef = parser.ingredient("ground beef")
caribou = parser.ingredient("T-bone steak of caribou")
chicken = parser.ingredient("chicken breast")
salmon = parser.ingredient("fillet of salmon")
duck = parser.ingredient("tenderloin of duck")
halibut = parser.ingredient("fillet of halibut")
ham = parser.ingredient("slice of pork loin")
lamb = parser.ingredient("rib of lamb")
mutton = parser.ingredient("fillet of mutton")
pork = parser.ingredient("slice of pork loin")
snapper = parser.ingredient("fillet of snapper")
turkey = parser.ingredient("turkey breast")
veal = parser.ingredient("fillet of veal")
venison = parser.ingredient("steak of venison")
walleye = parser.ingredient("fillet of walleye")
yellowfinTuna = parser.ingredient("fillet of yellowfin tuna")

nonMeatSubList = [slicedBacon.ing, beef.ing, caribou.ing, chicken.ing, salmon.ing, duck.ing, halibut.ing, ham.ing, lamb.ing, mutton.ing, pork.ing, snapper.ing, turkey.ing, veal.ing, venison.ing, walleye.ing, yellowfinTuna.ing]


bacon = parser.ingredient("Bacon")
wBread = parser.ingredient("white bread")
bCrumbs = parser.ingredient("Bread crumbs")
butter = parser.ingredient("Butter")
margarine = parser.ingredient("margarine")
egg = parser.ingredient("Eggs")
apFlour = parser.ingredient("all-purpose flour")
gBeef = parser.ingredient("ground beef")
iLettuce = parser.ingredient("iceberg lettuce")
mayon = parser.ingredient("mayonnaise")
eMilk = parser.ingredient("evaporated milk")
wMilk = parser.ingredient("whole milk")
pasta = parser.ingredient("pasta")
wRice = parser.ingredient("white rice")
sCream = parser.ingredient("sour cream")
yogurt = parser.ingredient("yogurt")
sugar = parser.ingredient("sugar")
cChips = parser.ingredient("chocolate chips")
vOil = parser.ingredient("vegetable oil")
cCheese = parser.ingredient("cream cheese")



cBacon = parser.ingredient("Canadian bacon")
tBacon = parser.ingredient("turkey bacon")
sTurkey = parser.ingredient("smoked turkey")
leanPro = parser.ingredient("lean prosciutto")
wgBread = parser.ingredient("Whole-grain bread")
cbCereal = parser.ingredient("crushed bran cereal")
gfSeeds = parser.ingredient("ground flax seeds")
appSauce = parser.ingredient("Applesauce")
cSpray = parser.ingredient("cooking spray")
eWhite = parser.ingredient("egg white")
wpFlour = parser.ingredient("whole-wheat pastry flour")
elgBeef = parser.ingredient("Extra-lean ground beef")
lgBeef = parser.ingredient("lean ground beef")
gChicken = parser.ingredient("ground chicken breast")
gTurkey = parser.ingredient("ground turkey breast")
arugula = parser.ingredient("Arugula")
chicory = parser.ingredient("chicory")
cGreen = parser.ingredient("collard greens")
kale = parser.ingredient("kale")
spinach = parser.ingredient("spinach")
watercress = parser.ingredient("watercress")
rcMayon = parser.ingredient("Reduced-calorie mayonnaise")
esMilk = parser.ingredient("Evaporated skim milk")
rfMilk = parser.ingredient("Reduced fat milk")
sMilk = parser.ingredient("skim milk")
wPasta = parser.ingredient("whole-wheat pasta")
bRice = parser.ingredient("Brown rice")
wildRice = parser.ingredient("wild rice")
ffSourCream = parser.ingredient("Fat free sour cream")
lfSourCream = parser.ingredient("low-fat sour cream")
lfpYogurt = parser.ingredient("low-fat plain yogurt")
ffpYogurt = parser.ingredient("fat-free plain yogurt")
gYogurt = parser.ingredient("greek yogurt")
plYogurt = parser.ingredient("plain low-fat yogurt")
stevia = parser.ingredient("stevia")
cNibs = parser.ingredient("cacao nibs")
cOil = parser.ingredient("coconut oil")
ffcCheese = parser.ingredient("Fat free cream cheese")



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







