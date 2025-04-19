class Library:
    book_list = []

    def __init__(self, title, auther):
        self.title = title
        self.auther = auther
        self.book_list = [[title, auther]]

    def add_book(self, title, auther):
        self.book_list.append([title, auther])

    def remove_book(self, title):
        for ind, val in enumerate(self.book_list):
            if title in val:
                self.book_list.pop(ind)

    def search_book(self, title):

        for ind, val in enumerate(self.book_list):
            if title in val:
                print(f"The {val[0]} with auther {val[1]} is Exist.")

    def show_book(self):
        print(self.book_list)