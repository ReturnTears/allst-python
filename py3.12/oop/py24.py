class PyBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"《{self.title}》 by {self.author}"

book = PyBook("Python 3.12", "Eric Matthes")
print(book)
print(repr(book))
