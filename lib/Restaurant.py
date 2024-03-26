from __init__ import CONN, CURSOR

class Restaurant:
    def __init__(self, price, name=""):
        self.restaurant_name = name
        self.reviews = []
        self.price = price
        
    def get_name(self):
        return self.restaurant_name
    
    def add_review(self, review):
        self.reviews.append(review)
        
    def customers(self):
        return list(set([review.customer() for review in self.reviews]))
    
    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum([review.rating() for review in self.reviews])
        return total_ratings / len(self.reviews)
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS restaurant (
            id INTEGER PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            price REAL)
        """
        CURSOR.execute(sql)
        CONN.commit()
        