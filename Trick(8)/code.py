class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages
    
book = Book('Derakhshan',480)
print(len(book))