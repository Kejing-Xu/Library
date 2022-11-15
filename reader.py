import datetime
import pymysql
import sys
import os


class ReaderClass():
    def __init__(self, cno):
        self.conn = pymysql.connect(host='localhost',
                                    user='root',
                                    password='471225ABCD',
                                    database='library')
        self.cursor = self.conn.cursor()
        self.cno = cno

    def get_reader_info(self):
        personal_info_sql = 'select * from card where cno="%s"' % self.cno
        try:
            self.cursor.execute(personal_info_sql)
            get_info = self.cursor.fetchone()
        except:
            print("信息获取失败")
            return
        if len(get_info) == 0:
            print("查无此人")
            return
        identity = ["0", "本科生", "研究生", "教师", "其它"]
        print("\n借书证号：", get_info[0], "\n姓名：", get_info[1], "\n部门：", get_info[2],
              "\n身份信息：", identity[get_info[3]], "\n信用值：", get_info[5])
        print("\n您已借的书有：")
        sql_search_borrow = 'select * from borrow where cno="%s"' % self.cno
        self.cursor.execute(sql_search_borrow)
        while True:
            row = self.cursor.fetchone()
            if not row:
                break
            print("书籍号：", row[0], "\n书名：", row[4], "\n借书时间：", row[2], "\n还书时间：", row[3], "\n")

    def change_personal_file(self):
        change = int(input("请问你要修改什么？\n1：姓名\t\t2:部门\t\t3：身份信息\t\t4：密码\n"))
        if change == 1:
            new_name = input("请输入你要修改为的姓名：")
            change_name_sql = 'update card set name="%s" where cno="%s"' % (new_name, self.cno)
            try:
                self.cursor.execute(change_name_sql)
                self.conn.commit()
                print("修改姓名成功，感谢使用图书管理系统")
            except:
                print("修改失败")
                return
        elif change == 2:
            new_department = input("请输入你要修改为的部门：")
            change_department_sql = 'update card set department="%s" where cno="%s"' % (new_department, self.cno)
            try:
                self.cursor.execute(change_department_sql)
                self.conn.commit()
                print("修改部门成功，感谢使用图书管理系统")
            except:
                print("修改失败")
                return
        elif change == 3:
            new_type = input("请输入你要修改为的身份信息\n1：本科生\t\t2：研究生\t\t3：教师\t\t4：其他\n")
            change_department_sql = 'update card set type="%s" where cno="%s"' % (new_type, self.cno)
            try:
                self.cursor.execute(change_department_sql)
                self.conn.commit()
                print("修改身份信息成功，感谢使用图书管理系统")
            except:
                print("修改失败")
                return
        elif change == 4:
            new_pw = '1'
            pw_again = '0'
            while new_pw != pw_again:
                new_pw = input("请输入你要修改为的密码：")
                pw_again = input("请确认您的密码：")
                if new_pw != pw_again:
                    print("输入不一致，请重新输入！")
            change_department_sql = 'update card set password="%s" where cno="%s"' % (new_pw, self.cno)
            try:
                self.cursor.execute(change_department_sql)
                self.conn.commit()
                print("修改密码成功，请重新登陆！")
                os.system("python sign_reader.py")
            except:
                print("修改失败")
                return
        else:
            print("输入信息无效！")
            return

    def borrow(self):
        sql_credit = 'select credit from card where cno="%s"' % self.cno
        self.cursor.execute(sql_credit)
        credit = self.cursor.fetchone()
        if credit[0] == 0:
            print("您已失信三次及以上，无法借书\n若想重新获得借书权利，可以向图书管理员申诉，或向图书馆公共邮箱 My_library@163.com 致信请求恢复")
            sys.exit(0)
        borrow_bno = input("请输入你要借的书的书籍号：")
        sql_find = 'select * from book where bno="%s"' % borrow_bno
        self.cursor.execute(sql_find)
        find = self.cursor.fetchall()
        if len(find) == 0:
            print("查无此书")
            return
        sql_search = 'select * from book where bno="%s"' % borrow_bno
        self.cursor.execute(sql_search)
        get_book = self.cursor.fetchone()
        if get_book[7] == 0:
            print("很抱歉，书籍已借出")
            return
        else:
            print("书籍的信息是：")
            print("书籍号：", get_book[0], "\n类别：", get_book[1], "\n书名：", get_book[2], "\n出版社：", get_book[3], "\n出版年份：",
                  get_book[4],
                  "\n作者：", get_book[5], "\n价格：", get_book[6], "\n库藏：", get_book[7], "\n")
            if_borrow = int(input("请问你确定要借阅吗\n1.确定\t\t2.返回\n"))
            if if_borrow == 2:
                return
            borrow_dt = datetime.datetime.now()
            return_dt = borrow_dt + datetime.timedelta(days=30)
            borrow_dt = borrow_dt.strftime("%Y-%m-%d %H:%M:%S")
            return_dt = return_dt.strftime("%Y-%m-%d %H:%M:%S")
            sql_name = 'select title from book where bno="%s"' % borrow_bno
            self.cursor.execute(sql_name)
            book_name = self.cursor.fetchone()
            try:
                sql_register = 'insert into borrow values ("%s","%s","%s","%s","%s")' % (
                    borrow_bno, self.cno, borrow_dt, return_dt, book_name[0])
                self.cursor.execute(sql_register)
                self.conn.commit()
                sql_borrow = 'update book set stock=%d where bno="%s"' % (get_book[7] - 1, borrow_bno)
                self.cursor.execute(sql_borrow)
                self.conn.commit()
                print("书籍已借出，借阅时间为30天，最迟还书时间为", return_dt, "\n感谢使用图书管理系统")
            except:
                print("啊哦，出错了哦")
                return

    def return_book(self):
        return_bno = input("请输入你将还的书的书籍号：")
        search_sql = 'select * from borrow where bno="%s" and cno="%s"' % (return_bno, self.cno)
        self.cursor.execute(search_sql)
        get_record = self.cursor.fetchone()
        if get_record is None:
            print("您未借此书")
            return
        sql_search_return = 'select * from book where bno="%s"' % return_bno
        self.cursor.execute(sql_search_return)
        get_book = self.cursor.fetchone()
        print("您要归还的书的信息是：")
        print("书籍号：", get_book[0], "\n类别：", get_book[1], "\n书名：", get_book[2], "\n出版社：", get_book[3], "\n出版年份：",
              get_book[4], "\n作者：", get_book[5], "\n价格：", get_book[6], "\n库藏：", get_book[7], "\n")
        if_prolong = int(input("请问你确定要归还吗\n1.确定\t\t2.返回\n"))
        if if_prolong == 2:
            return
        if datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") > get_record[3].strftime("%Y-%m-%d %H:%M:%S"):
            sql_get_credit = 'select credit from card where cno="%s"' % self.cno
            self.cursor.execute(sql_get_credit)
            get_credit = self.cursor.fetchone()
            sql_credit_minus = 'update card set credit=%d where cno="%s"' % self.cno
            self.cursor.execute(sql_credit_minus)
            self.conn.commit()
            print("还书超时，信用值减一，当失信三次及以上时自动取消还书资格")
        try:
            sql_num_return = 'select stock from book where bno="%s"' % return_bno
            self.cursor.execute(sql_num_return)
            get_num_return = self.cursor.fetchone()
            sql_return = 'update book set stock=%d where bno="%s"' % (get_num_return[0] + 1, return_bno)
            self.cursor.execute(sql_return)
            self.conn.commit()
            sql_delete_record = 'delete from borrow where bno="%s" and cno="%s" limit 1' % (return_bno, self.cno)
            self.cursor.execute(sql_delete_record)
            self.conn.commit()
            print("书籍已还，欢迎再次使用图书管理系统")
        except:
            print("啊哦，出了点小问题")

    def prolong_borrow(self):
        prolong_bno = input("请输入你将续借的书的书籍号：")
        search_sql = 'select * from borrow where bno="%s" and cno="%s"' % (prolong_bno, self.cno)
        self.cursor.execute(search_sql)
        get_record = self.cursor.fetchone()
        if get_record is None:
            print("您未借此书")
            return
        sql_search_prolong = 'select * from book where bno="%s"' % prolong_bno
        self.cursor.execute(sql_search_prolong)
        get_book = self.cursor.fetchone()
        print("您要续借的书的信息是：")
        print("书籍号：", get_book[0], "\n类别：", get_book[1], "\n书名：", get_book[2], "\n出版社：", get_book[3], "\n出版年份：",
              get_book[4], "\n作者：", get_book[5], "\n价格：", get_book[6], "\n库藏：", get_book[7], "\n")
        if_prolong = int(input("请问你确定要续借吗\n1.确定\t\t2.返回\n"))
        if if_prolong == 2:
            return
        new_return = datetime.datetime.now() + datetime.timedelta(days=30)
        new_return = new_return.strftime("%Y-%m-%d %H:%M:%S")
        sql_borrow = 'update borrow set return_date="%s" where bno="%s"' % (new_return, prolong_bno)
        self.cursor.execute(sql_borrow)
        self.conn.commit()
        print("书籍已续借，续借时间为30天，最迟还书时间为", new_return, "\n感谢使用图书管理系统")
