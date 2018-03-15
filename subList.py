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



cBacon = parser.ingredient("Canadian bacon")
tBacon = parser.ingredient("turkey bacon")
sTurkey = parser.ingredient("smoked turkey")
leanPro = parser.ingredient("lean prosciutto")
wgBread = parser.ingredient("Whole-grain bread")
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

# healtyDict = {
#     canadianbacon.ing["name"]:bacon.ing,
#     turkeybacon.ing["name"]:bacon.ing,
#     smokedturkey.ing["name"]:bacon.ing,
#     leanprosciutto.ing["name"]:bacon.ing,
#     whole-grainbread.ing["name"]:whitebread.ing,
#     rolledoats.ing["name"]:breadcrumbs.ing,
#     crushedbrancereal.ing["name"]:breadcrumbs.ing,
#     groundflaxseeds.ing["name"]:breadcrumbs.ing,
#     applesauce.ing["name"]:butter.ing,
#     cookingspray.ing["name"]:greesepanwithbutter.ing,
#     eggwhite.ing["name"]:eggs.ing,
#     whole-wheatpastryflour.ing["name"]:allpurposeflour.ing,
#     extra-leangroundbeef.ing["name"]:groundbeef.ing,
#     leangroundbeef.ing["name"]:groundbeef.ing,
#     groundchickenbreast.ing["name"]:groundbeef.ing,
#     groundturkeybreast.ing["name"]:groundbeef.ing,
#     arugula.ing["name"]:iceberglettuce.ing,
#     chicory.ing["name"]:iceberglettuce.ing,
#     collardgreens.ing["name"]:iceberglettuce.ing,
#     kale.ing["name"]:iceberglettuce.ing,
#     spinach.ing["name"]:iceberglettuce.ing,
#     watercress.ing["name"]:iceberglettuce.ing,
#     reduced-caloriemayonnaise.ing["name"]:mayonnaise.ing,
#     evaporatedskimmilk.ing["name"]:evaporatedmilk.ing,
#     reducedfatmilk.ing["name"]:wholemilk.ing,
#     skimmilk.ing["name"]:wholemilk.ing,
#     whole-wheatpasta.ing["name"]:pasta.ing,
#     brownrice.ing["name"]:whiterice.ing,
#     wildrice.ing["name"]:whiterice.ing,
#     fatfreesourcream.ing["name"]:sourcream.ing,
#     low-fatsourcream.ing["name"]:sourcream.ing,
#     low-fatplainyogurt.ing["name"]:sourcream.ing,
#     fat-freeplainyogurt.ing["name"]:sourcream.ing,
#     greekyogurt.ing["name"]:sourcream.ing,
#     plainlow-fatyogurt.ing["name"]:yogurt.ing,
#     stevia.ing["name"]:sugar.ing,
#     cacaonibs.ing["name"]:chocolatechips.ing,
#     coconutoil.ing["name"]:vegetableoil.ing,
#     fatfreecreamcheese.ing["name"]:creamcheese.ing
# }
#
#
# nonHealthyDict = {
#     bacon.ing["name"]: canadianbacon.ing,
#     whitebread.ing["name"]: whole-grainbread.ing,
#     breadcrumbs.ing["name"]: rolledoats.ing,
#     butter.ing["name"]: applesauce.ing,
#     margarine.ing["name"]: applesauce.ing,
#     greesepanwithButter.ing["name"]: cookingspray.ing,
#     eggs.ing["name"]: eggwhite.ing,
#     allpurposeflour.ing["name"]: whole - wheatpastryflour.ing,
#     groundbeef.ing["name"]: extra - leangroundbeef.ing,
#     iceberglettuce.ing["name"]: arugula.ing,
#     mayonnaise.ing["name"]: reduced - caloriemayonnaise.ing,
#     evaporatedmilk.ing["name"]: evaporatedskimmilk.ing,
#     wholemilk.ing["name"]: reducedfatmilk.ing,
#     pasta.ing["name"]: whole - wheatpasta.ing,
#     whiterice.ing["name"]: brownrice.ing,
#     sourcream.ing["name"]: fatfreesourcream.ing,
#     yogurt.ing["name"]: plainlow - fatyogurt.ing,
#     sugar.ing["name"]: stevia.ing,
#     chocolatechips.ing["name"]: cacaonibs.ing,
#     vegetableoil.ing["name"]: coconutoil.ing,
#     creamcheese.ing["name"]: fatfreecreamcheese.ing
# }