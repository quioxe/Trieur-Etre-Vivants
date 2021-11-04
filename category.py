class Category:
    def __init__(self, name, category_id = None, id=None) -> None:
        self.name = name
        self.category_id = category_id

    def save(self, conn):
        c = conn.cursor()
        c.execute("INSERT INTO category (name, category_id) VALUES (?,?)",
                  (self.name, self.category_id))
        conn.commit()

    @staticmethod
    def get_categories(conn):
        c = conn.cursor()
        c.execute("SELECT * FROM category")
        categories = c.fetchall()
        return categories


