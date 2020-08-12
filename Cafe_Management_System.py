from tkinter import *
import time
import datetime
import tkinter.messagebox
import random


root = Tk()
root.geometry('1350x750+0+0')
root.title('Restaurant Management System')
root.config(bg='Cadet Blue')


Tops = Frame(root,bg='Cadet Blue',bd=20,pady=5,relief='ridge')
Tops.pack(side=TOP)

lblTitle = Label(Tops,font=('Arial',60,'bold'),text='Restaurant Management System',bd=21,bg='Cadet Blue',fg='Cornsilk',justify=CENTER)
lblTitle.grid(row=0,column=0)

ReceiptCal_F = Frame(root,bg='Powder Blue',bd=10,relief='ridge')
ReceiptCal_F.pack(side=RIGHT)

Buttons_F = Frame(ReceiptCal_F,bg='Powder Blue',bd=3,relief='ridge')
Buttons_F.pack(side=BOTTOM)

Cal_F = Frame(ReceiptCal_F,bg='powder blue',bd=6,relief='ridge')
Cal_F.pack(side=TOP)

Receipt_F = Frame(ReceiptCal_F,bg='powder blue',bd=4,relief='ridge')
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root,bg='Cadet Blue',bd=10,relief='ridge')
MenuFrame.pack(side=TOP)

Cost_F = Frame(MenuFrame,bg='powder blue',bd=4)
Cost_F.pack(side=BOTTOM)

Drinks_F = Frame(MenuFrame,bg='cadet blue',bd=10)
Drinks_F.pack(side=TOP)

Drinks_F = Frame(MenuFrame,bg='powder blue',bd=10,relief=RIDGE)
Drinks_F.pack(side='left')

Cake_F = Frame(MenuFrame,bg='powder blue',bd=10,relief='ridge')
Cake_F.pack(side=RIGHT)

var1 = IntVar()
var2= IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateOfOrder = StringVar()
Receipt_Ref = StringVar()
GST = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostOfCakes = StringVar()
CostOfDrinks = StringVar()
ServiceCharge = StringVar()


E_Latte = StringVar()
E_Espresso = StringVar()
E_Iced_Latte = StringVar()
E_Vale_Coffee = StringVar()
E_Cappuccino = StringVar()
E_African_Coffee = StringVar()
E_American_Coffee = StringVar()
E_Iced_Cappuccino = StringVar()

E_Latte.set('0')
E_Espresso.set('0')
E_Iced_Latte.set('0')
E_Vale_Coffee.set('0')
E_Cappuccino.set('0')
E_African_Coffee.set('0')
E_American_Coffee.set('0')
E_Iced_Cappuccino.set('0')

E_SchoolCake = StringVar()
E_Sunny_AO_Cake = StringVar()
E_Jonathan_YO_Cake = StringVar()
E_West_African_Cake = StringVar()
E_Lagos_Chocolate_Cake = StringVar()
E_Kilburn_Chocolate_Cake = StringVar()
E_Carlton_Hill_Cake = StringVar()
E_Queen_Park_Cake = StringVar()

E_SchoolCake.set('0')
E_Sunny_AO_Cake.set('0')
E_Jonathan_YO_Cake.set('0')
E_West_African_Cake.set('0')
E_Lagos_Chocolate_Cake.set('0')
E_Kilburn_Chocolate_Cake.set('0')
E_Carlton_Hill_Cake.set('0')
E_Queen_Park_Cake.set('0')

DateOfOrder.set(time.strftime('%d/%m/%Y'))


def chkLatte():
        if (var1.get() == 1):
                txtLatte.configure(state=NORMAL)
                txtLatte.focus()
                txtLatte.delete('0',END)
                E_Latte.set('')
        elif (var1.get() == 0):
                txtLatte.configure(state=DISABLED)
                E_Latte.set('0')

def chkEspresso():
        if (var2.get() == 1):
                txtEspresso.configure(state=NORMAL)
                txtEspresso.focus()
                txtEspresso.delete('0',END)
                E_Espresso.set('')
        elif (var2.get() == 0):
                txtEspresso.configure(state=DISABLED)
                E_Espresso.set('0')

def chkIced_Latte():
        if (var3.get() == 1):
                txtIced_Latte.configure(state=NORMAL)
                txtIced_Latte.focus()
                txtIced_Latte.delete('0',END)
                E_Iced_Latte.set('')
        elif (var3.get() == 0):
                txtIced_Latte.configure(state=DISABLED)
                E_Iced_Latte.set('0')

def chkVale_Coffee():
        if (var4.get() == 1):
                txtVale_Coffee.configure(state=NORMAL)
                txtVale_Coffee.focus()
                txtVale_Coffee.delete('0',END)
                E_Vale_Coffee.set('')
        elif (var4.get() == 0):
                txtVale_Coffee.configure(state=DISABLED)
                E_Vale_Coffee.set('0')


def chkCappuccino():
        if (var5.get() == 1):
                txtCappuccino.configure(state=NORMAL)
                txtCappuccino.focus()
                txtCappuccino.delete('0',END)
                E_Cappuccino.set('')
        elif (var5.get() == 0):
                txtCappuccino.configure(state=DISABLED)
                E_Cappuccino.set('0')

def chkAfrican_Coffee():
        if (var6.get() == 1):
                txtAfrican_Coffee.configure(state=NORMAL)
                txtAfrican_Coffee.focus()
                txtAfrican_Coffee.delete('0',END)
                E_African_Coffee.set('')
        elif (var6.get() == 0):
                txtAfrican_Coffee.configure(state=DISABLED)
                E_African_Coffee.set('0')

def chkAmerican_Coffee():
        if (var7.get() == 1):
                txtAmerican_Coffee.configure(state=NORMAL)
                txtAmerican_Coffee.focus()
                txtAmerican_Coffee.delete('0',END)
                E_American_Coffee.set('')
        elif (var7.get() == 0):
                txtAmerican_Coffee.configure(state=DISABLED)
                E_American_Coffee.set('0')

def chkIced_Cappuccino():
        if (var8.get() == 1):
                txtIced_Cappuccino.configure(state=NORMAL)
                txtIced_Cappuccino.focus()
                txtIced_Cappuccino.delete('0',END)
                E_Iced_Cappuccino.set('')
        elif (var8.get() == 0):
                txtIced_Cappuccino.configure(state=DISABLED)
                E_Iced_Cappuccino.set('0')

def chkSchoolCake():
        if (var9.get() == 1):
                txtSchoolCake.configure(state=NORMAL)
                txtSchoolCake.focus()
                txtSchoolCake.delete('0',END)
                E_SchoolCake.set('')
        elif (var9.get() == 0):
                txtSchoolCake.configure(state=DISABLED)
                E_SchoolCake.set('0')

def chkSunny_AO_Cake():
        if (var10.get() == 1):
                txtSunny_AO_Cake.configure(state=NORMAL)
                txtSunny_AO_Cake.focus()
                txtSunny_AO_Cake.delete('0',END)
                E_Sunny_AO_Cake.set('')
        elif (var10.get() == 0):
                txtSunny_AO_Cake.configure(state=DISABLED)
                E_Sunny_AO_Cake.set('0')

def chkJonathan_YO_Cake():
        if (var11.get() == 1):
                txtJonathan_YO_Cake.configure(state=NORMAL)
                txtJonathan_YO_Cake.focus()
                txtJonathan_YO_Cake.delete('0',END)
                E_Jonathan_YO_Cake.set('')
        elif (var11.get() == 0):
                txtJonathan_YO_Cake.configure(state=DISABLED)
                E_Jonathan_YO_Cake.set('0')

def chkWest_African_Cake():
        if (var12.get() == 1):
                txtWest_African_Cake.configure(state=NORMAL)
                txtWest_African_Cake.focus()
                txtWest_African_Cake.delete('0',END)
                E_West_African_Cake.set('')
        elif (var12.get() == 0):
                txtWest_African_Cake.configure(state=DISABLED)
                E_West_African_Cake.set('0')

def chkLagos_Chocolate_Cake():
        if (var13.get() == 1):
                txtLagos_Chocolate_Cake.configure(state=NORMAL)
                txtLagos_Chocolate_Cake.focus()
                txtLagos_Chocolate_Cake.delete('0',END)
                E_Lagos_Chocolate_Cake.set('')
        elif (var13.get() == 0):
                txtLagos_Chocolate_Cake.configure(state=DISABLED)
                E_Lagos_Chocolate_Cake.set('0')

def chkKilburn_Chocolate_Cake():
        if (var14.get() == 1):
                txtKilburn_Chocolate_Cake.configure(state=NORMAL)
                txtKilburn_Chocolate_Cake.focus()
                txtKilburn_Chocolate_Cake.delete('0',END)
                E_Kilburn_Chocolate_Cake.set('')
        elif (var14.get() == 0):
                txtKilburn_Chocolate_Cake.configure(state=DISABLED)
                E_Kilburn_Chocolate_Cake.set('0')

def chkCarlton_Hill_Cake():
        if (var15.get() == 1):
                txtCarlton_Hill_Cake.configure(state=NORMAL)
                txtCarlton_Hill_Cake.focus()
                txtCarlton_Hill_Cake.delete('0',END)
                E_Carlton_Hill_Cake.set('')
        elif (var15.get() == 0):
                txtCarlton_Hill_Cake.configure(state=DISABLED)
                E_Carlton_Hill_Cake.set('0')

def chkQueen_Park_Cake():
        if (var16.get() == 1):
                txtQueen_Park_Cake.configure(state=NORMAL)
                txtQueen_Park_Cake.focus()
                txtQueen_Park_Cake.delete('0',END)
                E_Queen_Park_Cake.set('')
        elif (var16.get() == 0):
                txtQueen_Park_Cake.configure(state=DISABLED)
                E_Queen_Park_Cake.set('0')


def Receipt():
        global txtReceipt
        txtReceipt.delete('1.0',END)
        x = random.randint(1020300,9092399)
        randomRef = str(x)
        Receipt_Ref.set('BILL '+randomRef)

        txtReceipt.insert(END,'Receipt Ref:\t\t'+Receipt_Ref.get()+'\t\t   '+DateOfOrder.get()+'\n')
        txtReceipt.insert(END,'Item:\t\t\t\t'+'Cost of Items\n')
        txtReceipt.insert(END,'Latte:\t\t\t\t\t'+E_Latte.get()+'\n')
        txtReceipt.insert(END,'Espresso:\t\t\t\t\t'+E_Espresso.get()+'\n')
        txtReceipt.insert(END,'Iced Latte:\t\t\t\t\t'+E_Iced_Latte.get()+'\n')
        txtReceipt.insert(END,'Vale Coffee:\t\t\t\t\t'+E_Vale_Coffee.get()+'\n')
        txtReceipt.insert(END,'Cappuccino:\t\t\t\t\t'+E_Cappuccino.get()+'\n')
        txtReceipt.insert(END,'African Coffee:\t\t\t\t\t'+E_African_Coffee.get()+'\n')
        txtReceipt.insert(END,'American Coffee:\t\t\t\t\t'+E_American_Coffee.get()+'\n')
        txtReceipt.insert(END,'Iced Cappuccino:\t\t\t\t\t'+E_Iced_Cappuccino.get()+'\n')
        txtReceipt.insert(END,'School Cake:\t\t\t\t\t'+E_SchoolCake.get()+'\n')
        txtReceipt.insert(END,'Sunday O Cake:\t\t\t\t\t'+E_Sunny_AO_Cake.get()+'\n')
        txtReceipt.insert(END,'Jonathan O Cake:\t\t\t\t\t'+E_Jonathan_YO_Cake.get()+'\n')
        txtReceipt.insert(END,'West African Cake:\t\t\t\t\t'+E_West_African_Cake.get()+'\n')
        txtReceipt.insert(END,'Lagos Chocolate Cake:\t\t\t\t\t'+E_Lagos_Chocolate_Cake.get()+'\n')
        txtReceipt.insert(END,'Kilburn Chocolate Cake:\t\t\t\t\t'+E_Kilburn_Chocolate_Cake.get()+'\n')
        txtReceipt.insert(END,'Carlton Hill Chocolate Cake:\t\t\t\t\t'+E_Carlton_Hill_Cake.get()+'\n')
        txtReceipt.insert(END,'Queen Park Chocolate Cake:\t\t\t\t\t'+E_Queen_Park_Cake.get()+'\n')
        txtReceipt.insert(END,'Cost of Drinks:\t\t\t\t'+CostOfDrinks.get()+'\nGST:\t\t\t\t'+GST.get()+'\n')
        txtReceipt.insert(END,'Cost of Cakes:\t\t\t\t'+CostOfCakes.get()+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+'\n')
        txtReceipt.insert(END,'Service Charge:\t\t\t\t'+ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+'\n')
        txtReceipt.configure(state=DISABLED)


Latte = Checkbutton(Drinks_F,text='Latte',variable=var1,onvalue=1,offvalue=0,font=('Arial',18,'bold'),bg='powder blue',command=chkLatte).grid(row=0,sticky=W)
Espresso = Checkbutton(Drinks_F,text='Espresso',variable=var2,onvalue=1,offvalue=0,font=('Arial',18,'bold'),bg='powder blue',command=chkEspresso).grid(row=1,sticky=W)
Iced_Latte = Checkbutton(Drinks_F,text='Iced Latte',variable=var3,onvalue=1,offvalue=0,font=('Arial',18,'bold'),bg='powder blue',command=chkIced_Latte).grid(row=2,sticky=W)
Vale_Coffee = Checkbutton(Drinks_F,text='Vale Coffee',variable=var4,onvalue=1,offvalue=0,font=('Arial',18,'bold'),bg='powder blue',command=chkVale_Coffee).grid(row=3,sticky=W)
Cappuccino = Checkbutton(Drinks_F,text='Cappuccino',variable=var5,onvalue=1,offvalue=0,font=('Arial',18,'bold'),bg='powder blue',command=chkCappuccino).grid(row=4,sticky=W)
African_Coffee = Checkbutton(Drinks_F,text='African Coffee',variable=var6,onvalue=1,offvalue=0,font=('Arial',18,'bold'),bg='powder blue',command=chkAfrican_Coffee).grid(row=5,sticky=W)
American_Coffee = Checkbutton(Drinks_F,text='American Coffee',variable=var7,onvalue=1,offvalue=0,font=('Arial',18,'bold'),bg='powder blue',command=chkAmerican_Coffee).grid(row=6,sticky=W)
Iced_Cappuccino = Checkbutton(Drinks_F,text='Iced Cappuccino',variable=var8,onvalue=1,offvalue=0,font=('Arial',18,'bold'),bg='powder blue',command=chkIced_Cappuccino).grid(row=7,sticky=W)

txtLatte = Entry(Drinks_F,font=('Arial',16,'bold'),bd=8,width=6,justify='left',state='disabled',textvariable=E_Latte)
txtLatte.grid(row=0,column=1)

txtEspresso = Entry(Drinks_F,font=('Arial',16,'bold'),bd=8,width=6,justify='left',state='disabled',textvariable=E_Espresso)
txtEspresso.grid(row=1,column=1)

txtIced_Latte = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state='disabled',textvariable=E_Iced_Latte)
txtIced_Latte.grid(row=2,column=1)

txtVale_Coffee = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state='disabled',textvariable=E_Vale_Coffee)
txtVale_Coffee.grid(row=3,column=1)

txtCappuccino = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state='disabled',textvariable=E_Cappuccino)
txtCappuccino.grid(row=4,column=1)

txtAfrican_Coffee = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state='disabled',textvariable=E_African_Coffee)
txtAfrican_Coffee.grid(row=5,column=1)

txtAmerican_Coffee = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state='disabled',textvariable=E_American_Coffee)
txtAmerican_Coffee.grid(row=6,column=1)

txtIced_Cappuccino = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state='disabled',textvariable=E_Iced_Cappuccino)
txtIced_Cappuccino.grid(row=7,column=1)



SchoolCake = Checkbutton(Cake_F,text='School Cake\t\t\t',variable=var9,onvalue=1,offvalue=0,font=('Arial',16,'bold'),bg='powder blue',command=chkSchoolCake).grid(row=0,sticky=W)
Sunny_AO_Cake = Checkbutton(Cake_F,text='Sunday O Cake',variable=var10,onvalue=1,offvalue=0,font=('Arial',16,'bold'),bg='powder blue',command=chkSunny_AO_Cake).grid(row=1,sticky=W)
Jonathan_YO_Cake = Checkbutton(Cake_F,text='Jonathan O Cake',variable=var11,onvalue=1,offvalue=0,font=('Arial',16,'bold'),bg='powder blue',command=chkJonathan_YO_Cake).grid(row=2,sticky=W)
West_African_Cake = Checkbutton(Cake_F,text='West African Cake',variable=var12,onvalue=1,offvalue=0,font=('Arial',16,'bold'),bg='powder blue',command=chkWest_African_Cake).grid(row=3,sticky=W)
Lagos_Chocolate_Cake = Checkbutton(Cake_F,text='Lagos Chocolate Cake',variable=var13,onvalue=1,offvalue=0,font=('Arial',16,'bold'),bg='powder blue',command=chkLagos_Chocolate_Cake).grid(row=4,sticky=W)
Kilburn_Chocolate_Cake = Checkbutton(Cake_F,text='Kilburn Chocolate Cake',variable=var14,onvalue=1,offvalue=0,font=('Arial',16,'bold'),bg='powder blue',command=chkKilburn_Chocolate_Cake).grid(row=5,sticky=W)
Carlton_Hill_Cake = Checkbutton(Cake_F,text='Carlton Hill Chocolate Cake',variable=var15,onvalue=1,offvalue=0,font=('Arial',16,'bold'),bg='powder blue',command=chkCarlton_Hill_Cake).grid(row=6,sticky=W)
Queen_Park_Cake = Checkbutton(Cake_F,text="Queen's Park Chocolate Cake",variable=var16,onvalue=1,offvalue=0,font=('Arial',16,'bold'),bg='powder blue',command=chkQueen_Park_Cake).grid(row=7,sticky=W)

txtSchoolCake = Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state='disabled',textvariable=E_SchoolCake)
txtSchoolCake.grid(row=0,column=1)

txtSunny_AO_Cake = Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state='disabled',textvariable=E_Sunny_AO_Cake)
txtSunny_AO_Cake.grid(row=1,column=1)

txtJonathan_YO_Cake = Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state='disabled',textvariable=E_Jonathan_YO_Cake)
txtJonathan_YO_Cake.grid(row=2,column=1)

txtWest_African_Cake = Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state='disabled',textvariable=E_West_African_Cake)
txtWest_African_Cake.grid(row=3,column=1)

txtLagos_Chocolate_Cake = Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state='disabled',textvariable=E_Lagos_Chocolate_Cake)
txtLagos_Chocolate_Cake.grid(row=4,column=1)

txtKilburn_Chocolate_Cake = Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state='disabled',textvariable=E_Kilburn_Chocolate_Cake)
txtKilburn_Chocolate_Cake.grid(row=5,column=1)

txtCarlton_Hill_Cake = Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state='disabled',textvariable=E_Carlton_Hill_Cake)
txtCarlton_Hill_Cake.grid(row=6,column=1)

txtQueen_Park_Cake = Entry(Cake_F,font=('arial',16,'bold'),bd=8,width=6,justify='left',state='disabled',textvariable=E_Queen_Park_Cake)
txtQueen_Park_Cake.grid(row=7,column=1)




lblCostDrinks = Label(Cost_F,font=('Arial',14,'bold'),text='Cost of Drinks\t',bg='powder Blue',fg='black')
lblCostDrinks.grid(row=0,column=0,sticky=W)
txtCostDrinks = Entry(Cost_F,font=('arial',14,'bold'),bd=7,bg='white',insertwidth=2,justify='right',textvariable=CostOfDrinks)
txtCostDrinks.grid(row=0,column=1)

lblCostCakes = Label(Cost_F,font=('Arial',14,'bold'),text='Cost of Cakes\t',bg='powder Blue',fg='black')
lblCostCakes.grid(row=1,column=0,sticky=W)
txtCostCakes = Entry(Cost_F,font=('arial',14,'bold'),bd=7,bg='white',insertwidth=2,justify='right',textvariable=CostOfCakes)
txtCostCakes.grid(row=1,column=1)

lblServiceCharge = Label(Cost_F,font=('Arial',14,'bold'),text='Service Charge\t',bg='powder Blue',fg='black')
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge = Entry(Cost_F,font=('arial',14,'bold'),bd=7,bg='white',justify='right',textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)

lblGST = Label(Cost_F,font=('Arial',14,'bold'),text='\tGST    ',bg='powder Blue',fg='black')
lblGST.grid(row=0,column=2,sticky=W)
txtGST = Entry(Cost_F,font=('arial',14,'bold'),bd=7,bg='white',insertwidth=2,justify='right',textvariable=GST )
txtGST.grid(row=0,column=3)

lblSubTotal = Label(Cost_F,font=('Arial',14,'bold'),text='\tSub Total    ',bg='powder Blue',fg='black')
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal = Entry(Cost_F,font=('arial',14,'bold'),bd=7,bg='white',insertwidth=2,justify='right',textvariable=SubTotal)
txtSubTotal.grid(row=1,column=3)

lblTotalCost = Label(Cost_F,font=('Arial',14,'bold'),text='\tTotal Cost    ',bg='powder Blue',fg='black')
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost = Entry(Cost_F,font=('arial',14,'bold'),bd=7,bg='white',insertwidth=2,justify='right',textvariable=TotalCost)
txtTotalCost.grid(row=2,column=3)


txtReceipt = Text(Receipt_F,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'),state=NORMAL)
txtReceipt.grid(row=0,column=0)




def iExit():
        iExit = tkinter.messagebox.askyesno('Exit Restaurant Management System','Confirm if you want to exit ?')
        if iExit > 0:
                root.destroy()
        else:
                return

def Reset():
        GST.set('')
        SubTotal.set('')
        TotalCost.set('')
        CostOfCakes.set('')
        CostOfDrinks.set('')
        ServiceCharge.set('')
        txtReceipt.configure(state=NORMAL)
        txtReceipt.delete('1.0',END)
        
        
        E_SchoolCake.set('0')
        E_Sunny_AO_Cake.set('0')
        E_Jonathan_YO_Cake.set('0')
        E_West_African_Cake.set('0')
        E_Lagos_Chocolate_Cake.set('0')
        E_Kilburn_Chocolate_Cake.set('0')
        E_Carlton_Hill_Cake.set('0')
        E_Queen_Park_Cake.set('0')
        E_Latte.set('0')
        E_Espresso.set('0')
        E_Iced_Latte.set('0')
        E_Vale_Coffee.set('0')
        E_Cappuccino.set('0')
        E_African_Coffee.set('0')
        E_American_Coffee.set('0')
        E_Iced_Cappuccino.set('0')

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)

        txtLatte.configure(state=DISABLED)
        txtEspresso.configure(state=DISABLED)
        txtIced_Latte.configure(state=DISABLED)
        txtVale_Coffee.configure(state=DISABLED)
        txtCappuccino.configure(state=DISABLED)
        txtAfrican_Coffee.configure(state=DISABLED)
        txtAmerican_Coffee.configure(state=DISABLED)
        txtIced_Cappuccino.configure(state=DISABLED)
        txtSchoolCake.configure(state=DISABLED)
        txtSunny_AO_Cake.configure(state=DISABLED)
        txtJonathan_YO_Cake.configure(state=DISABLED)
        txtWest_African_Cake.configure(state=DISABLED)
        txtLagos_Chocolate_Cake.configure(state=DISABLED)
        txtKilburn_Chocolate_Cake.configure(state=DISABLED)
        txtCarlton_Hill_Cake.configure(state=DISABLED)        
        txtQueen_Park_Cake.configure(state=DISABLED)

        txtDisplay.delete('0',END)
        txtDisplay.insert(0,'0')

def CostofItem():
        Item1 = float(E_Latte.get())
        Item2 = float(E_Espresso.get())
        Item3 = float(E_Iced_Latte.get())
        Item4 = float(E_Vale_Coffee.get())
        Item5 = float(E_Cappuccino.get())
        Item6 = float(E_African_Coffee.get())
        Item7 = float(E_American_Coffee.get())
        Item8 = float(E_Iced_Cappuccino.get())
        Item9 = float(E_SchoolCake.get())
        Item10 = float(E_Sunny_AO_Cake.get())
        Item11 = float(E_Jonathan_YO_Cake.get())
        Item12 = float(E_West_African_Cake.get())
        Item13 = float(E_Lagos_Chocolate_Cake.get())
        Item14 = float(E_Kilburn_Chocolate_Cake.get())
        Item15 = float(E_Carlton_Hill_Cake.get())
        Item16 = float(E_Queen_Park_Cake.get())

        PriceOfDrinks = (Item1 * 50) + (Item2 * 60) + (Item3 * 60) + (Item4 * 45) + (Item5 * 60) + (Item6 * 75) + (Item7 * 75) + (Item8 * 70)
        PriceOfCakes = (Item9 * 110) + (Item10 * 120) + (Item11 * 120) + (Item12 * 150) + (Item13 * 220) + (Item14 * 220) + (Item15 * 180) + (Item16 * 175)

        DrinksPrice = u"\u20B9",str('%.2f'%(PriceOfDrinks))
        CakesPrice = u"\u20B9",str('%.2f'%(PriceOfCakes))
        CostOfCakes.set(CakesPrice)
        CostOfDrinks.set(DrinksPrice)

        SC = u"\u20B9",str('%.2f'%(10))
        ServiceCharge.set(SC)

        SubTotalOfItems = u"\u20B9",str('%.2f'%(PriceOfDrinks+PriceOfCakes+10))
        SubTotal.set(SubTotalOfItems)

        Tax = u"\u20B9",str('%.2f'%((PriceOfDrinks+PriceOfCakes+10)*0.15))
        GST.set(Tax)

        TT = ((PriceOfDrinks+PriceOfCakes+10)*0.15)
        TC = u"\u20B9",str('%.2f'%(PriceOfDrinks+PriceOfCakes+10+TT))
        TotalCost.set(TC)

        if (PriceOfDrinks == 0) and (PriceOfCakes == 0):
                tkinter.messagebox.showinfo('Important Info',"Since you haven't bought anything and you want the total of\nyour purchase (which is 0) we would still like to charge you the\ntax for breathing,watching,hearing and sensing !!")


btnTotal = Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Total',bg='powder blue',command=CostofItem).grid(row=0,column=0)
btnReceipt = Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Receipt',bg='powder blue',command=Receipt).grid(row=0,column=1)
btnReset = Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Reset',bg='powder blue',command=Reset).grid(row=0,column=2)
btnExit = Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Exit',bg='powder blue',command=iExit).grid(row=0,column=3)


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    result = str(eval(expression)) 
    input_text.set(result)
    expression = ""


expression = ""
input_text = StringVar()


txtDisplay = Entry(Cal_F,width=45,bg='white',bd=4,font=('arial',12,'bold'),justify='right',textvariable=input_text)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,'0')



btn7 = Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='7',command=lambda: btn_click(7)).grid(row=2,column=0)
btn8 = Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='8',command=lambda: btn_click(8)).grid(row=2,column=1)
btn9 = Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='9',command=lambda: btn_click(9)).grid(row=2,column=2)
btnAdd = Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='+',bg='powder blue',command=lambda: btn_click("+")).grid(row=2,column=3)
btn4 = Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='4',command=lambda: btn_click(4)).grid(row=3,column=0)
btn5 = Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='5',command=lambda: btn_click(5)).grid(row=3,column=1)
btn6 = Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='6',command=lambda: btn_click(6)).grid(row=3,column=2)
btnSub = Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='-',bg='powder blue',command=lambda: btn_click("-")).grid(row=3,column=3)
btn1 = Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='1',command=lambda: btn_click(1)).grid(row=4,column=0)
btn2 = Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='2',command=lambda: btn_click(2)).grid(row=4,column=1)
btn3 = Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='3',command=lambda: btn_click(3)).grid(row=4,column=2)
btnMulti = Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='x',bg='powder blue',command=lambda: btn_click("*")).grid(row=4,column=3)
btn0 = Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='0',bg='powder blue',command=lambda: btn_click(0)).grid(row=5,column=0)
btnClear = Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='C',bg='powder blue',command=lambda: btn_clear).grid(row=5,column=1)
btnEquals = Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='=',bg='powder blue',command=lambda: btn_equal).grid(row=5,column=2)
btnDiv = Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text=chr(247),bg='powder blue',command=lambda: btn_click('/')).grid(row=5,column=3)



root.tk_focusFollowsMouse()
root.mainloop()
