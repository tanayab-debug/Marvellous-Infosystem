class BookStore():
    NoOfBooks = 0

    def __init__(self, Name, Author):
        self.BookName = Name
        self.AuthorName = Author
        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.BookName} by {self.AuthorName}. Number of Books:{self.NoOfBooks}")

obj = BookStore("1988","George Orwell")
obj.Display()

obj1 = BookStore("Dodger", "Terry Prachet")
obj1.Display()