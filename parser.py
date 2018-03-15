from bs4 import BeautifulSoup
import requests
import nltk
import json
import keyWords
import re
from fractions import Fraction
import string
#from en import verb
from nltk.stem.wordnet import WordNetLemmatizer
from collections import OrderedDict

class ingredient(object):

    def __init__(self,ingredientText):
        self.stopwords = nltk.corpus.stopwords.words('english') + list(string.punctuation)
        self.ing = OrderedDict()
        #self.ing = {}
        self.ing["name"] = ""
        self.ing["quantity"] = ""
        self.ing["measurement"] = []
        self.ing["descriptor"] = []
        self.ing["preparation"] = []
        

        quantityText = re.search('(\d+([\s\.\/\d]+)?)+', ingredientText)
        # print (quantityText)
        quantity = None
        if quantityText != None:
            quantityTextList = quantityText.group(0).strip().split()
            if quantityTextList != None or len(quantityTextList) != 0:
                quantity = float(sum(Fraction(q) for q in quantityTextList))
                ingredientText = ingredientText.replace(quantityText.group(0),'')    
                

        if quantity == None:
            quantity = 1
        
        self.ing["quantity"] = quantity
        # print (newIngredient["quantity"])

        # print (ingredientText)

        tokens = nltk.tokenize.word_tokenize(ingredientText)
        bigrams = nltk.bigrams(tokens)
        bigramsTokens = []
        for g in bigrams:
            bigramsTokens.append(" ".join(g))
        # print (tokens)
        measurementList = []
        descriptorList = []
        preparationList = []

        for token in tokens:
            if token in keyWords.unitsList:
                measurement = token
                if measurement in keyWords.unitsAbbrToFull:
                    measurement = keyWords[measurement]
                self.ing["measurement"].append(measurement)
                ingredientText = ingredientText.replace(token,'')

            if token in keyWords.descriptorList:
                self.ing["descriptor"].append(token)
                ingredientText = ingredientText.replace(token,'')

            if token in keyWords.preparationList:
                self.ing["preparation"].append(token)
                ingredientText = ingredientText.replace(token,'')

        if len(self.ing["measurement"]) == 0:
            self.ing["measurement"].append("unit")

        for token in bigramsTokens:
            if token in keyWords.unitsList:
                measurement = token
                if measurement in keyWords.unitsAbbrToFull:
                    measurement = keyWords[measurement]
                self.ing["measurement"].append(measurement)
                ingredientText = ingredientText.replace(token,'')

            if token in keyWords.descriptorList:
                self.ing["descriptor"].append(token)
                ingredientText = ingredientText.replace(token,'')

            if token in keyWords.preparationList:
                self.ing["preparation"].append(token)
                ingredientText = ingredientText.replace(token,'')

        if len(self.ing["measurement"]) == 0:
            self.ing["measurement"].append("unit")


        tokens = nltk.tokenize.word_tokenize(ingredientText)
        totensList = []
        for token in tokens:
            if token in self.stopwords:
                continue
            totensList.append(token.lower())
        self.ing["name"] = (" ").join(totensList)
       

class parser(object):

    def __init__(self,url,resPath="output.json"):
        self.res = OrderedDict()
        self.text = requests.get(url).text
        self.soup = BeautifulSoup(self.text,"html.parser")
        self.res["URL"] = url
        self.stopwords = nltk.corpus.stopwords.words('english') + list(string.punctuation)
        self.ingredients = []
        self.directionList = []
        self.tools = []
        self.methods = []
        self.primaryMethods = []
        #self.filterlist = ["and"]
        

    def readDict(self,dictPath):
        with open(dictPath,'r') as f:
            resDict = json.load(f)
        return resDict

    
    def parserIngredient(self):
        # self.res["ingredients"] = {}
        # self.res["ingredients"]["spices"] = []
        # self.res["ingredients"]["protein"] = []
        # self.res["ingredients"]["carbohydrates"] = []
        # self.res["ingredients"]["fats"] = []
        # self.res["ingredients"]["others"] = []
        self.res["ingredients"] = []
        ingredientsTextRaw = self.soup.find_all('span', {"class": "recipe-ingred_txt","itemprop": "ingredients"})
        for ingredientText in ingredientsTextRaw:
            ingredientText =  ingredientText.text.strip().encode('ascii').lower().decode()
            if len(ingredientText) == 0:
                continue
            # print (ingredientText)
            newIngredient = ingredient(ingredientText)

            self.res["ingredients"].append(newIngredient.ing)
            self.ingredients.append(newIngredient.ing["name"])


    
    def parserDirection(self):
        directionTextRaw = self.soup.find_all('span', {"class": "recipe-directions__list--item"})
        self.res["Tools"] = None
        self.res["Methods"] = {}
        self.res["directions"] = []

        for directionText in directionTextRaw:
            directionText =  directionText.text.strip().encode('ascii').lower().decode()
            if directionText.strip() == "":
                continue
            self.directionList.append(directionText) 
            uniStepsTokens = nltk.tokenize.word_tokenize(directionText)
            bigrams = nltk.bigrams(uniStepsTokens)
            bigramsStepsTokens = []
            for g in bigrams:
                bigramsStepsTokens.append(" ".join(g))

            methodStep = []
            toolsStep = []
            timesStep = []
            ingredientsStep = []
            #uni-gram
            for t in uniStepsTokens:


                if t in keyWords.primaryMethodsList:
                    self.primaryMethods.append(t)

                if t in keyWords.methodList and t not in keyWords.primaryMethodsList:

                    tmp = WordNetLemmatizer().lemmatize(t,'v')

                    # correct some worse case:
                    if tmp == "cub":
                        tmp = "cube"
                    if tmp == "par":
                        tmp = "pare"

                    self.methods.append(tmp)
                    methodStep.append(tmp)
                    if tmp in keyWords.method2Tool:
                        self.tools.append(keyWords.method2Tool[tmp])
                        toolsStep.append(keyWords.method2Tool[tmp])


                if t in keyWords.toolList:
                    self.tools.append(t)
                    toolsStep.append(t)

                for ingred in self.ingredients:
                    # print ("debug " + ingred + " " + t)
                    if t == ingred.split()[0]:
                        ingredientsStep.append(ingred)    
            
            #bigram
            for t in bigramsStepsTokens:

                if t in keyWords.primaryMethodsList:
                    self.primaryMethods.append(t)

                if t in keyWords.methodList and t not in keyWords.primaryMethodsList:
                    self.methods.append(t)
                    methodStep.append(t)
                    if t in keyWords.method2Tool:
                        self.tools.append(keyWords.method2Tool[t])
                        toolsStep.append(keyWords.method2Tool[t])


                if t in keyWords.toolList:
                    self.tools.append(t)
                    toolsStep.append(t)
                   
            timeMatchList = re.findall(r'(([\d\/\.]+)\s?(([\-to\d\/\. ]+)?)\s?(min(?:(?:utes?)?|.?)?|sec(?:(?:onds?)?|.?)?|h(?:(?:ours?|rs?.?)?))\s?(?:per side|each side)?)',directionText)
            # if costTime != None:
            #     timesStep.append(costTime.group(0).strip())
            for t in timeMatchList:
                timesStep.append(t[0].strip())
            
            step = {}

            methodStep = list(set(methodStep))
            toolsStep = list(set(toolsStep))
            timesStep = list(set(timesStep))
            ingredientsStep = list(set(ingredientsStep))
            step["ingredients"] = ingredientsStep
            step["methods"] = methodStep
            step["tools"] = toolsStep
            step["time"] = timesStep
            step["action"] = directionText
            #print ("each step:")
            self.res["directions"].append(step)
            #print (step)


        self.tools = list(set(self.tools))
        self.primaryMethods = list(set(self.primaryMethods))
        self.methods = list(set(self.methods))
        self.res["Tools"] = self.tools
        self.res["Methods"] = {}
        self.res["Methods"]["Primary cooking method"] = self.primaryMethods
        self.res["Methods"]["other method"] = self.methods


        # print ("tools")
        # print (self.tools)
        #
        # print ("Primary cooking method")
        # print (self.primaryMethods)
        #
        # print ("other method")
        # print (self.methods)


                    
        
        

    

                


                    



                




            




    


