import pymysql


class AdminClass():
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password='471225ABCD',
                                    database='library')
        self.cursor = self.conn.cursor()

    def add_newbook(self):
        choose=int(input("请问您要进行的操作是：\n1、单本入库\t\t2、批量入库\n"))
        if choose!=1 and choose!=2:
            print("无效输入")
        elif choose==1:
            book_num = 0
            new_bno = input("请输入新书的图书编号：")
            new_category = input("请输入新书的图书类别：")
            new_title = input("请输入新书的标题：")
            new_press = input("请输入新书的出版社：")
            new_year = input("请输入新书的出版年份：")
            new_author = input("请输入新书的作者：")
            new_price = input("请输入新书的价格：")
            try:
                sql_search = 'select stock from book where bno="%s"' % new_bno
                self.cursor.execute(sql_search)
                book_num = self.cursor.fetchone()
                if book_num is None:
                    new_stock = 1
                    sql_add_book = 'insert into book values("%s","%s","%s","%s",%s,"%s",%s,%d) ' % (
                    new_bno, new_category, new_title, new_press, new_year, new_author, new_price, new_stock)
                else:
                    new_stock = int(book_num[0]) + 1
                    sql_add_book = 'update book set stock=%d where bno="%s"' % (new_stock, new_bno)
                self.cursor.execute(sql_add_book)
                self.conn.commit()
                print("添加书籍成功，感谢使用图书管理系统")
            except:
                print("啊哦，出错了哦")
                return
        elif choose==2:
            print("请输入你要入库的书，每条图书信息放在一行，一行中的内容如下：")
            print("(书号，类别，标题，出版社，出版年份，作者，价格，数量)")
            while True:
                line_book=input()
                if line_book=='':
                    break
                sql_many='insert into book values %s' %line_book
                try:
                    self.cursor.execute(sql_many)
                    self.conn.commit()
                except:
                    print("啊哦，出错了哦")
            print("添加成功，感谢使用图书管理系统")

    def add_card(self):
        new_cid = input("请输入新借书证ID：")
        new_cname = input("请输入姓名：")
        new_cdepartment = input("请输入部门：")
        new_ctype = input("请输入身份信息：\n1:本科生\t\t2:研究生\t\t3：教师\t\t4:其他\n")
        new_cpassword = input("请输入初始密码：")
        try:
            sql_add_card = 'insert into card values("%s","%s","%s",%s,"%s",3) ' % (
                new_cid, new_cname, new_cdepartment, new_ctype, new_cpassword)
            self.cursor.execute(sql_add_card)
            self.conn.commit()
            print("添加借书证成功，感谢使用图书管理系统")
        except:
            print("输入错误！")
            return

    def delete_book(self):
        delete_bno = input("请输入要删除的书籍号：")
        try:
            sql_search_book = 'select stock from book where bno="%s"' % delete_bno
            self.cursor.execute(sql_search_book)
            get_num_delete = self.cursor.fetchone()
            if len(get_num_delete) == 0:
                print("无此书库藏")
                return
            elif get_num_delete[0] > 1:
                new_num = get_num_delete[0] - 1
                sql_delete_book = 'update book set stock=%d where bno="%s"' % (new_num, delete_bno)
            else:
                sql_delete_book = 'delete from book where bno="%s"' % delete_bno
            self.cursor.execute(sql_delete_book)
            self.conn.commit()
            print("删除成功，感谢使用图书管理系统")
        except:
            print("删除失败")
            return

    def delete_card(self):
        delete_cid = input("请输入要删除的卡号：")
        try:
            sql_delete_card = 'delete from card where cno="%s" ' % delete_cid
            self.cursor.execute(sql_delete_card)
            self.conn.commit()
            print("删除借书证成功，感谢使用图书管理系统")
        except:
            print("删除错误")
            return


