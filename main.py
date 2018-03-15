import parser
import transfrom
import json
import keyWords
from nltk.stem.wordnet import WordNetLemmatizer
import utils
import sys

if __name__ == '__main__':
    # url = raw_input("Please enter a URL from allrecipes.com")

    url = "https://www.allrecipes.com/recipe/232458/pork-chops-with-creamy-scalloped-potatoes/"


    resPath = "./output/parserOutput.json"
    test = parser.parser(url,resPath)
    test.parserIngredient()
    test.parserDirection()
    utils.writeDict(utils.recipeAddNumber(test.res),resPath)

    newRecipePath = "./output/newRecipeOutput.json"
    transfromtest = transfrom.transform(test.res)
    # transfromtest.toVegetarian()
    # transfromtest.fromVegetarian()
    # transfromtest.toHealthy()
    # transfromtest.fromHealthy()
    # transfromtest.toMexican()
    transfromtest.subMethods({"bake":"boil"})
    utils.writeDict(utils.recipeAddNumber(transfromtest.newrecipe), newRecipePath)
    #transfromtest.subMethods()

    url = None

    print ("welcome recipe parser and transformer")
    while True:
        select = raw_input("press 0: exit this process\npress 1: enter an URL to parse a recipe\npress 2: do transformation")
        if select == 1:
            url = str(raw_input("please enter an URL from allrecipe"))
            test = parser.parser(url, resPath)
            test.parserIngredient()
            test.parserDirection()
            utils.printDict(utils.recipeAddNumber(test.res))

        elif select == 2:
            transfromtest = transfrom.transform(test.res)
            tran = raw_input("press 0: exit this process\n  \
                   press 1: change recipe to Vegetarian\n  \
                   press 2: change recipe to Non-Vegetarian\n \
                   press 3: change recipe to Healthy recipe\n \
                   press 4: change recipe to Non-healthy recipe\n \
                   press 5: change recipe to Mexican recipe\n \
                   press 6: change cooking methods\n" \
                   )
            if tran == 0:
                break
            elif tran == 1:
                transfromtest.toVegetarian()
                utils.printDict(utils.recipeAddNumber(transfromtest.newrecipe))
            elif tran == 2:
                transfromtest.fromVegetarian()
                utils.printDict(utils.recipeAddNumber(transfromtest.newrecipe))
            elif tran == 3:
                transfromtest.toHealthy()
                utils.printDict(utils.recipeAddNumber(transfromtest.newrecipe))
            elif tran == 4:
                transfromtest.fromHealthy()
                utils.printDict(utils.recipeAddNumber(transfromtest.newrecipe))
            elif tran == 5:
                transfromtest.toMexican()
                utils.printDict(utils.recipeAddNumber(transfromtest.newrecipe))
            elif tran == 6:
                transfromtest.subMethods({"bake":"boil"})
                utils.printDict(utils.recipeAddNumber(transfromtest.newrecipe))
            else:
                print ("ilegal input")

        elif select == 0:
            break
        else:
            print ("ilegal input")



