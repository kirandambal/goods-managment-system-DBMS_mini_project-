from tkinter import*
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from managestaff import *
from managegoods import *
from buygoods import *
from sellgoods import *


def adminpage():
    global root
    root=Tk()
    root.title("Admin Window")
    root.geometry("1350x700+0+0")
    root.maxsize(width=1350,height=700)
    root.config(bg='Navajo white')

    #-------Headings-------
    main_title=Label(root,text="ADMIN PAGE FOR WHOLESALE GOODS MANAGEMENT",font=("times new roman",25,"bold"),bg="green",fg="white").place(x=0,y=0,width=1350)
   

    #-----log out Button-----
    logout_btn=Button(root,text="LOG OUT",font=("times new roman",20,"bold"),command=root.destroy,bd=3,bg="purple",fg="white",cursor="hand2")
    logout_btn.place(x=1100,y=80,width=150,height=50)

    #-------buttons--------
    staffmng_btn=Button(root,text="MANAGE STAFF",font=("times new roman",20,"bold"),command=mngstaff_func,bd=3,bg="orange",fg="white",cursor="hand2")
    staffmng_btn.place(x=470,y=150,width=450,height=40)

    medmng_btn=Button(root,text="MANAGE GOODS",font=("times new roman",20,"bold"),command=mngmed_func,bd=3,bg="blue",fg="white",cursor="hand2")
    medmng_btn.place(x=470,y=200,width=450,height=40)

    sell_btn=Button(root,text="BUY GOODS",font=("times new roman",20,"bold"),command=buymed_func,bd=3,bg="red",fg="white",cursor="hand2")
    sell_btn.place(x=470,y=250,width=450,height=40)

    transaction_btn=Button(root,text="SELL GOODS",font=("times new roman",20,"bold"),command=sellmed_func,bd=3,bg="brown",fg="white",cursor="hand2")
    transaction_btn.place(x=470,y=300,width=450,height=40)
    root.mainloop()


def mngstaff_func():
    managestaff()

def mngmed_func():
    managegoods()

def sellmed_func():
    Sellgoods()

def buymed_func():
    buygoods()


#adminpage()