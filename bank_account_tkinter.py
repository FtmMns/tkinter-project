from tkinter import *
import pandas as pd
import openpyxl
import xlsxwriter
import bankacount
exel_data = pd.read_excel("C:\\Users\\PC\\Desktop\\Users.xlsx")
file_path = ("C:\\Users\\PC\\Desktop\\Users.xlsx")
user_i_logged = None
update_balance = 0
def login_func():
    global user_i_logged
    for i in range(len(exel_data)):
      if str(username_Entry.get())==str(exel_data["username"][i]) and str(password_Entry.get())==str(exel_data["password"][i]):
          welcome_label.config(text=f"welcome dear {exel_data['firstname'][i]}")
          user_i_logged = i
          balance_Entry.config(state="normal")

          balance_Entry.insert(END,str(exel_data["balance"][user_i_logged]))

          varizi_button.config(state="normal")

          varizi_Entry.config(state="normal")
          bardasht_Entry.config(state="normal")
          bardasht_button.config(state="normal")
          username_Entry.config(state="disabled")
          password_Entry.config(state="disabled")
          login_button.config(state="disabled")

          break
      else:
        welcome_label.config(text="username or password is incorecct")
def varizi_func():
   global update_balance
   balance_Entry.delete(0,END)
   balance_after_variz = float(exel_data["balance"][user_i_logged])+float(varizi_Entry.get())
   exel_data["balance"][user_i_logged] = balance_after_variz
   balance_Entry.insert(END,balance_after_variz)
   varizi_Entry.delete(0,END)
   welcome_label.config(text = "variz ba movafaghiyat anjam shod", bg = "light green", justify = "center")
   update_balance = balance_after_variz
   update_excel()

def bardasht_func():
    global bardasht_is_valied
    global update_balance
    if float(bardasht_Entry.get()) <= float(exel_data["balance"][user_i_logged]):
        balance_after_bardasht = float(exel_data["balance"][user_i_logged])-float(bardasht_Entry.get())
        exel_data["balance"][user_i_logged] =  balance_after_bardasht
        bardasht_is_valied = True
        if bardasht_is_valied == True:
         welcome_label.config(text="bardasht ba movafaghiat anjam shod",bg="light green",justify="center")
         balance_Entry.delete(0,END)
         balance_Entry.insert(END,balance_after_bardasht)
         update_balance=balance_after_bardasht
         bardasht_Entry.delete(0,END)
         update_excel()
    else:
        bardasht_button.config(state="disabled")
        welcome_label.config(text="low balance",bg="red",justify="center")
        bardasht_is_valied = False

    bardasht_button.config(state="normal", text="bardasht")
    bardasht_Entry.delete(0,END)
def update_excel():
    exel_data.at[user_i_logged,"balance"]=update_balance
    exel_data.to_excel(file_path,index=False)



window = Tk()
window.title("bank acount")
window.geometry("350x300+20+20")

usename_label = Label(window,text="user name")
usename_label.place(x=30,y=14)
username_Entry = Entry(window,bd=2,bg="powder blue",width=12,justify="left")
username_Entry.place(x=30,y=35)


password_label = Label(window,text="pass word")
password_label.place(x=118,y=14)
password_Entry = Entry(window,bd=2,bg="powder blue",width=12,justify="left",show="*")
password_Entry.place(x=118,y=35)

login_button = Button(window,text="Login",width=10,command=login_func)
login_button.place(x=217,y=28)

welcome_label = Label(window,text="",justify="left",font=("bold"))
welcome_label.place(x=20,y=70)

balance_label = Label(window,text="balance")
balance_label.place(x=50,y=120)
balance_Entry = Entry(window,bd=2,width=25,justify="left",state="disabled")
balance_Entry.place(x=50,y=140)

varizi_Entry = Entry(window,bd=2,width=15,justify="left",state="disabled")
varizi_Entry.place(x=50,y=180)
varizi_button = Button(window,text="variz",width=8,bd=2,state="disabled",command = varizi_func)
varizi_button.place(x=155,y=180)

bardasht_Entry = Entry(window,bd=2,width=15,justify="left",state="disabled")
bardasht_Entry.place(x=50,y=220)
bardasht_button = Button(window,text="bardasht",width=8,bd=2,state="disabled",command = bardasht_func)
bardasht_button.place(x=155,y=220)


window.mainloop()
