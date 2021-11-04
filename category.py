from sqlite3.dbapi2 import Cursor
import database

class Category:
    def __init__(self, name, parent_category=None, id=None) -> None:
        self.name = name
        self.parent_category = parent_category

    def __init__(self, id) -> None:
        cursor = database.get_cursor()
        cursor.execute("SELECT * FROM category WHERE id = (?)", (str(id), ))
        category = cursor.fetchall()
        
        if len(category) == 1:
            self.name = category[0][1]
            self.id = category[0][0]
            if(category[0][2]):
                self.parent_category = Category(category[0][2])
            else: self.parent_category = None

    def save(self):
        cursor = database.get_cursor()
        cursor.execute("INSERT INTO category (name, category_id) VALUES (?,?)",
                  (self.name, self.category_id.get_id()))
        database.conn.commit()

    @staticmethod
    def get_categories():
        
        c = database.get_cursor() 
        c.execute("SELECT * FROM category")
        categories = c.fetchall()
        return categories

    @staticmethod
    def category_listing():
        categories = Category.get_categories()
        for category in categories:
            category_obj = Category(category[0])
            if(category_obj.get_parent_category()):
                print("Index: " + str(category_obj.get_id()) + ", nume : " +
                      category_obj.get_name() + ", parent : " + category_obj.get_parent_category().get_name())
            else:
                print("Index: " + str(category_obj.get_id()) + ", nume : " +
                      category_obj.get_name() + ", parent : None")
    

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_parent_category(self):
        return self.parent_category
