import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


def sql_connect():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        db="dbmsproject"
    )


class BookStoreManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Store Management System")
        self.root.geometry("1550x900+0+0")  # Dimensions of the GUI

        # Connect to MySQL
        self.con = sql_connect()
        if self.con is None:
            return

        # Creating the customisation of the title block
        lbltitle = Label(self.root, text="Book Store Management System", bg="light blue", fg="grey", bd=20,
                         relief=RIDGE, font=("Times New Roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        # Inner Frame css
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="light blue")
        frame.place(x=0, y=130, width=1530, height=300)

        # ======================== Data Frame Left ============================#
        DataFrameLeft = LabelFrame(frame, text="Book Store Management System", bg="light blue", fg="grey", bd=12,
                                   relief=RIDGE, font=("Times New Roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=700, height=250)

        # Member Type DropDown
        # lblMember = Label(DataFrameLeft,font=("arial",12,"bold"),bg="light blue",text="Member Type",padx=2,pady=6)
        # lblMember.grid(row=0,column=0,sticky=W)

        # Dropdown options
        # comMember=ttk.Combobox(DataFrameLeft,text="Member Type",font=("arial",12,"bold"),width=27)
        # comMember["value"]=("Admin Staff","Student","Lecturer")
        # comMember.grid(row=0,column=1)

        self.custId = StringVar()
        Label(DataFrameLeft, bg="light blue", text="Cust. Id", font=("arial", 12, "bold"), padx=2).grid(row=0, column=0,
                                                                                                        sticky=W)
        # Entry Box
        Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.custId).grid(row=0, column=1)

        self.custFname = StringVar()
        Label(DataFrameLeft, font=("arial", 12, "bold"), text="Cust. FName", padx=2, pady=4, bg="light blue").grid(
            row=1, column=0, sticky=W)
        # Entry Box
        Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.custFname).grid(row=1, column=1)

        self.custLname = StringVar()
        Label(DataFrameLeft, font=("arial", 12, "bold"), text="Cust. LName", padx=2, pady=6, bg="light blue").grid(
            row=2, column=0, sticky=W)
        # Entry Box
        Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.custLname).grid(row=2, column=1)

        self.custAddr = StringVar()
        Label(DataFrameLeft, font=("arial", 12, "bold"), text="Cust. Addr", padx=2, pady=4, bg="light blue").grid(row=3,
                                                                                                                  column=0,
                                                                                                                  sticky=W)
        # Entry Box
        Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.custAddr).grid(row=3, column=1)

        self.custPhNo = StringVar()
        Label(DataFrameLeft, font=("arial", 12, "bold"), text="Cust. PhNo", padx=2, pady=6, bg="light blue").grid(row=4,
                                                                                                                  column=0,
                                                                                                                  sticky=W)
        # Entry Box
        Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.custPhNo).grid(row=4, column=1)

        self.bookIsbn = StringVar()
        Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book ISBN", padx=2, pady=4, bg="light blue").grid(row=5,
                                                                                                                 column=0,
                                                                                                                 sticky=W)
        # Entry Box
        Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.bookIsbn).grid(row=5, column=1)

        self.orderId = StringVar()
        Label(DataFrameLeft, font=("arial", 12, "bold"), text="Order Id", padx=2, pady=4, bg="light blue").grid(row=6,
                                                                                                                column=0,
                                                                                                                sticky=W)
        # Entry Box
        Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.orderId).grid(row=6, column=1)

        self.orderTtl = StringVar()
        Label(DataFrameLeft, font=("arial", 12, "bold"), text="Order Ttl", padx=2, pady=4, bg="light blue").grid(row=7,
                                                                                                                 column=0,
                                                                                                                 sticky=W)
        # Entry Box
        Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.orderTtl).grid(row=7, column=1)

        self.bookTitle = StringVar()
        Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Title", padx=2, pady=4, bg="light blue").grid(row=0,
                                                                                                                  column=2,
                                                                                                                  sticky=W)
        # Entry Box
        Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.bookTitle).grid(row=0, column=3)

        self.bookPrice = StringVar()
        Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Price", padx=2, pady=4, bg="light blue").grid(row=1,
                                                                                                                  column=2,
                                                                                                                  sticky=W)
        # Entry Box
        Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.bookPrice).grid(row=1, column=3)

        self.bookAuthor = StringVar()
        Label(DataFrameLeft, font=("arial", 12, "bold"), text="Book Author", padx=2, pady=4, bg="light blue").grid(
            row=2, column=2, sticky=W)
        # Entry Box
        Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.bookAuthor).grid(row=2, column=3)

        self.catId = StringVar()
        Label(DataFrameLeft, font=("arial", 12, "bold"), text="Cat. Id", padx=2, pady=4, bg="light blue").grid(row=3,
                                                                                                               column=2,
                                                                                                               sticky=W)
        # Entry Box
        Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.catId).grid(row=3, column=3)

        self.catName = StringVar()
        Label(DataFrameLeft, font=("arial", 12, "bold"), text="Cat. Name", padx=2, pady=4, bg="light blue").grid(row=4,
                                                                                                                 column=2,
                                                                                                                 sticky=W)
        # Entry Box
        Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.catName).grid(row=4, column=3)

        self.publLic = StringVar()
        Label(DataFrameLeft, font=("arial", 12, "bold"), text="Publ. Lic", padx=2, pady=4, bg="light blue").grid(row=5,
                                                                                                                 column=2,
                                                                                                                 sticky=W)
        # Entry Box
        Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.publLic).grid(row=5, column=3)

        self.pymtId = StringVar()
        Label(DataFrameLeft, font=("arial", 12, "bold"), text="Pymt. Id", padx=2, pady=4, bg="light blue").grid(row=6,
                                                                                                                column=2,
                                                                                                                sticky=W)
        # Entry Box
        Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.pymtId).grid(row=6, column=3)

        self.pymtAmt = StringVar()
        Label(DataFrameLeft, font=("arial", 12, "bold"), text="Pymt. Amt", padx=2, pady=4, bg="light blue").grid(row=7,
                                                                                                                 column=2,
                                                                                                                 sticky=W)
        # Entry Box
        Entry(DataFrameLeft, font=("arial", 13, "bold"), width=29, textvariable=self.pymtAmt).grid(row=7, column=3)

        # ====================data frame right=======================
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="light blue", fg="black", bd=12, relief=RIDGE,
                                    font=("arial", 12, "bold"), padx=20)
        DataFrameRight.place(x=700, y=5, width=700, height=250)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        self.listBox = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=90, height=14)
        self.listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=self.listBox.yview)

        # Books Name list

        # ============================== Buttons Frame ====================================#
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="light blue")
        Framebutton.place(x=0, y=430, width=1530, height=70)

        btnAddData = Button(Framebutton, text="Add Data", font=("arial", 12, "bold"), width=23, bg="Grey", fg="black",
                            command=self.addData)
        btnAddData.grid(row=0, column=0)

        btnAddData = Button(Framebutton, text="Update Data", font=("arial", 12, "bold"), width=23, bg="Grey",
                            fg="black", command=self.updateData)
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(Framebutton, text="Delete Data", font=("arial", 12, "bold"), width=23, bg="Grey",
                            fg="black", command=self.deleteData)
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(Framebutton, text="Reset", font=("arial", 12, "bold"), width=23, bg="Grey", fg="black",
                            command=self.resetData)
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(Framebutton, text="Exit", font=("arial", 12, "bold"), width=23, bg="Grey", fg="black",
                            command=self.root.destroy)
        btnAddData.grid(row=0, column=5)

        # ============================== Information Frame ================================#
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="light blue")
        FrameDetails.place(x=0, y=490, width=1530, height=310)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg="light blue")
        Table_frame.place(x=0, y=2, width=1350, height=250)

        # ScrollBar dim
        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)
        self.library_table_ = ttk.Treeview(Table_frame, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set,
                                           show='headings',
                                           columns=[
                                               "Cust. Id",
                                               "Cust. FName",
                                               "Cust. LName",
                                               "Cust. Addr",
                                               "Cust. PhNo",
                                               "Book ISBN",
                                               "Order Id",
                                               "Order Ttl",
                                               "Book Title",
                                               "Book Price",
                                               "Book Author",
                                               "Cat. Id",
                                               "Cat. Name",
                                               "Publ. Lic",
                                               "Pymt. Id",
                                               "Pymt. Amt"
                                           ])  # All Column Names

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        # scrollbar dim can be viewed after entering data
        xscroll.config(command=self.library_table_.xview)
        yscroll.config(command=self.library_table_.yview)

        self.library_table_.heading("Cust. Id", text="Cust. Id")
        self.library_table_.heading("Cust. FName", text="Cust. FName")
        self.library_table_.heading("Cust. LName", text="Cust. LName")
        self.library_table_.heading("Cust. Addr", text="Cust. Addr")
        self.library_table_.heading("Cust. PhNo", text="Cust. PhNo")
        self.library_table_.heading("Book ISBN", text="Book ISBN")
        self.library_table_.heading("Order Id", text="Order Id")
        self.library_table_.heading("Order Ttl", text="Order Ttl")
        self.library_table_.heading("Book Title", text="Book Title")
        self.library_table_.heading("Book Price", text="Book Price")
        self.library_table_.heading("Book Author", text="Book Author")
        self.library_table_.heading("Cat. Id", text="Cat. Id")
        self.library_table_.heading("Cat. Name", text="Cat. Name")
        self.library_table_.heading("Publ. Lic", text="Publ. Lic")
        self.library_table_.heading("Pymt. Id", text="Pymt. Id")
        self.library_table_.heading("Pymt. Amt", text="Pymt. Amt")

        self.library_table_["show"] = "headings"
        self.library_table_.pack(fill=BOTH, expand=1)

        self.populateTable()

        # self.library_table_.column("Member type",width=100)
        # do for remaining columns with same width

    def populateBookNames(self):
        self.listBox.delete(0, END)

        bookListBox = []
        cursor = self.con.cursor()
        cursor.execute("select title from Book;")
        for row in cursor.fetchall():
            bookListBox.append(row[0])
        for item in bookListBox:
            self.listBox.insert(END, item)

    def populateTable(self):
        for i in self.library_table_.get_children():
            self.library_table_.delete(i)

        rows = []

        # Customer.id, Customer.first_name, Customer.last_name, Customer.address, Customer.phone_no
        cursor = self.con.cursor()
        cursor.execute("select id, first_name, last_name, address, phone_no from Customer;")
        data = cursor.fetchall()
        for i, row in enumerate(data):
            if i < len(row):
                rows.append(["" for i in range(16)])
            for j, field in enumerate(row):
                rows[i][0 + j] = str(field)

        # Book.isbn, Book.title, Book.price, Book.author
        cursor = self.con.cursor()
        cursor.execute("select isbn, title, price, author from Book;")
        data = cursor.fetchall()
        for i, row in enumerate(data):
            if i < len(row):
                rows.append(["" for i in range(16)])
            for j, field in enumerate(row):
                rows[i][5 + j] = str(field)

        # _Order.id, _Order.total
        cursor = self.con.cursor()
        cursor.execute("select id, total from _Order;")
        data = cursor.fetchall()
        for i, row in enumerate(data):
            if i < len(row):
                rows.append(["" for i in range(16)])
            for j, field in enumerate(row):
                rows[i][9 + j] = str(field)

        # Category.id, Category.name
        cursor = self.con.cursor()
        cursor.execute("select id, name from Category;")
        data = cursor.fetchall()
        for i, row in enumerate(data):
            if i < len(row):
                rows.append(["" for i in range(16)])
            for j, field in enumerate(row):
                rows[i][11 + j] = str(field)

        # Publisher.license
        cursor = self.con.cursor()
        cursor.execute("select license from Publisher;")
        data = cursor.fetchall()
        for i, row in enumerate(data):
            if i < len(row):
                rows.append(["" for i in range(16)])
            for j, field in enumerate(row):
                rows[i][12 + j] = str(field)

        # Payment.id, Payment.amt
        cursor = self.con.cursor()
        cursor.execute("select id, amt from Payment;")
        data = cursor.fetchall()
        for i, row in enumerate(data):
            if i < len(row):
                rows.append(["" for i in range(16)])
            for j, field in enumerate(row):
                rows[i][14 + j] = str(field)

        for row in rows:
            self.library_table_.insert('', tkinter.END, values=row)

        self.populateBookNames()

    # Button event handlers
    def addData(self):
        try:
            # Customer
            custId = str(self.custId.get()).strip()
            custFname = str(self.custFname.get()).strip()
            custLname = str(self.custLname.get()).strip()
            custAddr = str(self.custAddr.get()).strip()
            custPhNo = str(self.custPhNo.get()).strip()
            if custId != "" and custFname != "" and custLname != "" and custAddr != "" and custPhNo != "":
                cursor = self.con.cursor()
                cursor.execute(
                    f"insert into Customer values ({custId}, '{custFname}', '{custLname}', '{custAddr}', {custPhNo});")
                self.con.commit()

            # Book
            bookIsbn = str(self.bookIsbn.get()).strip()
            bookTitle = str(self.bookTitle.get()).strip()
            bookPrice = str(self.bookPrice.get()).strip()
            bookAuthor = str(self.bookAuthor.get()).strip()
            if bookIsbn != "" and bookTitle != "" and bookPrice != "" and bookAuthor != "":
                cursor = self.con.cursor()
                cursor.execute(
                    f"insert into Book values ({bookIsbn}, '{bookTitle}', {bookPrice}, NULL, '{bookAuthor}');")
                self.con.commit()

            # Category
            catId = str(self.catId.get()).strip()
            catName = str(self.catName.get()).strip()
            if catId != "" and catName != "":
                cursor = self.con.cursor()
                cursor.execute(
                    f"insert into Category values ({catId}, '{catName}');")
                self.con.commit()

            # Payment
            pymtId = str(self.pymtId.get()).strip()
            pymtAmt = str(self.pymtAmt.get()).strip()
            if pymtId != "" and pymtAmt != "":
                cursor = self.con.cursor()
                cursor.execute(
                    f"insert into Payment values ({pymtId}, {pymtAmt}, NULL);")
                self.con.commit()

            # Publisher
            publLic = str(self.publLic.get()).strip()
            if publLic != "":
                cursor = self.con.cursor()
                cursor.execute(
                    f"insert into Publisher values ({publLic}, NULL, NULL, NULL);")
                self.con.commit()

            # Order
            orderId = str(self.orderId.get()).strip()
            orderTtl = str(self.orderTtl.get()).strip()
            if orderId != "" and orderTtl != "":
                cursor = self.con.cursor()
                cursor.execute(
                    f"insert into _Order values ({orderId}, NULL, {orderTtl});")
                self.con.commit()

            self.populateTable()
        except Exception as e:
            messagebox.showerror("Cannot execute query")

    def updateData(self):
        try:
            # Customer
            custId = str(self.custId.get()).strip()
            custFname = str(self.custFname.get()).strip()
            custLname = str(self.custLname.get()).strip()
            custAddr = str(self.custAddr.get()).strip()
            custPhNo = str(self.custPhNo.get()).strip()
            if custId != "" and custFname != "" and custLname != "" and custAddr != "" and custPhNo != "":
                cursor = self.con.cursor()
                cursor.execute(
                    f"update Customer set first_name='{custFname}', last_name='{custLname}', address='{custAddr}', phone_no={custPhNo} where id={custId};")
                self.con.commit()

            # Book
            bookIsbn = str(self.bookIsbn.get()).strip()
            bookTitle = str(self.bookTitle.get()).strip()
            bookPrice = str(self.bookPrice.get()).strip()
            bookAuthor = str(self.bookAuthor.get()).strip()
            if bookIsbn != "" and bookTitle != "" and bookPrice != "" and bookAuthor != "":
                cursor = self.con.cursor()
                cursor.execute(
                    f"update Book set title='{bookTitle}', price={bookPrice}, author='{bookAuthor}' where isbn={bookIsbn};")
                self.con.commit()

            # Category
            catId = str(self.catId.get()).strip()
            catName = str(self.catName.get()).strip()
            if catId != "" and catName != "":
                cursor = self.con.cursor()
                cursor.execute(
                    f"update Category set name='{catName}' where id={catId};")
                self.con.commit()

            # Payment
            pymtId = str(self.pymtId.get()).strip()
            pymtAmt = str(self.pymtAmt.get()).strip()
            if pymtId != "" and pymtAmt != "":
                cursor = self.con.cursor()
                cursor.execute(
                    f"update Payment set amt={pymtAmt} where id={pymtId};")
                self.con.commit()

            # Order
            orderId = str(self.orderId.get()).strip()
            orderTtl = str(self.orderTtl.get()).strip()
            if orderId != "" and orderTtl != "":
                cursor = self.con.cursor()
                cursor.execute(
                    f"update _Order set total={orderTtl} where id={orderId};")
                self.con.commit()

            self.populateTable()
        except:
            messagebox.showerror("Cannot execute query")

    def deleteData(self):
        try:
            # Customer
            conditions = []
            custId = str(self.custId.get()).strip()
            custFname = str(self.custFname.get()).strip()
            custLname = str(self.custLname.get()).strip()
            custAddr = str(self.custAddr.get()).strip()
            custPhNo = str(self.custPhNo.get()).strip()

            if custId != "":
                conditions.append(f"id={custId}")
            if custFname != "":
                conditions.append(f"first_name='{custFname}'")
            if custLname != "":
                conditions.append(f"last_name='{custLname}'")
            if custAddr != "":
                conditions.append(f"address='{custAddr}'")
            if custPhNo != "":
                conditions.append(f"phone_no={custPhNo}")

            if len(conditions) > 0:
                cursor = self.con.cursor()
                cursor.execute(
                    f"delete from Customer where {' and '.join(conditions)};")
                self.con.commit()

            # Book
            conditions = []
            bookIsbn = str(self.bookIsbn.get()).strip()
            bookTitle = str(self.bookTitle.get()).strip()
            bookPrice = str(self.bookPrice.get()).strip()
            bookAuthor = str(self.bookAuthor.get()).strip()

            if bookIsbn != "":
                conditions.append(f"isbn={bookIsbn}")
            if bookTitle != "":
                conditions.append(f"title='{bookTitle}'")
            if bookPrice != "":
                conditions.append(f"price={bookPrice}")
            if bookAuthor != "":
                conditions.append(f"author='{bookAuthor}'")

            if len(conditions) > 0:
                cursor = self.con.cursor()
                cursor.execute(
                    f"delete from Book where {' and '.join(conditions)};")
                self.con.commit()

            # Category
            conditions = []
            catId = str(self.catId.get()).strip()
            catName = str(self.catName.get()).strip()

            if catId != "":
                conditions.append(f"id={catId}")
            if catName != "":
                conditions.append(f"name='{catName}'")

            if len(conditions) > 0:
                cursor = self.con.cursor()
                cursor.execute(
                    f"delete from Category where {' and '.join(conditions)};")
                self.con.commit()

            # Payment
            conditions = []
            pymtId = str(self.pymtId.get()).strip()
            pymtAmt = str(self.pymtAmt.get()).strip()

            if pymtId != "":
                conditions.append(f"id={pymtId}")
            if pymtAmt != "":
                conditions.append(f"amt={pymtAmt}")

            if len(conditions) > 0:
                cursor = self.con.cursor()
                cursor.execute(
                    f"delete from Payment where {' and '.join(conditions)};")
                self.con.commit()

            # Publisher
            conditions = []
            publLic = str(self.publLic.get()).strip()

            if publLic != "":
                conditions.append(f"license={publLic}")

            if len(conditions) > 0:
                cursor = self.con.cursor()
                cursor.execute(
                    f"delete from Publisher where {' and '.join(conditions)};")
                self.con.commit()

            # Order
            conditions = []
            orderId = str(self.orderId.get()).strip()
            orderTtl = str(self.orderTtl.get()).strip()

            if orderId != "":
                conditions.append(f"id={orderId}")
            if orderTtl != "":
                conditions.append(f"total={orderTtl}")

            if len(conditions) > 0:
                cursor = self.con.cursor()
                cursor.execute(
                    f"delete from _Order where {' and '.join(conditions)};")
                self.con.commit()

            self.populateTable()
        except:
            messagebox.showerror("Cannot execute query")

    def resetData(self):
        fields = [
            self.custId,
            self.custFname,
            self.custLname,
            self.custAddr,
            self.custPhNo,
            self.bookIsbn,
            self.bookTitle,
            self.bookPrice,
            self.bookAuthor,
            self.orderId,
            self.orderTtl,
            self.catId,
            self.catName,
            self.publLic,
            self.pymtId,
            self.pymtAmt
        ]
        for field in fields:
            field.set("")


if __name__ == "__main__":
    root = Tk()
    obj = BookStoreManagementSystem(root)
    root.mainloop()
