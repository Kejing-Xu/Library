def find_book(cursor, bno):
    find_book_sql = 'select * from book where bno="%s"' % bno
    try:
        cursor.execute(find_book_sql)
        find = cursor.fetchone()
        if find is None:
            print("查无此书！")
        print("书籍号：",find[0],"\n类别：",find[1],"\n书名：",find[2],"\n出版社：",find[3],"\n出版年份：",find[4],
              "\n作者：",find[5],"\n价格：",find[6],"\n库藏：",find[7],"\n")
    except:
        print("查找失败！")
        return


def show_all_books(cursor):
    show_all_books_sql = 'select * from book'
    try:
        cursor.execute(show_all_books_sql)
        flag=0
        while True:
            row = cursor.fetchone()
            flag=1
            if not row:
                break
            print("书籍号：", row[0], "\n类别：", row[1], "\n书名：", row[2], "\n出版社：", row[3], "\n出版年份：", row[4],
                  "\n作者：", row[5], "\n价格：", row[6], "\n库藏：", row[7], "\n")
        if flag==0:
            print("图书馆无库藏书籍")
    except:
        print("出现了一些小错误")
        return

