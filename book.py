class Book:
    def __init__(self,name,author,price,book_id,count):
        self.name = name
        self.author = author
        self.price = price
        self.book_id = book_id
        self.count = count


    def borrow_book(self,num):
        if self.count >= num:
            self.count -= num
            return True
        else:
            return False

    def return_book(self,num):
        self.count += num


    def show_info(self):
        return (f"书名: {self.name}, 作者: {self.author}, 价格: {self.price}, 书编号: {self.book_id},剩余书量: {self.count}\n"
                f"状态:{'已借出' if self.count == 0 else '可借'}")