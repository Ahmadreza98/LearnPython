class Library:
    book_list = []

    def __init__(self, title, auther):
        self.title = title
        self.auther = auther
        self.book_list.append([title, auther])

    def add_book(self, title, auther):
        self.book_list.append([title, auther])
        print("The book saved.")

    def remove_book(self, title):
        for ind, val in enumerate(self.book_list):
            if title in val:
                self.book_list.pop(ind)
        print("The book removed.")

    def search_book(self, title):
        for ind, val in enumerate(self.book_list):
            if title in val:
                print(f"The book founded, the book name is "
                      f"{self.book_list[ind][1]}")
            else:
                print("the book not found")

    def show_book(self):
        return self.book_list

