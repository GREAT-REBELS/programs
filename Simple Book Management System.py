class Library:
    def __init__(self,books):
        self.books = books
    def list_books(self):
        print("Available Books")
        for book in books:
            print(book)
    def borrow_book(self, borrow_book):
        if borrow_book in books:
            print("Book Borrowed Sucessfully")
            self.books.remove(borrow_book)
        else:
            print("Book Not Available")
    def receive_book(self, receive_book):
        print("You have returned the book")
        self.books.append(receive_book)
        
books = ["Java","C","C++","R","Big Data","Sql"]
obj = Library(books)
msg = """
     1.Display books
     2.Borrow_book
     3.Receive_book
     """
while True:
    print(msg)
    N=int(input("Enter Your Choice : "))
    if(N==0):
        print("Thank You")
        quit()
    elif N==1:
        obj.list_books()
    elif N==2:
        book = input("Enter the Book Name to borrow : ")
        obj.borrow_book(book)
    elif N==3:
        book = input("Enter the Book Name to return : ")
        obj.receive_book(book)
    else:
        print("Invalid choice")
