import parserrrrrr

tofu = parserrrrrr.ingredient("sliced tofu")
seitan = parserrrrrr.ingredient("sliced seitan")
tempeh = parserrrrrr.ingredient("sliced tempeh")
lentil = parserrrrrr.ingredient("burger patty")
mushroom = parserrrrrr.ingredient("large portabella mushroom")
texturedVegetableProtein = parserrrrrr.ingredient("dry Textured Vegetable Protein")
nonChickenBroh = parserrrrrr.ingredient("Better-Than Boullion non-chicken broth")
nonBeefBroh = parserrrrrr.ingredient("Better-Than Boullion non-beef broth")

meatsubList = [tofu.ing,seitan.ing,tempeh.ing,lentil.ing,mushroom.ing,texturedVegetableProtein.ing]

slicedBacon = parserrrrrr.ingredient("slice of bacon")
beef = parserrrrrr.ingredient("ground beef")
caribou = parserrrrrr.ingredient("T-bone steak of caribou")
chicken = parserrrrrr.ingredient("chicken breast")
salmon = parserrrrrr.ingredient("fillet of salmon")
duck = parserrrrrr.ingredient("tenderloin of duck")
halibut = parserrrrrr.ingredient("fillet of halibut")
ham = parserrrrrr.ingredient("slice of pork loin")
lamb = parserrrrrr.ingredient("rib of lamb")
mutton = parserrrrrr.ingredient("fillet of mutton")
pork = parserrrrrr.ingredient("slice of pork loin")
snapper = parserrrrrr.ingredient("fillet of snapper")
turkey = parserrrrrr.ingredient("turkey breast")
veal = parserrrrrr.ingredient("fillet of veal")
venison = parserrrrrr.ingredient("steak of venison")
walleye = parserrrrrr.ingredient("fillet of walleye")
yellowfinTuna = parserrrrrr.ingredient("fillet of yellowfin tuna")

nonMeatSubList = [slicedBacon.ing, beef.ing, caribou.ing, chicken.ing, salmon.ing, duck.ing, halibut.ing, ham.ing, lamb.ing, mutton.ing, pork.ing, snapper.ing, turkey.ing, veal.ing, venison.ing, walleye.ing, yellowfinTuna.ing]

cBacon = parserrrrrr.ingredient("Canadian bacon")
tBacon = parserrrrrr.ingredient("turkey bacon")
sTurkey = parserrrrrr.ingredient("smoked turkey")
leanPro = parserrrrrr.ingredient("lean prosciutto")
wgBread = parserrrrrr.ingredient("Whole-grain bread")
rOats = parserrrrrr.ingredient("Rolled oats")
cbCereal = parserrrrrr.ingredient("crushed bran cereal")
gfSeeds = parserrrrrr.ingredient("ground flax seeds")
appSauce = parserrrrrr.ingredient("Applesauce")
cSpray = parserrrrrr.ingredient("cooking spray")
eWhite = parserrrrrr.ingredient("egg white")
wpFlour = parserrrrrr.ingredient("whole-wheat pastry flour")
elgBeef = parserrrrrr.ingredient("Extra-lean ground beef")
lgBeef = parserrrrrr.ingredient("lean ground beef")
gChicken = parserrrrrr.ingredient("ground chicken breast")
gTurkey = parserrrrrr.ingredient("ground turkey breast")
arugula = parserrrrrr.ingredient("Arugula")
chicory = parserrrrrr.ingredient("chicory")
cGreen = parserrrrrr.ingredient("collard greens")
kale = parserrrrrr.ingredient("kale")
spinach = parserrrrrr.ingredient("spinach")
watercress = parserrrrrr.ingredient("watercress")
rcMayon = parserrrrrr.ingredient("Reduced-calorie mayonnaise")
esMilk = parserrrrrr.ingredient("Evaporated skim milk")
rfMilk = parserrrrrr.ingredient("Reduced fat milk")
sMilk = parserrrrrr.ingredient("skim milk")
wPasta = parserrrrrr.ingredient("whole-wheat pasta")
bRice = parserrrrrr.ingredient("Brown rice")
wildRice = parserrrrrr.ingredient("wild rice")
ffSourCream = parserrrrrr.ingredient("Fat free sour cream")
lfSourCream = parserrrrrr.ingredient("low-fat sour cream")
lfpYogurt = parserrrrrr.ingredient("low-fat plain yogurt")
ffpYogurt = parserrrrrr.ingredient("fat-free plain yogurt")
gYogurt = parserrrrrr.ingredient("greek yogurt")
plYogurt = parserrrrrr.ingredient("plain low-fat yogurt")
stevia = parserrrrrr.ingredient("stevia")
cNibs = parserrrrrr.ingredient("cacao nibs")
cOil = parserrrrrr.ingredient("coconut oil")
ffcCheese = parserrrrrr.ingredient("Fat free cream cheese")
GreesePanButter = parserrrrrr.ingredient("greese pan with Butter")
GreesePanMag = parserrrrrr.ingredient("greese pan with margarine")
ffCheese = parserrrrrr.ingredient("fat free cheese")
butterOrMargarine = parserrrrrr.ingredient("butter or margarine")

bacon = parserrrrrr.ingredient("Bacon")
wBread = parserrrrrr.ingredient("white bread")
bCrumbs = parserrrrrr.ingredient("Bread crumbs")
butter = parserrrrrr.ingredient("Butter")
margarine = parserrrrrr.ingredient("margarine")
egg = parserrrrrr.ingredient("Eggs")
apFlour = parserrrrrr.ingredient("all-purpose flour")
gBeef = parserrrrrr.ingredient("ground beef")
iLettuce = parserrrrrr.ingredient("iceberg lettuce")
mayon = parserrrrrr.ingredient("mayonnaise")
eMilk = parserrrrrr.ingredient("evaporated milk")
wMilk = parserrrrrr.ingredient("whole milk")
pasta = parserrrrrr.ingredient("pasta")
wRice = parserrrrrr.ingredient("white rice")
sCream = parserrrrrr.ingredient("sour cream")
yogurt = parserrrrrr.ingredient("yogurt")
sugar = parserrrrrr.ingredient("sugar")
cChips = parserrrrrr.ingredient("chocolate chips")
vOil = parserrrrrr.ingredient("vegetable oil")
cCheese = parserrrrrr.ingredient("cream cheese")
cheese = parserrrrrr.ingredient("cheese")

nonHealthyDict = {
	bacon.ing["name"]:cBacon.ing,
	wBread.ing["name"]:wgBread.ing,
	bCrumbs.ing["name"]:rOats.ing,
	butter.ing["name"]:appSauce.ing,
	butterOrMargarine.ing["name"]:appSauce.ing,
	margarine.ing["name"]:appSauce.ing,
	GreesePanButter.ing["name"]:cSpray.ing,
	GreesePanMag.ing["name"]:cSpray.ing,
	egg.ing["name"]:eWhite.ing,
	apFlour.ing["name"]:wpFlour.ing,
	gBeef.ing["name"]:elgBeef.ing,
	iLettuce.ing["name"]:arugula.ing,
	mayon.ing["name"]:rcMayon.ing,
	eMilk.ing["name"]:esMilk.ing,
	wMilk.ing["name"]:rfMilk.ing,
	pasta.ing["name"]:wPasta.ing,
	wRice.ing["name"]:bRice.ing,
	sCream.ing["name"]:ffSourCream.ing,
	yogurt.ing["name"]:plYogurt.ing,
	sugar.ing["name"]:stevia.ing,
	cChips.ing["name"]:cNibs.ing,
	vOil.ing["name"]:cOil.ing,
	cCheese.ing["name"]:ffcCheese.ing,
	cheese.ing["name"]:ffCheese.ing
}

healtyDict = {
	cBacon.ing["name"]:bacon.ing,
	tBacon.ing["name"]:bacon.ing,
	sTurkey.ing["name"]:bacon.ing,
	leanPro.ing["name"]:bacon.ing,
	wgBread.ing["name"]:wBread.ing,
	rOats.ing["name"]:bCrumbs.ing,
	cbCereal.ing["name"]:bCrumbs.ing,
	gfSeeds.ing["name"]:bCrumbs.ing,
	appSauce.ing["name"]:butter.ing,
	cSpray.ing["name"]:GreesePanButter.ing,
	eWhite.ing["name"]:egg.ing,
	wpFlour.ing["name"]:apFlour.ing,
	elgBeef.ing["name"]:gBeef.ing,
	lgBeef.ing["name"]:gBeef.ing,
	gChicken.ing["name"]:gBeef.ing,
	gTurkey.ing["name"]:gBeef.ing,
	arugula.ing["name"]:iLettuce.ing,
	chicory.ing["name"]:iLettuce.ing,
	cGreen.ing["name"]:iLettuce.ing,
	kale.ing["name"]:iLettuce.ing,
	spinach.ing["name"]:iLettuce.ing,
	watercress.ing["name"]:iLettuce.ing,
	rcMayon.ing["name"]:mayon.ing,
	esMilk.ing["name"]:eMilk.ing,
	rfMilk.ing["name"]:wMilk.ing,
	sMilk.ing["name"]:wMilk.ing,
	wPasta.ing["name"]:pasta.ing,
	bRice.ing["name"]:wRice.ing,
	wildRice.ing["name"]:wRice.ing,
	ffSourCream.ing["name"]:sCream.ing,
	lfSourCream.ing["name"]:sCream.ing,
	lfpYogurt.ing["name"]:sCream.ing,
	ffpYogurt.ing["name"]:sCream.ing,
	gYogurt.ing["name"]:sCream.ing,
	plYogurt.ing["name"]:yogurt.ing,
	stevia.ing["name"]:sugar.ing,
	cNibs.ing["name"]:cChips.ing,
	cOil.ing["name"]:vOil.ing,
	ffcCheese.ing["name"]:cCheese.ing,
	ffCheese.ing["name"]:cheese.ing
}


non_mexican = ["rice", "romano", "teleme", "muenster", "provolone", "monterey jack", "cheddar", "parmesan", "ricotta","feta", "mozzarella"]

spRice = parserrrrrr.ingredient("spanish rice")
anejo = parserrrrrr.ingredient("anejo")
asadero = parserrrrrr.ingredient("asadero")
chihuahua = parserrrrrr.ingredient("chihuahua")
cotija = parserrrrrr.ingredient("cotija")
qFresco = parserrrrrr.ingredient("queso fresco")
qdo = parserrrrrr.ingredient("queso de oaxaca")



mexicanSubDict = {
	"rice":spRice.ing,
	"romano":anejo.ing,
	"teleme":asadero.ing,
	"muenster":asadero.ing,
	"provolone":asadero.ing,
	"monterey jack":chihuahua.ing,
	"cheddar":chihuahua.ing,
	"parmesan":cotija.ing,
	"ricotta":qFresco.ing,
	"feta":qFresco.ing,
	"mozzarella":qdo.ing
}


nonMexicanSpicyList = ["dried thai chilies", "jalapeno", "peppercorns", "red chili flakes", "szechuan peppercorns", "gochujang", "aleppo pepper", "curry", "garlic powder", "chili powder", "cumin", "oregano", "cilantro", "chopped onion"]




poPepper = parserrrrrr.ingredient("poblano pepper")
sePepper = parserrrrrr.ingredient("serano pepper")
haPepper = parserrrrrr.ingredient("habanero pepper")
chilPow = parserrrrrr.ingredient("chile-powder")
acPow = parserrrrrr.ingredient("ancho chile-powder")
chipSalsa = parserrrrrr.ingredient("chips and salsa on the side")

mexicanSpicyList = [poPepper.ing, sePepper.ing, haPepper.ing, chilPow.ing, acPow.ing, chipSalsa.ing]

nonMexicanSpicySubDict = {
	"dried thai chilies":poPepper.ing,
	"jalapeno":sePepper.ing,
	"peppercorns":haPepper.ing,
	"red chili flakes":poPepper.ing,
	"szechuan peppercorns":haPepper.ing,
	"gochujang":haPepper.ing,
	"aleppo pepper":sePepper.ing,
	"curry":chilPow.ing,
	"garlic powder":sePepper.ing,
	"chili powder":haPepper.ing,
	"cumin":poPepper.ing,
	"oregano":chipSalsa.ing,
	"cilantro":chipSalsa.ing,
	"chopped onion":chipSalsa.ing
}


# non_indian = [
#     "dried thyme", "mild oregano","lime juice", "lime powder","garlic powder","sesame seeds","wasabi", "horseradish","cinnamon", "nutmeg", "ginger", "ground cloves","celery seeds", "oregano","poppy seeds","ham","pork chop", "pork loin","bacon","pork sausage","pork","beef","ground beef","beef ribs","beef shank","beef shoulder", "beef chuck","beef sirloin","bread"
# ]

ajwain = parserrrrrr.ingredient("ajwain")
amchoor = parserrrrrr.ingredient("amchoor")
asafoetida = parserrrrrr.ingredient("asafoetida")
blackCumin = parserrrrrr.ingredient("black cumin seeds")
blackMustard = parserrrrrr.ingredient("black mustard seeds")
brownMustard = parserrrrrr.ingredient("brown mustard seeds")
cardamom = parserrrrrr.ingredient("cardamom")
nigella = parserrrrrr.ingredient("nigella")
whitePoppy = parserrrrrr.ingredient("white poppy seeds")
sTurkey = parserrrrrr.ingredient("smoked turkey")
tBreast = parserrrrrr.ingredient("turkey breast")
tBacon = parserrrrrr.ingredient("turkey bacon")
tSausage = parserrrrrr.ingredient("turkey sausage")
turkey = parserrrrrr.ingredient("turkey")
lamb = parserrrrrr.ingredient("lamb")
gLamb = parserrrrrr.ingredient("ground lamb")
lambRibs = parserrrrrr.ingredient("lamb ribs")
lambShank = parserrrrrr.ingredient("lamb shank")
lambShoulder = parserrrrrr.ingredient("lamb shoulder")
scLamb = parserrrrrr.ingredient("sirloin chop lamb")
naan = parserrrrrr.ingredient("Naan")


nonIndianDict = {
	"thyme":ajwain.ing,
	"oregano":ajwain.ing,
	"lime juice":amchoor.ing,
	"lime powder":amchoor.ing,
	"garlic powder":asafoetida.ing,
	"sesame seeds":blackCumin.ing,
	"wasabi":blackMustard.ing,
	"horseradish":brownMustard.ing,
	"cinnamon":cardamom.ing,
	"nutmeg":cardamom.ing,
	"ginger":cardamom.ing,
	"cloves":cardamom.ing,
	"celery seeds":nigella.ing,
	"oregano":nigella.ing,
	"poppy seeds":whitePoppy.ing,
	"ham":sTurkey.ing,
	"pork chop":tBreast.ing,
	"pork loin":tBreast.ing,
	"bacon":tBacon.ing,
	"pork sausage":tSausage.ing,
	"pork":turkey.ing,
	"beef":gLamb.ing,
	"beef ribs":lambRibs.ing,
	"beef shank":lambShank.ing,
	"beef shoulder":lambShoulder.ing,
	"beef chuck":lambShoulder.ing,
	"beef sirloin":scLamb.ing,
	"bread":naan.ing
}

raita = parserrrrrr.ingredient("raita")
gChutney = parserrrrrr.ingredient("Garlic chutney")
mAchaar = parserrrrrr.ingredient("Mango Achaar")

indianSpciyList = [
	raita.ing, gChutney.ing, mAchaar.ing
]

commonSpicesList = ["salt", "pepper", "garlic", "onion", "butter", "oil", "water"]