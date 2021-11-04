from category import Category
import database
from element import Element


if __name__ == '__main__':
    conn = database.create_connection("sqlite.db")
    if conn is not None:
        sql_create_tables = ("CREATE TABLE IF NOT EXISTS element(id integer PRIMARY KEY AUTOINCREMENT, name text NOT NULL, category_id integer NOT NULL, FOREIGN KEY(category_id) REFERENCES category(id))",
                             "CREATE TABLE IF NOT EXISTS category(id integer PRIMARY KEY AUTOINCREMENT, name text NOT NULL, category_id integer)")
        for sql in sql_create_tables:
            database.create_table(conn, sql)
    else:
        print("Can't connect to database")
            

    

    #perroquet = Element("perroquet")
    #perroquet.add_category("oiseau")
    #perroquet.save_element(conn)

#Les vertébrés-------------------------------------------------------------------------------
oiseau = ["perroquet", "poule", "poulet", "coq", "canard", "dinde", "dindon", "colibri", "mésange", "rouge-gorge", "corbeau", "perruche", "canard"]
amphibien = ["grenouilles", "crapauds", "salamandres"]
poisson = ["anguille", "saumon", "sardines", "maquereau", "morue", "thon", "raie", "gobie", "poisson rouge", "poisson clown"]
reptile = ["crocodiles", "serpents", "alligators", "lézards", "tortue"]
mammifere = ["humain", "ours", "loup", "chien", "renard", "dauphin", "lapin", "chat", "chaton", "chauve-souris", "balleine", "hérisson", "hamster", "cochon d'inde"]
chorde = [mammifere, reptile, poisson, amphibien, oiseau]
#--------------------------------------------------------------------------------------------
vertebre = [chorde]

#Les invertébrés-----------------------------------------------------------------------------
arachnide = ["araignées"]
crustace = ["crabe", "homard", "langouste", "crevette"]
insecte = ["moustiques", "libellules", "papillons"]
arthropode = [insecte, crustace, arachnide]
mollusque = ["escargot", "moule", "huitre", "saint-jacques", "palourde", "bigorneau", "pétoncle", "amande de mer", "bucarde", "bulot", "clam", "coque", "ormeau", "patelle", "pouce-pied", "praire", "telline"]
#--------------------------------------------------------------------------------------------
invertebre = [mollusque, arthropode]

#Les ANIMAUX
animal = [vertebre, invertebre]

#La liste FINALE
inp = input("1. Voulez vous introduire une categorie ? Appuyez 1 ")


def create_category(conn):
    category_name = input("Dites moi le nom de la categorie: ")
    print("Dites moi le parent de la categorie: ")
    categories = Category.get_categories(conn)
    for category in categories:
        print("Index: " + str(category[0]) + ", nume : " + category[1])
    category_parent = input("Alors, le index est: ")
    category = Category(category_name, category_parent)
    category.save(conn)
if (inp == "1"):
    create_category(conn)
print(Category.get_categories(conn))






