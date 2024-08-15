from walking import Donkey, Goat, Kangaroo, Llama, Pig
from slithering import BoaConstrictor, Copperhead, CoralSnake, RatSnake, WaterMoccasin
from swimming import Catfish, Flamingo, Goldfish, Mallard, Swan

miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "morning")
frijoles = Donkey("Frijoles", "Domesticated Equine", "midday")
oreo = Goat("Oreo", "LaMancha", "afternoon")
joey = Kangaroo("Joey", "Red Kangaroo", "midday")
ham = Pig("Ham", "Red River Hog", "afternoon")
rick = Copperhead("Rick", "Northern Copperhead")
stew = RatSnake("Stew", "Spilotes Pullatus")
marilyn = BoaConstrictor("Marilyn", "Short-Tailed Boa")
mr_stripey = CoralSnake("Mr. Stripey", "Eastern Coral Snake")
carl = WaterMoccasin("Carl", "Agkistrodon Piscivorus")
mr_quack = Mallard("Mr. Quack", "Anas Platyrhynchos")
murphy = Goldfish("Murphy", "Shubunkin")
grace = Swan("Grace", "Tundra Swan")
benny = Catfish("Benny", "Upside-Down Catfish")
stanley = Flamingo("Stanley", "Chilean Flamingo")

print(
    f"{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift} shift."
)
