import re

def DIYtoEasy(ingredients, steps):
    for step in steps:
        index = -1
        s = step.get('action')
        if "knead" in s: # bread or pasta
            step['action'] = ""
            for x in ingredients:
                if "flour" in x:
                    x = ""
                if "eggs" in x:
                    x = ""
        if "rise" in s:
            step['action'] = ""
            for x in ingredients:
                if "flour" in x:
                    x = ""
                if "eggs" in x:
                    x = ""
                if "yeast" in x:
                    x = ""
        if "grate" in s:
            cheese = re.search(r'\b(sprinkle\b)', step['action'])
            s = step['action'].split()[cheese:1]
            step['action'] = "sprinkle grated " + s
            
