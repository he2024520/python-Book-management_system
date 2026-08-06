from manager import BookManager
from book import Book

manager = BookManager()
manager.load_books()

while True:
    print('\n====BookManager====\n')
    print('欢迎使用图书管理系统\n')
    print('输入你需要使用功能前的数字')
    print('1.增加书籍')
    print('2.展示图示信息')
    print('3.借书')
    print('4.还书')
    print('5.查询图书')
    print('6.退出')

    choice = input('输入你需要使用的功能')

    if choice == '1':
        name = input('输入书籍名称：\n')
        author = input('输入书籍作者：\n')
        price = int(input('输入书籍价格:\n'))
        book_id = int(input('输入书籍编号:\n'))
        count = int(input('输入这本书一共几本\n'))
        book = Book(name,author,price,book_id,count)
        manager.add_books(book)

    elif choice == '2':
        manager.show_books()

    elif choice == '3':
        try:
            num1 = int(input('输入你需要借书的编号\n'))
            num2 = int(input('输入你需要借阅几本，一次一人最多借阅五本'))
            manager.borrow_books(num1,num2)
        except ValueError:
            print('输入正确的数字')

    elif choice == '4':
        try:
            num1 = int(input('输入你需要还书的编号\n'))
            num2 = int(input('输入你需要还书的数量\n'))
            manager.return_books(num1,num2)
        except ValueError:
            print('输入正确的数字')

    elif choice == '5':
        key_words = input('输入你需要查找书的关键信息\n')
        manager.search_books(key_words)

    elif choice == '6':
        break



