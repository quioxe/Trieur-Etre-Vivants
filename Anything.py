#Les vertébrés-------------------------------------------------------------------------------
oiseau = ["perroquet", "poule", "poulet", "coq", "canard", "dinde", "dindon", "colibri", "mésange", "rouge-gorge", "corbeau", "perruche", "canard"]
amphibien = ["grenouilles", "crapauds", "salamandres"]
poisson = ["anguille", "saumon", "sardines", "maquereau", "morue", "thon", "raie", "gobie", "poisson rouge", "poisson clown"]
reptile = ["crocodiles", "serpents", "alligators", "lézards", "tortue"]
mammifère = ["humain", "ours", "loup", "chien", "renard", "dauphin", "lapin", "chat", "chaton", "chauve-souris", "balleine", "hérisson", "hamster", "cochon d'inde"]
chordé = [mammifère, reptile, poisson, amphibien, oiseau]
#--------------------------------------------------------------------------------------------
vertébré = [chordé]

#Les invertébrés-----------------------------------------------------------------------------
arachnide = ["araignées"]
crustacé = ["crabe", "homard", "langouste", "crevette"]
insecte = ["moustiques", "libellules", "papillons"]
arthropode = [insecte, crustacé, arachnide]
mollusque = ["escargot", "moule", "huitre", "saint-jacques", "palourde", "bigorneau", "pétoncle", "amande de mer", "bucarde", "bulot", "clam", "coque", "ormeau", "patelle", "pouce-pied", "praire", "telline"]
#--------------------------------------------------------------------------------------------
invertébré = [mollusque, arthropode]

#Les ANIMAUX
animal = [vertébré, invertébré]

#La liste FINALE
elements = [animal]

inp = input("Quel élément voulez-vous trier : ")