from tkinter import *
from tkinter.ttk import *
import datetime

#get day
Date = datetime.datetime.now()
day = str(Date.day)
weekday = Date.strftime('%a')
month = str(Date.month)
year = str(Date.year)

#Create win
Restaurant = Tk()
Restaurant.geometry('500x500')
Restaurant.config(background='#ae79c7')
#Tạo nhãn có tên chính

mainLabel = Label(Restaurant, text='Restaurant Management System', foreground='blue', font=('Courier', 20, 'bold'), background='#ae79c7').pack()
timeLabel = Label(Restaurant, text=f"{weekday} {month} {day} {year}", foreground='blue', background='#ae79c7' ,font=('Courier', 10, 'bold')).pack()

#Tạo thông tin
order = StringVar()
fries = StringVar()
lunch = StringVar()
burger = StringVar()
pizza = StringVar()
cheese = StringVar()
drinks = StringVar()
total = StringVar()
order_Label = Label(Restaurant, text='Order No.', foreground='blue', font=('Courier', 10, 'bold'), background='#ae79c7').place(x='50', y='100')
order_Entry = Entry(Restaurant, textvariable=order).place(x='150', y='100')
fries_Label = Label(Restaurant, text='Fries Meal', foreground='blue', font=('Courier', 10, 'bold'), background='#ae79c7').place(x='50', y='130')
fries_Entry = Entry(Restaurant, textvariable=fries).place(x='150', y='130')
lunch_Label = Label(Restaurant, text='Lunch Meal', foreground='blue', background='#ae79c7', font=('Courier', 10, 'bold')).place(x='50', y='160')
lunch_Entry = Entry(Restaurant, textvariable=lunch).place(x='150', y='160')
Burger_Label = Label(Restaurant, text='Burger Meal', foreground='blue', font = ('Courier', 10, 'bold'), background='#ae79c7').place(x='50', y='190')
Burger_Entry = Entry(Restaurant, textvariable=burger).place(x='150', y='190')
pizaa_Label = Label(Restaurant, text='Pizza Meal', foreground='blue', font=('Courier', 10, 'bold'), background='#ae79c7').place(x='50', y='220')
pizza_Entry = Entry(Restaurant, textvariable=pizza).place(x='150', y='220')
chees_Label = Label(Restaurant, text='Cheese burger', foreground='blue', font=('Courier', 10, 'bold'), background='#ae79c7').place(x='40', y='250')
chees_Entry = Entry(Restaurant, textvariable=cheese).place(x='150', y='250')
drink_Label = Label(Restaurant, text='Drinks', foreground='blue', background='#ae79c7', font=('Courier', 10, 'bold')).place(x='50', y='280')
drink_Entry = Entry(Restaurant, textvariable=drinks).place(x='150', y='280')
total_Label = Label(Restaurant, text='Total', foreground='blue', background='#ae79c7', font=('Courier', 10, 'bold')).place(x='50', y='310')
displayTotal = Label(Restaurant, text=total.get(), width=20).place(x='150', y='310')

#ADD STYLE

btnsty = Style()
btnsty.configure('TButton', font=('Arial', 10, 'bold'))

def Price():
    price = Tk()
    price.geometry('300x300')
    price.title('Price List')
    title = Label(price, text='ITEM', font=('ARIAL', 15, 'bold')).place(x='50', y='50')
    cost = Label(price, text='PRICE', font=('Arial', 15, 'bold')).place(x='200', y='50')
    friesprice = Label(price, text='Fries Meal', font=('Arial', 10, 'bold'), foreground='blue').place(x='50', y='80')
    friceCost = Label(price, text='25', font=('Arial', 10, 'bold'), foreground='blue').place(x='225', y='80')
    lunchprice = Label(price, text='Lunch Meal', font=('Arial', 10, 'bold'), foreground='blue').place(x='50', y='110')
    lunchCost = Label(price, text='40', font=('Arial', 10, 'bold'), foreground='blue').place(x='225', y='110')
    burgerprice = Label(price, text='Burger Meal', font=('Arial', 10, 'bold'), foreground='blue').place(x='50', y='140')
    burgerCost = Label(price, text='35', font=('Arial', 10, 'bold'), foreground='blue').place(x='225', y='140')
    pizzaprice = Label(price, text='Pizza Meal', font=('Arial', 10, 'bold'), foreground='blue').place(x='50', y='170')
    pizzaCost = Label(price, text='50', font=('Arial', 10, 'bold'), foreground='blue').place(x='225', y='170')
    cheeseprice = Label(price, text='Cheese Burger', font=('Arial', 10, 'bold'), foreground='blue').place(x='50', y='200')
    cheeseCost = Label(price, text='30', font=('Arial', 10, 'bold'), foreground='blue').place(x='225', y='200')
    drinksprice = Label(price, text='Drinks', font=('Arial', 10, 'bold'), foreground='blue').place(x='50', y='230')
    drinkCost = Label(price, text='35', font=('Arial', 10, 'bold'), foreground='blue').place(x='225', y='230')

def Exit():
    Restaurant.destroy()


def Reset():
    order.set("")
    fries.set("")
    lunch.set("")
    burger.set("")
    pizza.set("")
    cheese.set("")
    drinks.set("")
    total.set("")
    displayTotal = Label(Restaurant, text="", width=20).place(x='150', y='310')

def Total():
    fries_Cost = 25
    get_fries = fries.get()
    lunch_Cost = 40
    get_lunch = lunch.get()
    burger_Cost = 35
    get_burger = burger.get()
    pizza_Cost = 50
    get_pizza = pizza.get()
    cheese_Cost = 30
    get_cheese = cheese.get()
    drinks_Cost = 35
    get_drinks = drinks.get()
    Total_price =int(get_drinks)*drinks_Cost + int(get_fries)*fries_Cost + int(get_lunch)*lunch_Cost + int(get_burger)*burger_Cost + int(get_pizza)*pizza_Cost + int(get_cheese)*cheese_Cost
    displayTotal = Label(Restaurant, text=str(Total_price), width=20).place(x='150', y='310')
    print(Total_price)



# print(weekday)
pricebtn = Button(Restaurant, text='Price',command=Price).place(x='50', y='340')
totalbtn = Button(Restaurant, text='Total', command=Total).place(x='150', y='340')
resetbtn = Button(Restaurant, text='Reset', command=Reset).place(x='250', y='340')
exitbtn = Button(Restaurant, text='Exit', command=Exit).place(x='350', y='340')
# print(day)
mainloop()