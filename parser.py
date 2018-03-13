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


class parser(object):

    def __init__(self,url,spicesDictPath,proteinDictPath,carbohydratesDictPath,fatsDictPath,resPath="output.json"):
        self.res = {}
        self.text = requests.get(url).text
        self.soup = BeautifulSoup(self.text,"html.parser")
        self.res["URL"] = url
        self.spicesDict = self.readDict(spicesDictPath)
        self.proteinDict = self.readDict(proteinDictPath)
        self.fatsDict = self.readDict(fatsDictPath)
        self.carbohydratesDict = self.readDict(carbohydratesDictPath)
        self.stopwords = nltk.corpus.stopwords.words('english') + list(string.punctuation)
        self.directionList = []
        self.tools = []
        self.methods = []
        self.primaryMethods = []

    def readDict(self,dictPath):
        with open(dictPath,'r') as f:
            resDict = json.load(f)
        print (resDict)
        return resDict

    
    def parserIngredient(self):
        self.res["ingredients"] = {}
        self.res["ingredients"]["spices"] = []
        self.res["ingredients"]["protein"] = []
        self.res["ingredients"]["carbohydrates"] = []
        self.res["ingredients"]["fats"] = []
        self.res["ingredients"]["others"] = []
        ingredientsTextRaw = self.soup.find_all('span', {"class": "recipe-ingred_txt","itemprop": "ingredients"})
        for ingredientText in ingredientsTextRaw:
            ingredientText =  ingredientText.text.strip().encode('ascii').lower().decode()
            if len(ingredientText) == 0:
                continue
            print (ingredientText)
            newIngredient = {}
            quantityText = re.search('(\d+([\s\.\/\d]+)?)+', ingredientText)
            # print (quantityText)
            quantity = None
            if quantityText != None:
                quantityTextList = quantityText.group(0).strip().split()
                if quantityTextList != None or len(quantityTextList) != 0:
                    quantity = float(sum(Fraction(q) for q in quantityTextList))
                    ingredientText = ingredientText.replace(quantityText.group(0),'')    
                    

            
            newIngredient["quantity"] = quantity
            # print (newIngredient["quantity"])

            # print (ingredientText)

            tokens = nltk.tokenize.word_tokenize(ingredientText)
            # print (tokens)
            measurementList = []
            descriptorList = []
            preparationList = []

            for token in tokens:
                if token in keyWords.unitsList:
                    measurement = token
                    if measurement in keyWords.unitsAbbrToFull:
                        measurement = keyWords[measurement]
                    measurementList.append(measurement)
                    ingredientText = ingredientText.replace(token,'')

                if token in keyWords.descriptorList:
                    descriptorList.append(token)
                    ingredientText = ingredientText.replace(token,'')

                if token in keyWords.preparationList:
                    preparationList.append(token)
                    ingredientText = ingredientText.replace(token,'')

            if measurement == None:
                measurement = "unit"

            # print (measurementList)
            # print (descriptorList)
            # print (descriptorList)
            
            newIngredient["measurement"] = measurementList
            newIngredient["descriptor"] = descriptorList
            newIngredient["preparation"] = preparationList

            tokens = nltk.tokenize.word_tokenize(ingredientText)
            for token in tokens:
                if token in self.stopwords:
                    tokens.remove(token)
            
            newIngredient["name"] = (" ").join(tokens)
            if newIngredient["name"] in self.spicesDict:
                newIngredient["sub-catagory"] = self.spicesDict[newIngredient["name"]]
                self.res["ingredients"]["spices"].append(newIngredient)
            elif newIngredient["name"] in self.proteinDict:
                newIngredient["sub-catagory"] = self.proteinDict[newIngredient["name"]]
                self.res["ingredients"]["protein"].append(newIngredient)
            elif newIngredient["name"] in self.fatsDict:
                newIngredient["sub-catagory"] = self.fatsDict[newIngredient["name"]]
                self.res["ingredients"]["fats"].append(newIngredient)
            elif newIngredient["name"] in self.carbohydratesDict:
                newIngredient["sub-catagory"] = self.carbohydratesDict[newIngredient["name"]]
                self.res["ingredients"]["carbohydrates"].append(newIngredient)
            else:
                newIngredient["sub-catagory"] = None
                self.res["ingredients"]["others"].append(newIngredient)


            # print (newIngredient)

    
    def parserDirection(self):
        directionTextRaw = self.soup.find_all('span', {"class": "recipe-directions__list--item"})
        self.res["steps"] = []
        for directionText in directionTextRaw:
            directionText =  directionText.text.strip().encode('ascii').lower().decode()
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

                if t in keyWords.methodList:
                    t = WordNetLemmatizer().lemmatize(t,'v')
                    self.methods.append(t)
                    methodStep.append(t)
                    if t in keyWords.method2Tool:
                        self.tools.append(keyWords.method2Tool[t])
                        toolsStep.append(keyWords.method2Tool[t])


                if t in keyWords.toolList:
                    self.tools.append(t)
                    toolsStep.append(t)

                
            
            #bigram
            for t in bigramsStepsTokens:
                if t in keyWords.primaryMethodsList:
                    self.primaryMethods.append(t)

                if t in keyWords.methodList:
                    self.methods.append(t)
                    methodStep.append(t)
                    if t in keyWords.method2Tool:
                        self.tools.append(keyWords.method2Tool[t])
                        toolsStep.append(keyWords.method2Tool[t])


                if t in keyWords.toolList:
                    self.tools.append(t)
                    toolsStep.append(t)
                   
            costTime = re.search(r'([\d\/\.]+)\s?(([\-to\d\/\. ]+)?)\s?(min(?:(?:utes?)?|.?)?|sec(?:(?:onds?)?|.?)?|h(?:(?:ours?|rs?.?)?))\s?(?:per side|each side)?',directionText)
            if costTime != None:
                timesStep.append(costTime.group(0).strip())
            # for t in timeMatchList:
            #     timesStep.append(t.group(0).strip())
            
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
            print ("each step:")
            self.res["steps"].append(step)
            print (step)


        self.tools = list(set(self.tools))
        self.primaryMethods = list(set(self.primaryMethods))
        self.methods = list(set(self.methods))
        self.res["Tools"] = self.tools
        self.res["Methods"] = {}
        self.res["Methods"]["Primary cooking method"] = self.primaryMethods
        self.res["Methods"]["other method"] = self.methods


        print ("tools")
        print (self.tools)

        print ("Primary cooking method")
        print (self.primaryMethods)

        print ("other method")
        print (self.methods)
                    
        
        

    

                


                    



                




            




    


