import parser
if __name__ == '__main__':
    # url = raw_input("Please enter a URL from allrecipes.com")

    url = "https://www.allrecipes.com/recipe/232458/pork-chops-with-creamy-scalloped-potatoes/"

    spicesDictPath = "spicesDict.json"
    proteinDictPath = "proteinDict.json"
    carbohydratesDictPath = "carbohydratesDict.json"
    fatsDictPath = "fatsDict.json"
    resPath = "output.json"
    test = parser.parser(url,spicesDictPath,proteinDictPath,carbohydratesDictPath,fatsDictPath,resPath)
    test.parserIngredient()
    test.parserDirection()