from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
import sqlite3



def buyitem():
    if  entry1.get()==""  or entry2.get()=="" or entry3.get()=="" or entry4.get()==""  or entry5.get()=="" or entry6.get()=="":
        messagebox.showerror("ERROR","All Fields Are Required")
        root.destroy()
    else:
        try:
            con=sqlite3.connect("goods.sqlite")
            cur=con.cursor()
            cur.execute('''SELECT * FROM GOODS WHERE ID=? AND NAME=? ''',(entry1.get(),entry2.get()))
            row=cur.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("ERROR","Product Not Registered In This System,Register First in ManageGoods or Invalid Good Name or ID")
                root.destroy()
            else:
                cur.execute('''CREATE TRIGGER IF NOT EXISTS ADDQUANTITY AFTER INSERT ON BUYGOODS FOR EACH ROW BEGIN UPDATE GOODS SET QUANTITY=QUANTITY+new.BUYQUANTITY WHERE ID=new.PRODUCT_ID ; END''')
                cur.execute('''INSERT INTO BUYGOODS (PRODUCT_ID,PRODUCT_NAME,BUYFROM,CONTACT,BUYDATE,BUYQUANTITY) VALUES (?,?,?,?,?,?)''',(entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get()))
                con.commit()
                con.close()
                fetch_data()
                messagebox.showinfo("Success","Product Brought Successfully")
                root.destroy()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to:{str(es)}")
            root.destroy()

def deleteitem():
    if  entry1.get()==""  or entry2.get()=="" or entry3.get()=="" or entry4.get()==""  or entry5.get()=="" or entry6.get()=="":
        messagebox.showerror("ERROR","All Fields Are Required")
        root.destroy()
    else:
        try:
            con=sqlite3.connect("goods.sqlite")
            cur=con.cursor()
            cur.execute('''SELECT * FROM GOODS WHERE ID=? AND NAME=? ''',(entry1.get(),entry2.get()))
            row=cur.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("ERROR","Product Not Registered In This System,Register First in ManageGoods or Invalid Product Name or ID")
                root.destroy()
            else:
                cur.execute('''SELECT * FROM BUYGOODS WHERE PRODUCT_ID=? AND PRODUCT_NAME=? ''',(entry1.get(),entry2.get()))
                row=cur.fetchone()
                #print(row)
                cur.execute('''DELETE FROM BUYGOODS WHERE TRANSACTIONID=?''',((row[0]),))
                cur.execute('''UPDATE GOODS SET QUANTITY=QUANTITY-? WHERE ID=?''',(entry6.get(),entry1.get()))
                
                con.commit()
                con.close()
                fetch_data()
                messagebox.showinfo("Success","DELETED Successfully")
                root.destroy()
        except Exception as es:
            messagebox.showerror("Error",f"Error due to:{str(es)}")
            root.destroy()


    




    

def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0,END)

def search():
    try:
        con = sqlite3.connect('goods.sqlite')
        cur = con.cursor()
        cur.execute("SELECT * FROM BUYGOODS WHERE "+str(combo_search.get())+" LIKE '%"+str(txt1.get())+"%' ORDER BY TRANSACTIONID DESC" )
        rows=cur.fetchall()
        if len(rows)!=0:
            Buygoods_table.delete(*Buygoods_table.get_children())
            for row in rows:
                Buygoods_table.insert('',END,values=row)
                con.commit()
        con.close()
        clearsearch()
    except Exception as es:
        messagebox.showerror("Error",f"Error Due To:{str(es)}")
        clearsearch()

def fetch_data():
    conn = sqlite3.connect('goods.sqlite')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM BUYGOODS ORDER BY TRANSACTIONID DESC''')
    rows=cur.fetchall()
    if len(rows)!=0:
        Buygoods_table.delete(*Buygoods_table.get_children())
        for row in rows:
            Buygoods_table.insert('',END,values=row)
            conn.commit()
    conn.close()

def get_cursor(ev):                              
    curosor_row=Buygoods_table.focus()                      
    contents=Buygoods_table.item(curosor_row)   
    row=contents['values']
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry1.insert(0, (row[1]))
    entry2.insert(0, (row[2]))
    entry3.insert(0, (row[3]))
    entry4.insert(0, (row[4]))
    entry5.insert(0, (row[5]))
    entry6.insert(0, (row[6]))

def clearsearch():
    combo_search.current(0)
    txt1.delete(0,END)


def buygoods():
    global root,entry1,entry2,entry3,entry4,entry5,entry6,txt1,combo_search,Buygoods_table
    conn = sqlite3.connect('goods.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS BUYGOODS(TRANSACTIONID INTEGER PRIMARY KEY AUTOINCREMENT,PRODUCT_ID NUMBER,PRODUCT_NAME TEXT,BUYFROM TEXT,CONTACT NUMBER,BUYDATE TEXT,BUYQUANTITY NUMBER)''')
    conn.commit()
    conn.close()

    root = Tk()
    root.title("Buy Product Window")
    root.geometry("1300x700+0+0")
    root.configure(bg='grey')

    label0= Label(root,text="WHOLESALE GOODS MANAGEMENT SYSTEM ",bg="grey",fg="white",font=("Times", 30))
    label1=Label(root,text="Product ID",bg="crimson",relief="ridge",fg="white",font=("Times", 12),width=25)
    entry1=Entry(root , font=("Times", 12))
    label2=Label(root, text="Product NAME",bd="2",relief="ridge",height="1",bg="crimson",fg="white", font=("Times", 12),width=25)
    entry2= Entry(root, font=("Times", 12))
    label3=Label(root, text="BUYFROM",bd="2",relief="ridge",bg="crimson",fg="white", font=("Times", 12),width=25)
    entry3= Entry(root, font=("Times", 12))
    label4=Label(root, text="CONTACT",bd="2",relief="ridge",bg="crimson",fg="white", font=("Times", 12),width=25)
    entry4= Entry(root, font=("Times", 12))
    label5=Label(root, text="BUYDATE",bg="crimson",relief="ridge",fg="white", font=("Times", 12),width=25)
    entry5= DateEntry(root, font=("Times", 12),width=18)
    label6=Label(root, text="Quantity",bd="2",relief="ridge",bg="crimson",fg="white", font=("Times", 12),width=25)
    entry6= Entry(root, font=("Times", 12))

    button1= Button(root, text="BUY ITEM", bg="white", fg="black", width=20, font=("Times", 12),command=buyitem)
    button2= Button(root, text="CLEAR SCREEN", bg="white", fg="black", width=20, font=("Times", 12),command=clearitem)
    button3= Button(root, text="DELETE BUYITEM", bg="white", fg="black", width=20, font=("Times", 12),command=deleteitem)

    label0.grid(columnspan=6, padx=10, pady=10)
    label1.grid(row=1,column=0, sticky=W, padx=10, pady=10)
    label2.grid(row=2,column=0, sticky=W, padx=10, pady=10)
    label3.grid(row=3,column=0, sticky=W, padx=10, pady=10)
    label4.grid(row=4,column=0, sticky=W, padx=10, pady=10)
    label5.grid(row=5,column=0, sticky=W, padx=10, pady=10)
    label6.grid(row=6,column=0, sticky=W, padx=10, pady=10)
    entry1.grid(row=1,column=1, padx=40, pady=10)
    entry2.grid(row=2,column=1, padx=10, pady=10)
    entry3.grid(row=3,column=1, padx=10, pady=10)
    entry4.grid(row=4,column=1, padx=10, pady=10)
    entry5.grid(row=5,column=1, padx=10, pady=10)
    entry6.grid(row=6,column=1, padx=10, pady=10)
    button1.grid(row=1,column=4, padx=40, pady=10)
    button2.grid(row=3,column=4, padx=40, pady=10)
    button3.grid(row=2,column=4, padx=40, pady=10)

    logout_btn=Button(root,text="QUIT",command=root.destroy,bg="brown",relief="ridge",fg="white",bd=3,font=("Times", 12),width=20,cursor="hand2").place(x=1100,y=25)

    #----------------------------Detail Frame-------------------
    detail_frame = Frame(root,bd=4,relief=RIDGE,bg="white")
    detail_frame.place(x=40,y=370,width=1220,height=330)

    lb1=Label(detail_frame,text="Search By",font=('times of roman',15,"bold"),bg="white",fg="BLACK").grid(row=0,column=1,padx=10,pady=10)
    combo_search=ttk.Combobox(detail_frame,width=10,font=('times of roman',15,"bold"),state="readonly")
    combo_search['values']=("","TRANSACTIONID","PRODUCT_ID","PRODUCT_NAME")
    combo_search.grid(row=0,column=2,padx=10,pady=10)
    combo_search.current(0)
    txt1=Entry(detail_frame,width=12,bd=3,relief=GROOVE,font=('times of roman',15,"bold"))
    txt1.grid(row=0,column=3,padx=10,pady=10)

    #-----------------------------Detail Frame Buttons---------------

    search_btn=Button(detail_frame,text='Serach',command=search,width=15,height=1).grid(row=0,column=5,padx=10,pady=10)
    showall_btn=Button(detail_frame,text='Show All',command=fetch_data,width=15,height=1).grid(row=0,column=6,padx=10,pady=10)

    #------------------------------Table Frame------------
    table_frame = Frame(detail_frame,bd=4,relief=RIDGE,bg="#3D3C3A")
    table_frame.place(x=10,y=50,width=1190,height=260)

    scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(table_frame,orient=VERTICAL)
    Buygoods_table=ttk.Treeview(table_frame,columns=("TRANSACTIONID","PRODUCT_ID","PRODUCT_NAME","BUYFROM","CONTACT","BUYDATE","BUYQUANTITY"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.configure(command=Buygoods_table.xview)
    scroll_y.configure(command=Buygoods_table.yview)
    Buygoods_table.heading("TRANSACTIONID",text="TRANSACTIONID")
    Buygoods_table.heading("PRODUCT_ID",text="PRODUCT_ID")
    Buygoods_table.heading("PRODUCT_NAME",text="PRODUCT_NAME")
    Buygoods_table.heading("BUYFROM",text="BUYFROM")
    Buygoods_table.heading("CONTACT",text="CONTACT")
    Buygoods_table.heading("BUYDATE",text="BUYDATE")
    Buygoods_table.heading("BUYQUANTITY",text="BUYQUANTITY")
    

    Buygoods_table['show']='headings'
    Buygoods_table.column("TRANSACTIONID",width=100)
    Buygoods_table.column("PRODUCT_ID",width=100)
    Buygoods_table.column("PRODUCT_NAME",width=100)
    Buygoods_table.column("BUYFROM",width=100)
    Buygoods_table.column("CONTACT",width=100)
    Buygoods_table.column("BUYDATE",width=100)
    Buygoods_table.column("BUYQUANTITY",width=100)
    Buygoods_table.pack(fill=BOTH,expand=1)
    Buygoods_table.bind("<ButtonRelease-1>",get_cursor)
    fetch_data()


    root.mainloop()

#buygoods()