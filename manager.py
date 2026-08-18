from book import Book
import json

class BookManager:
    def __init__(self):
        self.books = []

    def save_books(self):
        data = []
        for book in self.books:
            data.append(book.__dict__)
        with open('books.json', 'w',encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_books(self):
        try:
            with open('books.json','r',encoding='utf-8') as f:
                data = json.load(f)
                self.books = []
                for items in data:
                    book = Book(
                        items['name'],
                        items['author'],
                        items['price'],
                        items['book_id'],
                        items['count'],
                    )
                    self.books.append(book)
        except FileNotFoundError:
            self.books = []
            return self.books



    def add_books(self, book):
        self.books.append(book)
        self.save_books()

    def show_books(self):
        for index,book in enumerate(self.books):
            print(index,book.show_info())


    def borrow_books(self,num1,num2):
        found = False
        for index,book in enumerate(self.books):
            if num1 == book.book_id:
                found = True
                if num2 > 5:
                    print('一次最多借5本')
                    return
                elif num2 <= 0:
                    print('借书的数量必须大于0')
                    return
                result = book.borrow_book(num2)
                if result:
                    print('成功借出')
                    self.save_books()
                    self.show_books()
                else:
                    print('剩余图书小于借阅数量')
                    return
        if not found:
            print('没找到该书')


    def return_books(self,num1,num2):
        found = False
        for index,book in enumerate(self.books):
            if num1 == book.book_id:
                if num2 <= 0:
                    print('还书数量需要大于0')
                    return
                else:
                    book.return_book(num2)
                found = True
                self.save_books()
                self.show_books()
        if not found:
            print('没找到')

    def search_books(self,keyword):
        found = False
        for index,book in enumerate(self.books):
            if keyword in book.show_info():
                found = True
                print(index,book.show_info())
        if not found:
            print('没有找到')


    def delete_books(self,num):
        for book in self.books:
            if num == book.book_id:

                self.books.remove(book)
                self.save_books()
                print(f'已删除《{book.name}》')
                return

        print('没找到该书')


    def change_name(self,num,new_name):
        for book in self.books:
            if num == book.book_id:
                book.name = new_name
                self.save_books()
                return

    def change_author(self,num,new_author):
        for book in self.books:
            if num == book.book_id:
                book.author = new_author
                self.save_books()
                return

    def change_book_id(self,num,new_book_id):
        for book in self.books:
            if num == book.book_id:
                book.id = new_book_id
                self.save_books()
                return

    def change_price(self,num,new_price):
        for book in self.books:
            if num == book.book_id:
                book.price = new_price
                self.save_books()
                return

    def change_count(self,num,new_count):
        for book in self.books:
            if num == book.book_id:
                book.count = new_count
                self.save_books()
                return