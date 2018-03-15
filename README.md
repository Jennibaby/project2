# project2

### Step 1:  Install packages 
```
install bs4
install requests
install nltk
```

### Windows 
```
open windows commad prompt (Admin)
python -m pip install bs4
python -m pip install nltk
python -m pip install requests
```
### mac/linux

```
in console/terminal
pip install bs4
pip install nltk
pip install requests
(if you get a permissions error use sudo pip install and enter password when prompted)
```
### Setup nltk (download stopwords)
```
python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
```


### Step 2:  Enter URL
```
find the url of the recipe you would like to parse.
open main.py and in line 7 (url = ...) paste the url
```

### Step 3:  Run
```
run main.py from ide or in python console
```
