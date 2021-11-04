from database import Database

class Category:
    def __init__(self, name, category_id = None, id=None) -> None:
        self.name = name
        self.category_id = category_id

    def __init__(self, id) -> None:
        db = Database()
        c= db.conn.cursor() 
        c.execute("SELECT * FROM category WHERE id = (?)", str(id))
        category = c.fetchall()
        if len(category) == 1:
            return Category(category[0][1], category[0][2], category[0][0])
        else:
            print("Categorie avec le index " + str(id) + "n'existe pas.")
            return None


    def save(self):
        db = Database()
        c= db.conn.cursor() 
        c.execute("INSERT INTO category (name, category_id) VALUES (?,?)",
                  (self.name, self.category_id))
        db.conn.commit()

    @staticmethod
    def get_categories():
        db = Database()
        c= db.conn.cursor() 
        c.execute("SELECT * FROM category")
        categories = c.fetchall()
        return categories

    @staticmethod
    def category_listing():
        categories = Category.get_categories()
        for category in categories:
            parent_category = Category(category[2])
            print("Index: " + str(category[0]) + ", nume : " + category[1] + ", parent : " + parent_category.get_name())
        
    

    def get_name(self):
        return(self.name)