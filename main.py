import parser
import transfrom
import json
import keyWords
from nltk.stem.wordnet import WordNetLemmatizer
import utils
import sys
import keyWords

if __name__ == '__main__':
    # url = raw_input("Please enter a URL from allrecipes.com")

    url = "https://www.allrecipes.com/recipe/232458/pork-chops-with-creamy-scalloped-potatoes/"


    # resPath = "./output/parserOutput.json"
    # test = parser.parser(url,resPath)
    # test.parserIngredient()
    # test.parserDirection()
    # utils.writeDict(utils.recipeAddNumber(test.res),resPath)
    #
    # newRecipePath = "./output/newRecipeOutput.json"
    # transfromtest = transfrom.transform(test.res)
    # # transfromtest.toVegetarian()
    # # transfromtest.fromVegetarian()
    # # transfromtest.toHealthy()
    # # transfromtest.fromHealthy()
    # # transfromtest.toMexican()
    # transfromtest.subMethods({"bake":"boil"})
    # utils.writeDict(utils.recipeAddNumber(transfromtest.newrecipe), newRecipePath)
    # #transfromtest.subMethods()

    resPath = "./output/parserOutput.json"
    newRecipePath = "./output/newRecipeOutput.json"
    url = None
    transfromtest = None

    print ("welcome recipe parser and transformer")
    while True:
        select = input("press 0: exit this process\npress 1: enter an URL to parse a recipe\n\
press 2: do transformation\npress 3: show old recipe\npress 4: show new recipe\n")
        if select == '1':
            url = str(input("please enter an URL from allrecipe\n\
(default:https://www.allrecipes.com/recipe/232458/pork-chops-with-creamy-scalloped-potatoes/)\n"))
            if len(url.strip()) == 0:
                url = 'https://www.allrecipes.com/recipe/232458/pork-chops-with-creamy-scalloped-potatoes/'
            test = parser.parser(url, resPath)
            test.parserIngredient()
            test.parserDirection()
            utils.printDict(utils.recipeAddNumber(test.res))
            utils.writeDict(utils.recipeAddNumber(test.res), resPath)

        elif select == '2':
            if url == None:
                print ("you need to press 1 to enter an URL to parser an recipe first")
                continue
            transfromtest = transfrom.transform(test.res)
            tran = input("press 0: exit this process\n\
press 1: change recipe to Vegetarian\n\
press 2: change recipe to Non-Vegetarian\n\
press 3: change recipe to Healthy recipe\n\
press 4: change recipe to Non-healthy recipe\n\
press 5: change recipe to Mexican recipe\n\
press 6: change cooking methods\n" \
                   )
            if tran == '0':
                break
            elif tran == '1':
                transfromtest.toVegetarian()
                # utils.printDict(utils.recipeAddNumber(transfromtest.newrecipe))
                utils.writeDict(utils.recipeAddNumber(transfromtest.newrecipe), newRecipePath)
            elif tran == '2':
                transfromtest.fromVegetarian()
                # utils.printDict(utils.recipeAddNumber(transfromtest.newrecipe))
                utils.writeDict(utils.recipeAddNumber(transfromtest.newrecipe), newRecipePath)
            elif tran == '3':
                transfromtest.toHealthy()
                # utils.printDict(utils.recipeAddNumber(transfromtest.newrecipe))
                utils.writeDict(utils.recipeAddNumber(transfromtest.newrecipe), newRecipePath)
            elif tran == '4':
                transfromtest.fromHealthy()
                # utils.printDict(utils.recipeAddNumber(transfromtest.newrecipe))
                utils.writeDict(utils.recipeAddNumber(transfromtest.newrecipe), newRecipePath)
            elif tran == '5':
                transfromtest.toMexican()
                # utils.printDict(utils.recipeAddNumber(transfromtest.newrecipe))
                utils.writeDict(utils.recipeAddNumber(transfromtest.newrecipe), newRecipePath)
            elif tran == '6':
                print ("optional old methods that you want to subtititue")
                i = 1
                for pm in test.res["Methods"]["Primary cooking method"]:
                    print (str(i) + ":" + pm)
                    i += 1

                orig = int(input("enter sequence of your option of oldMethod\n"))
                if orig > len(test.res["Methods"]["Primary cooking method"]):
                    print ("ilegal input")

                print ("optional new methods that you want to use")
                i = 1
                for pm in keyWords.primaryMethodsList:
                    print (str(i) + ":" + pm)
                    i += 1

                new = int(input("enter your option of oldMethod\n"))
                if new > len(keyWords.primaryMethodsList):
                    print ("ilegal input")

                d = {test.res["Methods"]["Primary cooking method"][orig-1]:keyWords.primaryMethodsList[new-1]}
                transfromtest.subMethods(d)
                # utils.printDict(utils.recipeAddNumber(transfromtest.newrecipe))
                utils.writeDict(utils.recipeAddNumber(transfromtest.newrecipe), newRecipePath)
            else:
                print ("ilegal input")

        elif select == '3':
            if url == None:
                print ("you need to press 1 to enter an URL to parser an recipe first")
                continue
            utils.printDict(utils.recipeAddNumber(test.res))
        elif select == '4':
            if transfromtest == None:
                print ("you have not done any transformation before")
                continue
            utils.printDict(utils.recipeAddNumber(transfromtest.newrecipe))
        elif select == '0':
            break
        else:
            print ("ilegal input")



