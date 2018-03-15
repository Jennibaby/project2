import parser
import transfrom

if __name__ == '__main__':
    # url = raw_input("Please enter a URL from allrecipes.com")

    url = "https://www.allrecipes.com/recipe/232458/pork-chops-with-creamy-scalloped-potatoes/"


    resPath = "output.json"
    test = parser.parser(url,resPath)
    test.parserIngredient()
    test.parserDirection()
    # print (test.res)

    transfromtest = transfrom.transform(test.res)
    # transfromtest.toVegetarian()
    # transfromtest.fromVegetarian()
    #transfromtest.toHealthy()
    transfromtest.subMethods()


    # f = open("lists/non-meats.txt",'r')
    # print ("nonMeatList = [")
    # for line in f.readlines():
    #     if line.strip() != "":
    #         print ('"' + line.strip().lower() + '",')
    #
    # print ("]")


