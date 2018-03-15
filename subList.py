import parser

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

cBacon = parser.ingredient("Canadian bacon")
tBacon = parser.ingredient("turkey bacon")
sTurkey = parser.ingredient("smoked turkey")
leanPro = parser.ingredient("lean prosciutto")
wgBread = parser.ingredient("Whole-grain bread")
rOats = parser.ingredient("Rolled oats")
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
GreesePanButter = parser.ingredient("greese pan with Butter")
GreesePanMag = parser.ingredient("greese pan with margarine")
ffCheese = parser.ingredient("fat free cheese")

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
cheese = parser.ingredient("cheese")

nonHealthyDict = {
	bacon.ing["name"]:cBacon.ing,
	wBread.ing["name"]:wgBread.ing,
	bCrumbs.ing["name"]:rOats.ing,
	butter.ing["name"]:appSauce.ing,
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

spRice = parser.ingredient("spanish rice")
anejo = parser.ingredient("anejo")
asadero = parser.ingredient("asadero")
chihuahua = parser.ingredient("chihuahua")
cotija = parser.ingredient("cotija")
qFresco = parser.ingredient("queso fresco")
qdo = parser.ingredient("queso de oaxaca")



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




poPepper = parser.ingredient("poblano pepper")
sePepper = parser.ingredient("serano pepper")
haPepper = parser.ingredient("habanero pepper")
chilPow = parser.ingredient("chile-powder")
acPow = parser.ingredient("ancho chile-powder")
chipSalsa = parser.ingredient("chips and salsa on the side")

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

ajwain = parser.ingredient("ajwain")
amchoor = parser.ingredient("amchoor")
asafoetida = parser.ingredient("asafoetida")
blackCumin = parser.ingredient("black cumin seeds")
blackMustard = parser.ingredient("black mustard seeds")
brownMustard = parser.ingredient("brown mustard seeds")
cardamom = parser.ingredient("cardamom")
nigella = parser.ingredient("nigella")
whitePoppy = parser.ingredient("white poppy seeds")
sTurkey = parser.ingredient("smoked turkey")
tBreast = parser.ingredient("turkey breast")
tBacon = parser.ingredient("turkey bacon")
tSausage = parser.ingredient("turkey sausage")
turkey = parser.ingredient("turkey")
lamb = parser.ingredient("lamb")
gLamb = parser.ingredient("ground lamb")
lambRibs = parser.ingredient("lamb ribs")
lambShank = parser.ingredient("lamb shank")
lambShoulder = parser.ingredient("lamb shoulder")
scLamb = parser.ingredient("sirloin chop lamb")
naan = parser.ingredient("Naan")


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

raita = parser.ingredient("raita")
gChutney = parser.ingredient("Garlic chutney")
mAchaar = parser.ingredient("Mango Achaar")

indianSpciyList = [
	raita.ing, gChutney.ing, mAchaar.ing
]

commonSpicesList = ["salt", "pepper", "garlic", "onion", "butter", "oil", "water"]