healthy = (
    ("Canadian bacon", "turkey bacon", "smoked turkey", "lean prosciutto"),
    ("Whole-grain bread"),
    ("Rolled oats", "crushed bran cereal", "ground flax seeds"),
    ("1/2 Applesauce, 1/2 butter"),
    ("cooking spray"),
    ("Fat-free half-and-half", "evaporated skim milk"),
    ("Fat free cream cheese", "low-fat cream cheese", "low-fat cottage cheese"),
    ("2 egg whites"),
    ("1/2 whole-wheat flour, 1/2 flour", "whole-wheat pastry flour"),
    ("Extra-lean ground beef", "lean ground beef", "ground chicken breast", "ground turkey breast"),
    ("Arugula", "chicory", "collard greens", "kale", "spinach", "watercress"),
    ("Reduced-calorie mayonnaise"),
    ("Evaporated skim milk"),
    ("Reduced fat milk", "skim milk"), # check, might not be able to use skim milk if alreayd used.  change reduced fat milk to 2%?
    ("whole-wheat pasta"),
    ("Brown rice", "wild rice"),
    ("Fat free sour cream", "low-fat sour cream", "low-fat plain yogurt", "fat-free plain yogurt", "greek yogurt"),
    ("plain low-fat yogurt"),
    ("1/2 sugar, 1/2 stevia"),
    ("cacao nibs"),
    ("coconut oil")
)

not_healthy = (
    ("Bacon"),
    ("white bread"),
    ("Bread crumbs"),
    ("Butter", "margarine"),
    ("greese pan with Butter", "greese pan with margarine"), # combined step w ingredient
    ("Eggs"),
    ("all-purpose flour"),
    ("ground beef"),
    ("iceberg lettuce"),
    ("mayonnaise"),
    ("evaporated milk"),
    ("whole milk"),
    ("pasta"),
    ("white rice"),
    ("sour cream"),
    ("yogurt"),
    ("sugar"),
    ("chocolate chips"),
    ("vegetable oil")
)