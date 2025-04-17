from mylibrary import Library

x = Library("Power Electronics", "Rashid")
mybook = Library("Mathematics", "John Smith")

if __name__ == "__main__":
    print("Add Book \t-\t-\t Remove Book \t-\t-\t Show Book")
    print(mybook.show_book())
