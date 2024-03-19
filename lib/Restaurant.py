class Restaurant:
    def __init__(self, name=""):
        self.restaurant_name = name
        self.reviews = []
        
    def get_name(self):
        return self.restaurant_name
    
    def add_review(self, review):
        self.reviews.append(review)