class Element:
    def __init__(self, name, category, id=None) -> None:
        self.id = id
        self.name = name
        self.category = category 

    def add_category(self, category):
        self.category.append(category)

    def save_element(self, conn):
        c = conn.cursor()
        c.execute("INSERT INTO element(name, category) VALUES (?,?) ",
                  (self.name, self.category))
