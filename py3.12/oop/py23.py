class PyBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "《%s》 by %s" % (self.title, self.author)

book = PyBook("Python Crash Course", "Eric Matthes")
print(book)
print(str(book))
