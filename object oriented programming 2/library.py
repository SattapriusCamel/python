class library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}
    
    def displayBooks(self):
        print(f"We have the following books at this moments...")
        for book in self.booksList:
            print(book)
    
    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user}) 
            print("Book borrowed! You can take the book now...")
        else:
            print(f"The book is already taken by {self.lendDict[book]}")
    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list!")
    def returnBook(self, book):
        self.lendDict.pop(book)
    
    if __name__ == '__main__':
        books = Library(['Thomas The Tank Engine', 'Harry Potter', 'The Hobbit', 'Scratch Basics', 'Python Basics', 'Romeo and Juilet', 'Captain Underpants', 'ABBAS Neck PHYSIQUE'])
    while (True):
        print(f"Welcome to the {books.name} library. Choose your choice...")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
