from manager import BookManager
from book import Book

manager = BookManager()
manager.load_books()

while True:
    print('\n====BookManager====\n')
    print('欢迎使用图书管理系统\n')
    print('输入你需要使用功能前的数字')
    print('1.增加书籍')
    print('2.展示图书信息')
    print('3.借书')
    print('4.还书')
    print('5.查询图书')
    print('6.删除图书')
    print('7.修改图书信息')
    print('8.退出')

    choice = input('输入你需要使用的功能').strip()
    if choice == '':
        print('输入不能为空')
        continue

    if choice == '1':
        try:
            name = input('输入书籍名称：\n')
            author = input('输入书籍作者：\n')
            price = int(input('输入书籍价格:\n'))
            if price < 0:
                print('价格不能小于0')
                continue
            book_id = int(input('输入书籍编号:\n'))
            count = int(input('输入这本书一共几本\n'))
            if count < 0:
                print('数量不能小于0')
                continue
            book = Book(name,author,price,book_id,count)
            manager.add_books(book)
        except ValueError:
            print('输入正确的数字')

    elif choice == '2':
        manager.show_books()

    elif choice == '3':
        try:
            book_id = int(input('输入你需要借书的编号\n'))
            count = int(input('输入你需要借阅几本，一次一人最多借阅五本'))
            if count < 0:
                print('数量不能小于0')
                continue
            manager.borrow_books(book_id,count)
        except ValueError:
            print('输入正确的数字')

    elif choice == '4':
        try:
            book_id = int(input('输入你需要还书的编号\n'))
            count = int(input('输入你需要还书的数量\n'))
            if count < 0:
                print('数量不能小于0')
                continue
            manager.return_books(book_id,count)
        except ValueError:
            print('输入正确的数字')

    elif choice == '5':
        key_words = input('输入你需要查找书的关键信息\n')
        if key_words == '':
            print('输入不能为空')
            continue
        else:
            manager.search_books(key_words)

    elif choice == '6':
        try:
            book_id = int(input('输入需要删除的图书id\n'))
            manager.delete_books(book_id)
        except ValueError:
            print('输入正确的数字')

    elif choice == '7':
        try:
            print('1.修改图书书名')
            print('2.修改图书作者')
            print('3.修改图书id')
            print('4.修改图书价格')
            print('5.修改图书数量')
            book_id = int(input('输入你需要修改图书信息的id\n'))
            change_type = int(input('输入你需要修改的编号'))
            if change_type == 1:
                new_name = input('输入新的书名\n')
                manager.change_name(book_id,new_name)
            elif change_type == 2:
                new_author = input('输入新的作者\n')
                manager.change_author(book_id,new_author)
            elif change_type == 3:
                new_book_id = int(input('输入书的id\n'))
                manager.change_book_id(book_id,new_book_id)
            elif change_type == 4:
                new_price = int(input('输入书的价格\n'))
                if new_price < 0:
                    print('价格不能小于0')
                    continue
                manager.change_price(book_id,new_price)
            elif change_type == 5:
                new_count = int(input('输入书的数量\n'))
                if new_count < 0:
                    print('数量不能小于0')
                    continue
                manager.change_count(book_id,new_count)
            else:
                print('数字不在范围')
        except ValueError:
            print('输入正确的数字')
        
    elif choice == '8':
        print('退出成功')
        break

    else:
        print('数字不在范围')     