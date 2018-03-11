# TODO is there a way to detect type of recepie (would it be ok to add jalapeno to recepie for example which would be preferable to just trying to substitute a different peppers
# if recepie contains spicy ingredients -> can add peppers and such
mexican = (
    ("spanish rice", "white rice"),
("anejo"),
("asadero"),
("chihuahua"),
("cotija"),
("queso fresco"),
("queso de oaxaca"),
("queso panela"),
)

non_mexican = (
("wild rice", "brown rice"),
("romano"),
("teleme", "muenster", "provolone"),
("monterey jack", "mild cheddar", "cheddar"),
("parmesan"),
("ricotta", "french feta", "feta"),
("mozzarella"),
("monterey jack"),
)

# some ingredients are mexian but indicates spicy so we can add more mexican
spicy_indicators = (
    ("Harissa", "Red chili paste", "sriracha", "tabasco"),
("wasabi", "horseradish", "whole grain mustard", "ginger", "mustard powder"),
    ("dried thai chilies", "jalapeno", "peppercorns", "red chili flakes", "szechuan peppercorns", "gochujang", "aleppo pepper"),
    ("curry"),
    ("garlic powder", "chili powder", "cumin"),
    ("oregano", "cilantro")
)

spicy_additions = (
    (""), # TODO write in list if we think this is a good idea
    (""),
    ("poblano pepper", "serano pepper", "habanero pepper"),
    ("chile powder", "ancho chile powder"),
    ("poblano pepper", "serano pepper", "habanero pepper"),
    ("poblano pepper", "serano pepper", "habanero pepper", "jalapeno pepper"),
)