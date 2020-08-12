from tkinter import *
import tkinter.messagebox as tkmb
import time
import tkinter.ttk as ttk
import random
import pandas as pd
from tabulate import tabulate
from Receipt_SQL_Connector import *
import os


root = Tk()
root.geometry('1350x725+0+0')
root.title('Restaurant Management System')
root.config(bg='#9d0000')


################################################# FRAMES #################################################


Top_Frame = Frame(root, bg='red', bd=4, relief='sunken')
Top_Frame.pack(anchor='n')

Title_Label = Label(Top_Frame, font=('Arial', 21, 'bold'), width=78, text='Restaurant Management System', bd=15,
                    bg='#890000', fg='orange', justify='left')
Title_Label.grid(row=0, column=0)
Title_Label.grid_rowconfigure(0, weight=10)
Title_Label.grid_columnconfigure(0, weight=10)

Total_Receipt_Frame = Frame(root, bg='orange', bd=5)
Total_Receipt_Frame.pack(side='right', anchor='e')

Buttons_Frame = Frame(Total_Receipt_Frame, bg='orange', bd=4, relief='ridge')
Buttons_Frame.pack(side='bottom', anchor='s')

Calculator_Frame = Frame(Total_Receipt_Frame, bg='orange', bd=4, relief='ridge')
Calculator_Frame.pack(side='top', anchor='nw')

Receipt_Frame = Frame(Total_Receipt_Frame, bg='orange', bd=3, relief='ridge')
Receipt_Frame.pack(side='bottom', anchor='se')

Menu_Frame = Frame(root, bg='Yellow', bd=2, relief='ridge')
Menu_Frame.pack(side='left', anchor='w')

Cost_Frame = Frame(Menu_Frame, bg='orange', bd=3, relief='groove')
Cost_Frame.pack(side='bottom', anchor='center')

Drinks_Frame = Frame(Menu_Frame, bg='orange', bd=3, relief='ridge')
Drinks_Frame.pack(side='left', anchor='nw')

Food_Frame = Frame(Menu_Frame, bg='orange', bd=3, relief='ridge')
Food_Frame.pack(side='left', anchor='n')

Packed_Food = Frame(Menu_Frame, bg='orange', bd=3, relief='ridge')
Packed_Food.pack(side='left', anchor='n')

Payment_Frame = Frame(root, bg='orange', bd=6, relief='raised')
Payment_Frame.pack(anchor='n', pady=5, ipady=5)

################################################### VARIABLES ##################################################

'''INT VARS'''

var1 = IntVar()
var2 = IntVar()
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
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
var28 = IntVar()
var29 = IntVar()
var30 = IntVar()
var31 = IntVar()
var32 = IntVar()
var33 = IntVar()
var34 = IntVar()
var35 = IntVar()
var36 = IntVar()
var37 = IntVar()
var38 = IntVar()
var39 = IntVar()
var40 = IntVar()
var41 = IntVar()
var42 = IntVar()
var43 = IntVar()
var44 = IntVar()
var45 = IntVar()
var46 = IntVar()
var47 = IntVar()
var48 = IntVar()
var49 = IntVar()
var50 = IntVar()
var51 = IntVar()
var52 = IntVar()
var53 = IntVar()
var54 = IntVar()
var55 = IntVar()
var56 = IntVar()
var57 = IntVar()
var58 = IntVar()
var59 = IntVar()
var60 = IntVar()
var61 = IntVar()
var62 = IntVar()
var63 = IntVar()
var64 = IntVar()
var65 = IntVar()
var66 = IntVar()
var67 = IntVar()
var68 = IntVar()
var69 = IntVar()

''' STRING VARS '''
# ENTRY VARIABLES #

'''''''''''BILL'''''''''''

EV_DateofOrder = StringVar()
EV_ReceiptRef = StringVar()
EV_GST = StringVar()
EV_TotalCost = StringVar()
EV_CostofDrinks = StringVar()
EV_CostofFood = StringVar()
EV_CostofPackedFood = StringVar()
EV_ServiceCharge = StringVar()
EV_InputText = StringVar()

'''''''''''DRINKS'''''''''''

EV_MineralWater = StringVar()
EV_HotCoffee = StringVar()
EV_ColdCoffee = StringVar()
EV_HotChocolate = StringVar()
EV_Cappuccino = StringVar()
EV_Tea = StringVar()
EV_IcedTea = StringVar()
EV_ChocolateShake_R = StringVar()
EV_OreoShake_R = StringVar()
EV_StrawberryShake_R = StringVar()
EV_PineappleShake_R = StringVar()
EV_KitkatShake_R = StringVar()
EV_ChocolateShake_T = StringVar()
EV_OreoShake_T = StringVar()
EV_StrawberryShake_T = StringVar()
EV_PineappleShake_T = StringVar()
EV_KitkatShake_T = StringVar()
EV_ColdDrink_C = StringVar()
EV_ColdDrink_S = StringVar()
EV_VirginMojito = StringVar()
EV_MoscowMule = StringVar()
EV_Martini = StringVar()
EV_CranberryJuice = StringVar()

'''''''''''FOOD ITEMS'''''''''''

EV_FrenchFries = StringVar()
EV_CheeseBalls = StringVar()
EV_VegSandwich = StringVar()
EV_GrilledSandwich = StringVar()
EV_GrilledCheeseSandwich = StringVar()
EV_PaneerSandwich = StringVar()
EV_NutellaSandwich = StringVar()
EV_AlooTikkiBurger = StringVar()
EV_VegWhooper = StringVar()
EV_DoubleCheeseBurger = StringVar()
EV_PaneerKingBurger = StringVar()
EV_WhitePasta = StringVar()
EV_RedPasta = StringVar()
EV_SpecialItalianPasta = StringVar()
EV_MargheritaPizza = StringVar()
EV_SuperVeggiePizza = StringVar()
EV_PaneerCrispPizza = StringVar()
EV_PeriPeriPaneerPizza = StringVar()
EV_ChefSpecialCountryConnectionPizza = StringVar()
EV_MexicanTacos = StringVar()
EV_PaneerWrap = StringVar()
EV_SpringRoll = StringVar()
EV_PizzaRolls = StringVar()

'''''''''''PACKED FOOD ITEMS'''''''''''

EV_Lays = StringVar()
EV_Kurkure = StringVar()
EV_Bingo = StringVar()
EV_Nutella = StringVar()
EV_HersheysChocolateSyrup = StringVar()
EV_Bhujia = StringVar()
EV_Mixture = StringVar()
EV_SoyaStix = StringVar()
EV_BrittaniaMarieGold = StringVar()
EV_5050 = StringVar()
EV_Oreo = StringVar()
EV_HideandSeek = StringVar()
EV_DarkFantasy = StringVar()
EV_KinderJoy = StringVar()
EV_Nachos = StringVar()
EV_Bournvita = StringVar()
EV_Complan = StringVar()
EV_KellogsChocos = StringVar()
EV_Rusk = StringVar()
EV_DairyMilkSilk = StringVar()
EV_NestlesDarkSensation = StringVar()
EV_HersheysWhiteCocoaChocolate = StringVar()
EV_Pedigree = StringVar()

'''  Payment Combobox Variable  '''

cbvar = StringVar()

'''  DEFAULT ENTRIES '''

EV_MineralWater.set('0')
EV_HotCoffee.set('0')
EV_ColdCoffee.set('0')
EV_HotChocolate.set('0')
EV_Cappuccino.set('0')
EV_Tea.set('0')
EV_IcedTea.set('0')
EV_ChocolateShake_R.set('0')
EV_OreoShake_R.set('0')
EV_StrawberryShake_R.set('0')
EV_PineappleShake_R.set('0')
EV_KitkatShake_R.set('0')
EV_ChocolateShake_T.set('0')
EV_OreoShake_T.set('0')
EV_StrawberryShake_T.set('0')
EV_PineappleShake_T.set('0')
EV_KitkatShake_T.set('0')
EV_ColdDrink_C.set('0')
EV_ColdDrink_S.set('0')
EV_VirginMojito.set('0')
EV_MoscowMule.set('0')
EV_Martini.set('0')
EV_CranberryJuice.set('0')

EV_FrenchFries.set('0')
EV_CheeseBalls.set('0')
EV_VegSandwich.set('0')
EV_GrilledSandwich.set('0')
EV_GrilledCheeseSandwich.set('0')
EV_PaneerSandwich.set('0')
EV_NutellaSandwich.set('0')
EV_AlooTikkiBurger.set('0')
EV_VegWhooper.set('0')
EV_DoubleCheeseBurger.set('0')
EV_PaneerKingBurger.set('0')
EV_WhitePasta.set('0')
EV_RedPasta.set('0')
EV_SpecialItalianPasta.set('0')
EV_MargheritaPizza.set('0')
EV_SuperVeggiePizza.set('0')
EV_PaneerCrispPizza.set('0')
EV_PeriPeriPaneerPizza.set('0')
EV_ChefSpecialCountryConnectionPizza.set('0')
EV_MexicanTacos.set('0')
EV_PaneerWrap.set('0')
EV_SpringRoll.set('0')
EV_PizzaRolls.set('0')

EV_Lays.set('0')
EV_Kurkure.set('0')
EV_Bingo.set('0')
EV_Nutella.set('0')
EV_HersheysChocolateSyrup.set('0')
EV_Bhujia.set('0')
EV_Mixture.set('0')
EV_SoyaStix.set('0')
EV_BrittaniaMarieGold.set('0')
EV_5050.set('0')
EV_Oreo.set('0')
EV_HideandSeek.set('0')
EV_DarkFantasy.set('0')
EV_KinderJoy.set('0')
EV_Nachos.set('0')
EV_Bournvita.set('0')
EV_Complan.set('0')
EV_KellogsChocos.set('0')
EV_Rusk.set('0')
EV_NestlesDarkSensation.set('0')
EV_DairyMilkSilk.set('0')
EV_HersheysWhiteCocoaChocolate.set('0')
EV_Pedigree.set('0')

''' DATE OF ORDER ENTRY '''

EV_DateofOrder.set(time.strftime('%d-%m-%Y'))

################################################## COST OF #####################################################
################################################# PRODUCTS #####################################################

CostofMineralWater = 15
CostofHotCoffee = 30
CostofColdCoffee = 45
CostofHotChocolate = 45
CostofCappuccino = 50
CostofTea = 10
CostofIcedTea = 60
CostofChocolateShake_R = 75
CostofOreoShake_R = 95
CostofStrawberryShake_R = 75
CostofPineappleShake_R = 70
CostofKitkatShake_R = 95
CostofChocolateShake_T = 100
CostofOreoShake_T = 130
CostofStrawberryShake_T = 100
CostofPineappleShake_T = 95
CostofKitkatShake_T = 130
CostofColdDrink_C = 35
CostofColdDrink_S = 45
CostofVirginMojito = 120
CostofMoscowMule = 140
CostofMartini = 130
CostofCranberryJuice = 140
CostofFrenchFries = 60
CostofCheeseBalls = 50
CostofVegSandwich = 50
CostofGrilledSandwich = 75
CostofGrilledCheeseSandwich = 90
CostofPaneerSandwich = 75
CostofNutellaSandwich = 120
CostofAlooTikkiBurger = 35
CostofVegWhooper = 45
CostofDoubleCheeseBurger = 50
CostofPaneerKingBurger = 75
CostofWhitePasta = 110
CostofRedPasta = 110
CostofSpecialItalianPasta = 130
CostofMargherita = 120
CostofSuperVeggiePizza = 130
CostofPaneerCrispPizza = 150
CostofPeriPeriPaneerPizza = 200
CostofChefSpecialCountryConnectionPizza = 250
CostofMexicanTacos = 45
CostofPaneerWrap = 75
CostofSpringRoll = 60
CostofPizzaRolls = 90
CostofLays = 20
CostofKurkure = 20
CostofBingo = 20
CostofNutella = 750
CostofHersheysChocolateSyrup = 320
CostofBhujia = 45
CostofMixture = 60
CostofSoyaStix = 30
CostofBrittaniaMarieGold = 30
Costof5050 = 10
CostofOreo = 30
CostofHideandSeek = 30
CostofDarkFantasy = 40
CostofKinderJoy = 40
CostofNachos = 35
CostofBournvita = 400
CostofComplan = 225
CostofKellogsChocos = 300
CostofRusk = 65
CostofDairyMilkSilk = 75
CostofHersheysWhiteCocoaChocolate = 290
CostofNestlesDarkSensation = 100
CostofPedigree = 260


#################################################### VAR ######################################################
################################################# FUNCTIONS ###################################################


def chkMineralWater():
    if var1.get() == 1:
        TXT_MineralWater.configure(state='normal')
        TXT_MineralWater.focus()
        TXT_MineralWater.delete('0', END)
        EV_MineralWater.set('')
    elif var1.get() == 0:
        TXT_MineralWater.configure(state='disabled')
        EV_MineralWater.set('0')


def chkHotCoffee():
    if var2.get() == 1:
        TXT_HotCoffee.configure(state='normal')
        TXT_HotCoffee.focus()
        TXT_HotCoffee.delete('0', END)
        EV_HotCoffee.set('')
    elif var2.get() == 0:
        TXT_HotCoffee.configure(state='disabled')
        EV_HotCoffee.set('0')


def chkColdCoffee():
    if var3.get() == 1:
        TXT_ColdCoffee.configure(state='normal')
        TXT_ColdCoffee.focus()
        TXT_ColdCoffee.delete('0', END)
        EV_ColdCoffee.set('')
    elif var3.get() == 0:
        TXT_ColdCoffee.configure(state='disabled')
        EV_ColdCoffee.set('0')


def chkHotChocolate():
    if var4.get() == 1:
        TXT_HotChocolate.configure(state='normal')
        TXT_HotChocolate.focus()
        TXT_HotChocolate.delete('0', END)
        EV_HotChocolate.set('')
    elif var4.get() == 0:
        TXT_HotChocolate.configure(state='disabled')
        EV_HotChocolate.set('0')


def chkCappuccino():
    if var5.get() == 1:
        TXT_Cappuccino.configure(state='normal')
        TXT_Cappuccino.focus()
        TXT_Cappuccino.delete('0', END)
        EV_Cappuccino.set('')
    elif var5.get() == 0:
        TXT_Cappuccino.configure(state='disabled')
        EV_Cappuccino.set('0')


def chkTea():
    if var6.get() == 1:
        TXT_Tea.configure(state='normal')
        TXT_Tea.focus()
        TXT_Tea.delete('0', END)
        EV_Tea.set('')
    elif var6.get() == 0:
        TXT_Tea.configure(state='disabled')
        EV_Tea.set('0')


def chkIcedTea():
    if var7.get() == 1:
        TXT_IcedTea.configure(state='normal')
        TXT_IcedTea.focus()
        TXT_IcedTea.delete('0', END)
        EV_IcedTea.set('')
    elif var7.get() == 0:
        TXT_IcedTea.configure(state='disabled')
        EV_IcedTea.set('0')


def chkChocolateShake_R():
    if var8.get() == 1:
        TXT_ChocolateShake_R.configure(state='normal')
        TXT_ChocolateShake_R.focus()
        TXT_ChocolateShake_R.delete('0', END)
        EV_ChocolateShake_R.set('')
    elif var8.get() == 0:
        TXT_ChocolateShake_R.configure(state='disabled')
        EV_ChocolateShake_R.set('0')


def chkOreoShake_R():
    if var9.get() == 1:
        TXT_OreoShake_R.configure(state='normal')
        TXT_OreoShake_R.focus()
        TXT_OreoShake_R.delete('0', END)
        EV_OreoShake_R.set('')
    elif var9.get() == 0:
        TXT_OreoShake_R.configure(state='disabled')
        EV_OreoShake_R.set('0')


def chkStrawberryShake_R():
    if var10.get() == 1:
        TXT_StrawberryShake_R.configure(state='normal')
        TXT_StrawberryShake_R.focus()
        TXT_StrawberryShake_R.delete('0', END)
        EV_StrawberryShake_R.set('')
    elif var10.get() == 0:
        TXT_StrawberryShake_R.configure(state='disabled')
        EV_StrawberryShake_R.set('0')


def chkPineappleShake_R():
    if var11.get() == 1:
        TXT_PineappleShake_R.configure(state='normal')
        TXT_PineappleShake_R.focus()
        TXT_PineappleShake_R.delete('0', END)
        EV_PineappleShake_R.set('')
    elif var11.get() == 0:
        TXT_PineappleShake_R.configure(state='disabled')
        EV_PineappleShake_R.set('0')


def chkKitkatShake_R():
    if var12.get() == 1:
        TXT_KitkatShake_R.configure(state='normal')
        TXT_KitkatShake_R.focus()
        TXT_KitkatShake_R.delete('0', END)
        EV_KitkatShake_R.set('')
    elif var12.get() == 0:
        TXT_KitkatShake_R.configure(state='disabled')
        EV_KitkatShake_R.set('0')


def chkChocolateShake_T():
    if var13.get() == 1:
        TXT_ChocolateShake_T.configure(state='normal')
        TXT_ChocolateShake_T.focus()
        TXT_ChocolateShake_T.delete('0', END)
        EV_ChocolateShake_T.set('')
    elif var13.get() == 0:
        TXT_ChocolateShake_T.configure(state='disabled')
        EV_ChocolateShake_T.set('0')


def chkOreoShake_T():
    if var14.get() == 1:
        TXT_OreoShake_T.configure(state='normal')
        TXT_OreoShake_T.focus()
        TXT_OreoShake_T.delete('0', END)
        EV_OreoShake_T.set('')
    elif var14.get() == 0:
        TXT_OreoShake_T.configure(state='disabled')
        EV_OreoShake_T.set('0')


def chkStrawberryShake_T():
    if var15.get() == 1:
        TXT_StrawberryShake_T.configure(state='normal')
        TXT_StrawberryShake_T.focus()
        TXT_StrawberryShake_T.delete('0', END)
        EV_StrawberryShake_T.set('')
    elif var15.get() == 0:
        TXT_StrawberryShake_T.configure(state='disabled')
        EV_StrawberryShake_T.set('0')


def chkPineappleShake_T():
    if var16.get() == 1:
        TXT_PineappleShake_T.configure(state='normal')
        TXT_PineappleShake_T.focus()
        TXT_PineappleShake_T.delete('0', END)
        EV_PineappleShake_T.set('')
    elif var16.get() == 0:
        TXT_PineappleShake_T.configure(state='disabled')
        EV_PineappleShake_T.set('0')


def chkKitkatShake_T():
    if var17.get() == 1:
        TXT_KitkatShake_T.configure(state='normal')
        TXT_KitkatShake_T.focus()
        TXT_KitkatShake_T.delete('0', END)
        EV_KitkatShake_T.set('')
    elif var17.get() == 0:
        TXT_KitkatShake_T.configure(state='disabled')
        EV_KitkatShake_T.set('0')


def chkColdDrink_C():
    if var18.get() == 1:
        TXT_ColdDrink_C.configure(state='normal')
        TXT_ColdDrink_C.focus()
        TXT_ColdDrink_C.delete('0', END)
        EV_ColdDrink_C.set('')
    elif var18.get() == 0:
        TXT_ColdDrink_C.configure(state='disabled')
        EV_ColdDrink_C.set('0')


def chkColdDrink_S():
    if var19.get() == 1:
        TXT_ColdDrink_S.configure(state='normal')
        TXT_ColdDrink_S.focus()
        TXT_ColdDrink_S.delete('0', END)
        EV_ColdDrink_S.set('')
    elif (var19.get() == 0):
        TXT_ColdDrink_S.configure(state='disabled')
        EV_ColdDrink_S.set('0')


def chkVirginMojito():
    if var20.get() == 1:
        TXT_VirginMojito.configure(state='normal')
        TXT_VirginMojito.focus()
        TXT_VirginMojito.delete('0', END)
        EV_VirginMojito.set('')
    elif var20.get() == 0:
        TXT_VirginMojito.configure(state='disabled')
        EV_VirginMojito.set('0')


def chkMoscowMule():
    if var21.get() == 1:
        TXT_MoscowMule.configure(state='normal')
        TXT_MoscowMule.focus()
        TXT_MoscowMule.delete('0', END)
        EV_MoscowMule.set('')
    elif var21.get() == 0:
        TXT_MoscowMule.configure(state='disabled')
        EV_MoscowMule.set('0')


def chkMartini():
    if var22.get() == 1:
        TXT_Martini.configure(state='normal')
        TXT_Martini.focus()
        TXT_Martini.delete('0', END)
        EV_Martini.set('')
    elif var22.get() == 0:
        TXT_Martini.configure(state='disabled')
        EV_Martini.set('0')


def chkCranberryJuice():
    if var23.get() == 1:
        TXT_CranberryJuice.configure(state='normal')
        TXT_CranberryJuice.focus()
        TXT_CranberryJuice.delete('0', END)
        EV_CranberryJuice.set('')
    elif var23.get() == 0:
        TXT_CranberryJuice.configure(state='disabled')
        EV_CranberryJuice.set('0')


def chkFrenchFries():
    if var24.get() == 1:
        TXT_FrenchFries.configure(state='normal')
        TXT_FrenchFries.focus()
        TXT_FrenchFries.delete('0', END)
        EV_FrenchFries.set('')
    elif var24.get() == 0:
        TXT_FrenchFries.configure(state='disabled')
        EV_FrenchFries.set('0')


def chkCheeseBalls():
    if var25.get() == 1:
        TXT_CheeseBalls.configure(state='normal')
        TXT_CheeseBalls.focus()
        TXT_CheeseBalls.delete('0', END)
        EV_CheeseBalls.set('')
    elif var25.get() == 0:
        TXT_CheeseBalls.configure(state='disabled')
        EV_CheeseBalls.set('0')


def chkVegSandwich():
    if var26.get() == 1:
        TXT_VegSandwich.configure(state='normal')
        TXT_VegSandwich.focus()
        TXT_VegSandwich.delete('0', END)
        EV_VegSandwich.set('')
    elif var26.get() == 0:
        TXT_VegSandwich.configure(state='disabled')
        EV_VegSandwich.set('0')


def chkGrilledSandwich():
    if var27.get() == 1:
        TXT_GrilledSandwich.configure(state='normal')
        TXT_GrilledSandwich.focus()
        TXT_GrilledSandwich.delete('0', END)
        EV_GrilledSandwich.set('')
    elif var27.get() == 0:
        TXT_GrilledSandwich.configure(state='disabled')
        EV_GrilledSandwich.set('0')


def chkGrilledCheeseSandwich():
    if var28.get() == 1:
        TXT_GrilledCheeseSandwich.configure(state='normal')
        TXT_GrilledCheeseSandwich.focus()
        TXT_GrilledCheeseSandwich.delete('0', END)
        EV_GrilledCheeseSandwich.set('')
    elif var28.get() == 0:
        TXT_GrilledCheeseSandwich.configure(state='disabled')
        EV_GrilledCheeseSandwich.set('0')


def chkPaneerSandwich():
    if var29.get() == 1:
        TXT_PaneerSandwich.configure(state='normal')
        TXT_PaneerSandwich.focus()
        TXT_PaneerSandwich.delete('0', END)
        EV_PaneerSandwich.set('')
    elif var29.get() == 0:
        TXT_PaneerSandwich.configure(state='disabled')
        EV_PaneerSandwich.set('0')


def chkNutellaSandwich():
    if var30.get() == 1:
        TXT_NutellaSandwich.configure(state='normal')
        TXT_NutellaSandwich.focus()
        TXT_NutellaSandwich.delete('0', END)
        EV_NutellaSandwich.set('')
    elif var30.get() == 0:
        TXT_NutellaSandwich.configure(state='disabled')
        EV_NutellaSandwich.set('0')


def chkAlooTikkiBurger():
    if var31.get() == 1:
        TXT_AlooTikkiBurger.configure(state='normal')
        TXT_AlooTikkiBurger.focus()
        TXT_AlooTikkiBurger.delete('0', END)
        EV_AlooTikkiBurger.set('')
    elif var31.get() == 0:
        TXT_AlooTikkiBurger.configure(state='disabled')
        EV_AlooTikkiBurger.set('0')


def chkVegWhooper():
    if var32.get() == 1:
        TXT_VegWhooper.configure(state='normal')
        TXT_VegWhooper.focus()
        TXT_VegWhooper.delete('0', END)
        EV_VegWhooper.set('')
    elif var32.get() == 0:
        TXT_VegWhooper.configure(state='disabled')
        EV_VegWhooper.set('0')


def chkDoubleCheeseBurger():
    if var33.get() == 1:
        TXT_DoubleCheeseBurger.configure(state='normal')
        TXT_DoubleCheeseBurger.focus()
        TXT_DoubleCheeseBurger.delete('0', END)
        EV_DoubleCheeseBurger.set('')
    elif var33.get() == 0:
        TXT_DoubleCheeseBurger.configure(state='disabled')
        EV_DoubleCheeseBurger.set('0')


def chkPaneerKingBurger():
    if var34.get() == 1:
        TXT_PaneerKingBurger.configure(state='normal')
        TXT_PaneerKingBurger.focus()
        TXT_PaneerKingBurger.delete('0', END)
        EV_PaneerKingBurger.set('')
    elif var34.get() == 0:
        TXT_PaneerKingBurger.configure(state='disabled')
        EV_PaneerKingBurger.set('0')


def chkWhitePasta():
    if var35.get() == 1:
        TXT_WhitePasta.configure(state='normal')
        TXT_WhitePasta.focus()
        TXT_WhitePasta.delete('0', END)
        EV_WhitePasta.set('')
    elif var35.get() == 0:
        TXT_WhitePasta.configure(state='disabled')
        EV_WhitePasta.set('0')


def chkRedPasta():
    if var36.get() == 1:
        TXT_RedPasta.configure(state='normal')
        TXT_RedPasta.focus()
        TXT_RedPasta.delete('0', END)
        EV_RedPasta.set('')
    elif var36.get() == 0:
        TXT_RedPasta.configure(state='disabled')
        EV_RedPasta.set('0')


def chkSpecialItalianPasta():
    if var37.get() == 1:
        TXT_SpecialItalianPasta.configure(state='normal')
        TXT_SpecialItalianPasta.focus()
        TXT_SpecialItalianPasta.delete('0', END)
        EV_SpecialItalianPasta.set('')
    elif var37.get() == 0:
        TXT_SpecialItalianPasta.configure(state='disabled')
        EV_SpecialItalianPasta.set('0')


def chkMargheritaPizza():
    if var38.get() == 1:
        TXT_MargheritaPizza.configure(state='normal')
        TXT_MargheritaPizza.focus()
        TXT_MargheritaPizza.delete('0', END)
        EV_MargheritaPizza.set('')
    elif var38.get() == 0:
        TXT_MargheritaPizza.configure(state='disabled')
        EV_MargheritaPizza.set('0')


def chkSuperVeggiePizza():
    if var39.get() == 1:
        TXT_SuperVeggiePizza.configure(state='normal')
        TXT_SuperVeggiePizza.focus()
        TXT_SuperVeggiePizza.delete('0', END)
        EV_SuperVeggiePizza.set('')
    elif var39.get() == 0:
        TXT_SuperVeggiePizza.configure(state='disabled')
        EV_SuperVeggiePizza.set('0')


def chkPaneerCrispPizza():
    if var40.get() == 1:
        TXT_PaneerCrispPizza.configure(state='normal')
        TXT_PaneerCrispPizza.focus()
        TXT_PaneerCrispPizza.delete('0', END)
        EV_PaneerCrispPizza.set('')
    elif var40.get() == 0:
        TXT_PaneerCrispPizza.configure(state='disabled')
        EV_PaneerCrispPizza.set('0')


def chkPeriPeriPaneerPizza():
    if var41.get() == 1:
        TXT_PeriPeriPaneerPizza.configure(state='normal')
        TXT_PeriPeriPaneerPizza.focus()
        TXT_PeriPeriPaneerPizza.delete('0', END)
        EV_PeriPeriPaneerPizza.set('')
    elif var41.get() == 0:
        TXT_PeriPeriPaneerPizza.configure(state='disabled')
        EV_PeriPeriPaneerPizza.set('0')


def chkChefSpecialCountryConnectionPizza():
    if var42.get() == 1:
        TXT_ChefSpecialCountryConnectionPizza.configure(state='normal')
        TXT_ChefSpecialCountryConnectionPizza.focus()
        TXT_ChefSpecialCountryConnectionPizza.delete('0', END)
        EV_ChefSpecialCountryConnectionPizza.set('')
    elif var42.get() == 0:
        TXT_ChefSpecialCountryConnectionPizza.configure(state='disabled')
        EV_ChefSpecialCountryConnectionPizza.set('0')


def chkMexicanTacos():
    if var43.get() == 1:
        TXT_MexicanTacos.configure(state='normal')
        TXT_MexicanTacos.focus()
        TXT_MexicanTacos.delete('0', END)
        EV_MexicanTacos.set('')
    elif var43.get() == 0:
        TXT_MexicanTacos.configure(state='disabled')
        EV_MexicanTacos.set('0')


def chkPaneerWrap():
    if var44.get() == 1:
        TXT_PaneerWrap.configure(state='normal')
        TXT_PaneerWrap.focus()
        TXT_PaneerWrap.delete('0', END)
        EV_PaneerWrap.set('')
    elif var44.get() == 0:
        TXT_PaneerWrap.configure(state='disabled')
        EV_PaneerWrap.set('0')


def chkSpringRoll():
    if var45.get() == 1:
        TXT_SpringRoll.configure(state='normal')
        TXT_SpringRoll.focus()
        TXT_SpringRoll.delete('0', END)
        EV_SpringRoll.set('')
    elif var45.get() == 0:
        TXT_SpringRoll.configure(state='disabled')
        EV_SpringRoll.set('0')


def chkPizzaRolls():
    if var46.get() == 1:
        TXT_PizzaRolls.configure(state='normal')
        TXT_PizzaRolls.focus()
        TXT_PizzaRolls.delete('0', END)
        EV_PizzaRolls.set('')
    elif var46.get() == 0:
        TXT_PizzaRolls.configure(state='disabled')
        EV_PizzaRolls.set('0')


def chkLays():
    if var47.get() == 1:
        TXT_Lays.configure(state='normal')
        TXT_Lays.focus()
        TXT_Lays.delete('0', END)
        EV_Lays.set('')
    elif var47.get() == 0:
        TXT_Lays.configure(state='disabled')
        EV_Lays.set('0')


def chkKurkure():
    if var48.get() == 1:
        TXT_Kurkure.configure(state='normal')
        TXT_Kurkure.focus()
        TXT_Kurkure.delete('0', END)
        EV_Kurkure.set('')
    elif var48.get() == 0:
        TXT_Kurkure.configure(state='disabled')
        EV_Kurkure.set('0')


def chkBingo():
    if var49.get() == 1:
        TXT_Bingo.configure(state='normal')
        TXT_Bingo.focus()
        TXT_Bingo.delete('0', END)
        EV_Bingo.set('')
    elif var49.get() == 0:
        TXT_Bingo.configure(state='disabled')
        EV_Bingo.set('0')


def chkNutella():
    if var50.get() == 1:
        TXT_Nutella.configure(state='normal')
        TXT_Nutella.focus()
        TXT_Nutella.delete('0', END)
        EV_Nutella.set('')
    elif var50.get() == 0:
        TXT_Nutella.configure(state='disabled')
        EV_Nutella.set('0')


def chkHersheysChocolateSyrup():
    if var51.get() == 1:
        TXT_HersheysChocolateSyrup.configure(state='normal')
        TXT_HersheysChocolateSyrup.focus()
        TXT_HersheysChocolateSyrup.delete('0', END)
        EV_HersheysChocolateSyrup.set('')
    elif var51.get() == 0:
        TXT_HersheysChocolateSyrup.configure(state='disabled')
        EV_HersheysChocolateSyrup.set('0')


def chkBhujia():
    if var52.get() == 1:
        TXT_Bhujia.configure(state='normal')
        TXT_Bhujia.focus()
        TXT_Bhujia.delete('0', END)
        EV_Bhujia.set('')
    elif var52.get() == 0:
        TXT_Bhujia.configure(state='disabled')
        EV_Bhujia.set('0')


def chkMixture():
    if var53.get() == 1:
        TXT_Mixture.configure(state='normal')
        TXT_Mixture.focus()
        TXT_Mixture.delete('0', END)
        EV_Mixture.set('')
    elif var53.get() == 0:
        TXT_Mixture.configure(state='disabled')
        EV_Mixture.set('0')


def chkSoyaStix():
    if var54.get() == 1:
        TXT_SoyaStix.configure(state='normal')
        TXT_SoyaStix.focus()
        TXT_SoyaStix.delete('0', END)
        EV_SoyaStix.set('')
    elif var54.get() == 0:
        TXT_SoyaStix.configure(state='disabled')
        EV_SoyaStix.set('0')


def chkBrittaniaMarieGold():
    if var55.get() == 1:
        TXT_BrittaniaMarieGold.configure(state='normal')
        TXT_BrittaniaMarieGold.focus()
        TXT_BrittaniaMarieGold.delete('0', END)
        EV_BrittaniaMarieGold.set('')
    elif var55.get() == 0:
        TXT_BrittaniaMarieGold.configure(state='disabled')
        EV_BrittaniaMarieGold.set('0')


def chk5050():
    if var56.get() == 1:
        TXT_5050.configure(state='normal')
        TXT_5050.focus()
        TXT_5050.delete('0', END)
        EV_5050.set('')
    elif var56.get() == 0:
        TXT_5050.configure(state='disabled')
        EV_5050.set('0')


def chkOreo():
    if var57.get() == 1:
        TXT_Oreo.configure(state='normal')
        TXT_Oreo.focus()
        TXT_Oreo.delete('0', END)
        EV_Oreo.set('')
    elif var57.get() == 0:
        TXT_Oreo.configure(state='disabled')
        EV_Oreo.set('0')


def chkHideandSeek():
    if var58.get() == 1:
        TXT_HideandSeek.configure(state='normal')
        TXT_HideandSeek.focus()
        TXT_HideandSeek.delete('0', END)
        EV_HideandSeek.set('')
    elif var58.get() == 0:
        TXT_HideandSeek.configure(state='disabled')
        EV_HideandSeek.set('0')


def chkDarkFantasy():
    if var59.get() == 1:
        TXT_DarkFantasy.configure(state='normal')
        TXT_DarkFantasy.focus()
        TXT_DarkFantasy.delete('0', END)
        EV_DarkFantasy.set('')
    elif var59.get() == 0:
        TXT_DarkFantasy.configure(state='disabled')
        EV_DarkFantasy.set('0')


def chkKinderJoy():
    if var60.get() == 1:
        TXT_KinderJoy.configure(state='normal')
        TXT_KinderJoy.focus()
        TXT_KinderJoy.delete('0', END)
        EV_KinderJoy.set('')
    elif var60.get() == 0:
        TXT_KinderJoy.configure(state='disabled')
        EV_KinderJoy.set('0')


def chkNachos():
    if var61.get() == 1:
        TXT_Nachos.configure(state='normal')
        TXT_Nachos.focus()
        TXT_Nachos.delete('0', END)
        EV_Nachos.set('')
    elif var61.get() == 0:
        TXT_Nachos.configure(state='disabled')
        EV_Nachos.set('0')


def chkBournvita():
    if var62.get() == 1:
        TXT_Bournvita.configure(state='normal')
        TXT_Bournvita.focus()
        TXT_Bournvita.delete('0', END)
        EV_Bournvita.set('')
    elif var62.get() == 0:
        TXT_Bournvita.configure(state='disabled')
        EV_Bournvita.set('0')


def chkComplan():
    if var63.get() == 1:
        TXT_Complan.configure(state='normal')
        TXT_Complan.focus()
        TXT_Complan.delete('0', END)
        EV_Complan.set('')
    elif var63.get() == 0:
        TXT_Complan.configure(state='disabled')
        EV_Complan.set('0')


def chkKellogsChocos():
    if var64.get() == 1:
        TXT_KellogsChocos.configure(state='normal')
        TXT_KellogsChocos.focus()
        TXT_KellogsChocos.delete('0', END)
        EV_KellogsChocos.set('')
    elif var64.get() == 0:
        TXT_KellogsChocos.configure(state='disabled')
        EV_KellogsChocos.set('0')


def chkRusk():
    if var65.get() == 1:
        TXT_Rusk.configure(state='normal')
        TXT_Rusk.focus()
        TXT_Rusk.delete('0', END)
        EV_Rusk.set('')
    elif var65.get() == 0:
        TXT_Rusk.configure(state='disabled')
        EV_Rusk.set('0')


def chkDairyMilkSilk():
    if var66.get() == 1:
        TXT_DairyMilkSilk.configure(state='normal')
        TXT_DairyMilkSilk.focus()
        TXT_DairyMilkSilk.delete('0', END)
        EV_DairyMilkSilk.set('')
    elif var66.get() == 0:
        TXT_DairyMilkSilk.configure(state='disabled')
        EV_DairyMilkSilk.set('0')


def chkHersheysWhiteCocoaChocolate():
    if var67.get() == 1:
        TXT_HersheysWhiteCocoaChocolate.configure(state='normal')
        TXT_HersheysWhiteCocoaChocolate.focus()
        TXT_HersheysWhiteCocoaChocolate.delete('0', END)
        EV_HersheysWhiteCocoaChocolate.set('')
    elif var67.get() == 0:
        TXT_HersheysWhiteCocoaChocolate.configure(state='disabled')
        EV_HersheysWhiteCocoaChocolate.set('0')


def chkNestlesDarkSensation():
    if var68.get() == 1:
        TXT_NestlesDarkSensation.configure(state='normal')
        TXT_NestlesDarkSensation.focus()
        TXT_NestlesDarkSensation.delete('0', END)
        EV_NestlesDarkSensation.set('')
    elif var68.get() == 0:
        TXT_NestlesDarkSensation.configure(state='disabled')
        EV_NestlesDarkSensation.set('0')


def chkPedigree():
    if var69.get() == 1:
        TXT_Pedigree.configure(state='normal')
        TXT_Pedigree.focus()
        TXT_Pedigree.delete('0', END)
        EV_Pedigree.set('')
    elif (var69.get() == 0):
        TXT_Pedigree.configure(state='disabled')
        EV_Pedigree.set('0')


################################################# CHECKBUTTONS #################################################
################################################## & ENTRIES ###################################################


''' DRINKS CHECKBUTTONS '''

MineralWater = Checkbutton(Drinks_Frame, text='Mineral Water', bg='orange', variable=var1, onvalue=1, offvalue=0,
                           font=('Arial', 9, 'normal'), command=chkMineralWater).grid(row=0, sticky='w')
HotCoffee = Checkbutton(Drinks_Frame, text='Hot Coffee', bg='orange', variable=var2, onvalue=1, offvalue=0,
                        font=('Arial', 9, 'normal'), command=chkHotCoffee).grid(row=1, sticky='w')
ColdCoffee = Checkbutton(Drinks_Frame, text='Cold Coffee', bg='orange', variable=var3, onvalue=1, offvalue=0,
                         font=('Arial', 9, 'normal'), command=chkColdCoffee).grid(row=2, sticky='w')
HotChocolate = Checkbutton(Drinks_Frame, text='Hot Chocolate', bg='orange', variable=var4, onvalue=1, offvalue=0,
                           font=('Arial', 9, 'normal'), command=chkHotChocolate).grid(row=3, sticky='w')
Cappuccino = Checkbutton(Drinks_Frame, text='Cappuccino', variable=var5, bg='orange', onvalue=1, offvalue=0,
                         font=('Arial', 9, 'normal'), command=chkCappuccino).grid(row=4, sticky='w')
Tea = Checkbutton(Drinks_Frame, text='Tea', variable=var6, bg='orange', onvalue=1, offvalue=0,
                  font=('Arial', 9, 'normal'), command=chkTea).grid(row=5, sticky='w')
IcedTea = Checkbutton(Drinks_Frame, text='Iced Tea', bg='orange', variable=var7, onvalue=1, offvalue=0,
                      font=('Arial', 9, 'normal'), command=chkIcedTea).grid(row=6, sticky='w')
ChocolateShake_R = Checkbutton(Drinks_Frame, text='Chocolate Shake(Reg)', bg='orange', variable=var8, onvalue=1,
                               offvalue=0, font=('Arial', 9, 'normal'), command=chkChocolateShake_R).grid(row=7,
                                                                                                          sticky='w')
OreoShake_R = Checkbutton(Drinks_Frame, text='Oreo Shake(Reg)', bg='orange', variable=var9, onvalue=1, offvalue=0,
                          font=('Arial', 9, 'normal'), command=chkOreoShake_R).grid(row=8, sticky='w')
StrawberryShake_R = Checkbutton(Drinks_Frame, text='Strawberry Shake(Reg)', bg='orange', variable=var10, onvalue=1,
                                offvalue=0, font=('Arial', 9, 'normal'), command=chkStrawberryShake_R).grid(row=9,
                                                                                                            sticky='w')
PineappleShake_R = Checkbutton(Drinks_Frame, text='Pineapple Shake(Reg)', bg='orange', variable=var11, onvalue=1,
                               offvalue=0, font=('Arial', 9, 'normal'), command=chkPineappleShake_R).grid(row=10,
                                                                                                          sticky='w')
KitkatShake_R = Checkbutton(Drinks_Frame, text='Kitkat Shake(Reg)', bg='orange', variable=var12, onvalue=1, offvalue=0,
                            font=('Arial', 9, 'normal'), command=chkKitkatShake_R).grid(row=11, sticky='w')
ChocolateShake_T = Checkbutton(Drinks_Frame, text='Chocolate Shake(Thick)', bg='orange', variable=var13, onvalue=1,
                               offvalue=0, font=('Arial', 9, 'normal'), command=chkChocolateShake_T).grid(row=12,
                                                                                                          sticky='w')
OreoShake_T = Checkbutton(Drinks_Frame, text='Oreo Shake(Thick)', bg='orange', variable=var14, onvalue=1, offvalue=0,
                          font=('Arial', 9, 'normal'), command=chkOreoShake_T).grid(row=13, sticky='w')
StrawberryShake_T = Checkbutton(Drinks_Frame, text='Strawberry Shake(Thick)', bg='orange', variable=var15, onvalue=1,
                                offvalue=0, font=('Arial', 9, 'normal'), command=chkStrawberryShake_T).grid(row=14,
                                                                                                            sticky='w')
PineappleShake_T = Checkbutton(Drinks_Frame, text='Pineapple Shake(Thick)', bg='orange', variable=var16, onvalue=1,
                               offvalue=0, font=('Arial', 9, 'normal'), command=chkPineappleShake_T).grid(row=15,
                                                                                                          sticky='w')
KitkatShake_T = Checkbutton(Drinks_Frame, text='Kitkat Shake(Thick)', bg='orange', variable=var17, onvalue=1,
                            offvalue=0, font=('Arial', 9, 'normal'), command=chkKitkatShake_T).grid(row=16, sticky='w')
ColdDrink_C = Checkbutton(Drinks_Frame, text='Cold Drink(Canned)', bg='orange', variable=var18, onvalue=1, offvalue=0,
                          font=('Arial', 9, 'normal'), command=chkColdDrink_C).grid(row=17, sticky='w')
ColdDrink_S = Checkbutton(Drinks_Frame, text='Cold Drink(Served)', bg='orange', variable=var19, onvalue=1, offvalue=0,
                          font=('Arial', 9, 'normal'), command=chkColdDrink_S).grid(row=18, sticky='w')
VirginMojito = Checkbutton(Drinks_Frame, text='Virgin Mojito', bg='orange', variable=var20, onvalue=1, offvalue=0,
                           font=('Arial', 9, 'normal'), command=chkVirginMojito).grid(row=19, sticky='w')
MoscowMule = Checkbutton(Drinks_Frame, text='Moscow Mule', bg='orange', variable=var21, onvalue=1, offvalue=0,
                         font=('Arial', 9, 'normal'), command=chkMoscowMule).grid(row=20, sticky='w')
Martini = Checkbutton(Drinks_Frame, text='Martini', bg='orange', variable=var22, onvalue=1, offvalue=0,
                      font=('Arial', 9, 'normal'), command=chkMartini).grid(row=21, sticky='w')
CranberryJuice = Checkbutton(Drinks_Frame, text='Cranberry Juice', bg='orange', variable=var23, onvalue=1, offvalue=0,
                             font=('Arial', 9, 'normal'), command=chkCranberryJuice).grid(row=22, sticky='w')

''' FOOD ITEMS CHECKBUTTONS '''

FrenchFries = Checkbutton(Food_Frame, text='French Fries', bg='orange', variable=var24, onvalue=1, offvalue=0,
                          font=('Arial', 9, 'normal'), command=chkFrenchFries).grid(row=0, sticky='w')
CheeseBalls = Checkbutton(Food_Frame, text='Cheese Balls', bg='orange', variable=var25, onvalue=1, offvalue=0,
                          font=('Arial', 9, 'normal'), command=chkCheeseBalls).grid(row=1, sticky='w')
VegSandwich = Checkbutton(Food_Frame, text='Veg Sandwich', bg='orange', variable=var26, onvalue=1, offvalue=0,
                          font=('Arial', 9, 'normal'), command=chkVegSandwich).grid(row=2, sticky='w')
GrilledSandwich = Checkbutton(Food_Frame, text='Grilled Sandwich', bg='orange', variable=var27, onvalue=1, offvalue=0,
                              font=('Arial', 9, 'normal'), command=chkGrilledSandwich).grid(row=3, sticky='w')
GrilledCheeseSandwich = Checkbutton(Food_Frame, text='Grilled Cheese Sandwich', bg='orange', variable=var28, onvalue=1,
                                    offvalue=0, font=('Arial', 9, 'normal'), command=chkGrilledCheeseSandwich).grid(
    row=4, sticky='w')
PaneerSandwich = Checkbutton(Food_Frame, text='Paneer Sandwich', bg='orange', variable=var29, onvalue=1, offvalue=0,
                             font=('Arial', 9, 'normal'), command=chkPaneerSandwich).grid(row=5, sticky='w')
NutellaSandwich = Checkbutton(Food_Frame, text='Nutella Sandwich', bg='orange', variable=var30, onvalue=1, offvalue=0,
                              font=('Arial', 9, 'normal'), command=chkNutellaSandwich).grid(row=6, sticky='w')
AlooTikkiBurger = Checkbutton(Food_Frame, text='Aloo Tikki Burger', bg='orange', variable=var31, onvalue=1, offvalue=0,
                              font=('Arial', 9, 'normal'), command=chkAlooTikkiBurger).grid(row=7, sticky='w')
VegWhooper = Checkbutton(Food_Frame, text='Veg Whooper', bg='orange', variable=var32, onvalue=1, offvalue=0,
                         font=('Arial', 9, 'normal'), command=chkVegWhooper).grid(row=8, sticky='w')
DoubleCheeseBurger = Checkbutton(Food_Frame, text='Double Cheese Burger', bg='orange', variable=var33, onvalue=1,
                                 offvalue=0, font=('Arial', 9, 'normal'),
                                 command=chkDoubleCheeseBurger).grid(row=9, sticky='w')
PaneerKingBurger = Checkbutton(Food_Frame, text='Paneer King Burger', bg='orange', variable=var34, onvalue=1,
                               offvalue=0, font=('Arial', 9, 'normal'), command=chkPaneerKingBurger).grid(row=10,
                                                                                                          sticky='w')
WhitePasta = Checkbutton(Food_Frame, text='White Pasta', bg='orange', variable=var35, onvalue=1, offvalue=0,
                         font=('Arial', 9, 'normal'), command=chkWhitePasta).grid(row=11, sticky='w')
RedPasta = Checkbutton(Food_Frame, text='Red Pasta', bg='orange', variable=var36, onvalue=1, offvalue=0,
                       font=('Arial', 9, 'normal'), command=chkRedPasta).grid(row=12, sticky='w')
SpecialItalianPasta = Checkbutton(Food_Frame, text='Special Italian Pasta', bg='orange', variable=var37, onvalue=1,
                                  offvalue=0, font=('Arial', 9, 'normal'),
                                  command=chkSpecialItalianPasta).grid(row=13, sticky='w')
MargheritaPizza = Checkbutton(Food_Frame, text='Margherita', bg='orange', variable=var38, onvalue=1, offvalue=0,
                              font=('Arial', 9, 'normal'), command=chkMargheritaPizza).grid(row=14, sticky='w')
SuperVeggiePizza = Checkbutton(Food_Frame, text='Super Veggie Pizza', bg='orange', variable=var39, onvalue=1,
                               offvalue=0, font=('Arial', 9, 'normal'), command=chkSuperVeggiePizza).grid(row=15,
                                                                                                          sticky='w')
PaneerCrispPizza = Checkbutton(Food_Frame, text='Paneer Crisp Pizza', bg='orange', variable=var40, onvalue=1,
                               offvalue=0, font=('Arial', 9, 'normal'), command=chkPaneerCrispPizza).grid(row=16,
                                                                                                          sticky='w')
PeriPeriPaneerPizza = Checkbutton(Food_Frame, text='PeriPeri Paneer Pizza', bg='orange', variable=var41, onvalue=1,
                                  offvalue=0, font=('Arial', 9, 'normal'),
                                  command=chkPeriPeriPaneerPizza).grid(row=17, sticky='w')
ChefSpecialCountryConnectionPizza = Checkbutton(Food_Frame, text='Country Connection Pizza(Chef Special)', bg='orange',
                                                variable=var42, onvalue=1, offvalue=0, font=('Arial', 9, 'normal'),
                                                command=chkChefSpecialCountryConnectionPizza).grid(row=18, sticky='w')
MexicanTacos = Checkbutton(Food_Frame, text='Mexican Tacos', bg='orange', variable=var43, onvalue=1, offvalue=0,
                           font=('Arial', 9, 'normal'), command=chkMexicanTacos).grid(row=19, sticky='w')
PaneerWrap = Checkbutton(Food_Frame, text='Paneer Wrap', bg='orange', variable=var44, onvalue=1, offvalue=0,
                         font=('Arial', 9, 'normal'), command=chkPaneerWrap).grid(row=20, sticky='w')
SpringRoll = Checkbutton(Food_Frame, text='Spring Roll', bg='orange', variable=var45, onvalue=1, offvalue=0,
                         font=('Arial', 9, 'normal'), command=chkSpringRoll).grid(row=21, sticky='w')
PizzaRolls = Checkbutton(Food_Frame, text='Pizza Rolls', bg='orange', variable=var46, onvalue=1, offvalue=0,
                         font=('Arial', 9, 'normal'), command=chkPizzaRolls).grid(row=22, sticky='w')

''' PACKED FOOD ITEM CHECKBUTTONS '''

Lays = Checkbutton(Packed_Food, text='Lays', bg='orange', variable=var47, onvalue=1, offvalue=0,
                   font=('Arial', 9, 'normal'), command=chkLays).grid(row=0, sticky='w')
Kurkure = Checkbutton(Packed_Food, text='Kurkure', bg='orange', variable=var48, onvalue=1, offvalue=0,
                      font=('Arial', 9, 'normal'), command=chkKurkure).grid(row=1, sticky='w')
Bingo = Checkbutton(Packed_Food, text='Bingo', bg='orange', variable=var49, onvalue=1, offvalue=0,
                    font=('Arial', 9, 'normal'), command=chkBingo).grid(row=2, sticky='w')
Nutella = Checkbutton(Packed_Food, text='Nutella', bg='orange', variable=var50, onvalue=1, offvalue=0,
                      font=('Arial', 9, 'normal'), command=chkNutella).grid(row=3, sticky='w')
HersheysChocolateSyrup = Checkbutton(Packed_Food, text="Hershey's Chocolate Syrup", bg='orange', variable=var51,
                                     onvalue=1, offvalue=0, font=('Arial', 9, 'normal'),
                                     command=chkHersheysChocolateSyrup).grid(row=4, sticky='w')
Bhujia = Checkbutton(Packed_Food, text='Bikaji Bhujia', bg='orange', variable=var52, onvalue=1, offvalue=0,
                     font=('Arial', 9, 'normal'), command=chkBhujia).grid(row=5, sticky='w')
Mixture = Checkbutton(Packed_Food, text="Haldiram's Mixture", bg='orange', variable=var53, onvalue=1, offvalue=0,
                      font=('Arial', 9, 'normal'), command=chkMixture).grid(row=6, sticky='w')
SoyaStix = Checkbutton(Packed_Food, text='Soya Stix', bg='orange', variable=var54, onvalue=1, offvalue=0,
                       font=('Arial', 9, 'normal'), command=chkSoyaStix).grid(row=7, sticky='w')
BrittaniaMarieGold = Checkbutton(Packed_Food, text='Brittania Marie Gold', bg='orange', variable=var55, onvalue=1,
                                 offvalue=0, font=('Arial', 9, 'normal'),
                                 command=chkBrittaniaMarieGold).grid(row=8, sticky='w')
_5050_ = Checkbutton(Packed_Food, text='50-50 Maska Chaska', bg='orange', variable=var56, onvalue=1, offvalue=0,
                     font=('Arial', 9, 'normal'), command=chk5050).grid(row=9, sticky='w')
Oreo = Checkbutton(Packed_Food, text='Oreo', bg='orange', variable=var57, onvalue=1, offvalue=0,
                   font=('Arial', 9, 'normal'), command=chkOreo).grid(row=10, sticky='w')
HideandSeek = Checkbutton(Packed_Food, text='Hide & Seek', bg='orange', variable=var58, onvalue=1, offvalue=0,
                          font=('Arial', 9, 'normal'), command=chkHideandSeek).grid(row=11, sticky='w')
DarkFantasy = Checkbutton(Packed_Food, text='Dark Fantasy', bg='orange', variable=var59, onvalue=1, offvalue=0,
                          font=('Arial', 9, 'normal'), command=chkDarkFantasy).grid(row=12, sticky='w')
KinderJoy = Checkbutton(Packed_Food, text='Kinder Joy', bg='orange', variable=var60, onvalue=1, offvalue=0,
                        font=('Arial', 9, 'normal'), command=chkKinderJoy).grid(row=13, sticky='w')
Nachos = Checkbutton(Packed_Food, text='Nachos', bg='orange', variable=var61, onvalue=1, offvalue=0,
                     font=('Arial', 9, 'normal'), command=chkNachos).grid(row=14, sticky='w')
Bournvita = Checkbutton(Packed_Food, text='Bournvita', bg='orange', variable=var62, onvalue=1, offvalue=0,
                        font=('Arial', 9, 'normal'), command=chkBournvita).grid(row=15, sticky='w')
Complan = Checkbutton(Packed_Food, text='Complan', bg='orange', variable=var63, onvalue=1, offvalue=0,
                      font=('Arial', 9, 'normal'), command=chkComplan).grid(row=16, sticky='w')
KellogsChocos = Checkbutton(Packed_Food, text="Kellog's Chocos", bg='orange', variable=var64, onvalue=1, offvalue=0,
                            font=('Arial', 9, 'normal'), command=chkKellogsChocos).grid(row=17, sticky='w')
Rusk = Checkbutton(Packed_Food, text='Rusk', bg='orange', variable=var65, onvalue=1, offvalue=0,
                   font=('Arial', 9, 'normal'), command=chkRusk).grid(row=18, sticky='w')
DairyMilkSilk = Checkbutton(Packed_Food, text='Dairy Milk Silk', bg='orange', variable=var66, onvalue=1, offvalue=0,
                            font=('Arial', 9, 'normal'), command=chkDairyMilkSilk).grid(row=19, sticky='w')
HersheysWhiteCocoaChocolate = Checkbutton(Packed_Food, text="Hershey's White Cocoa Chocolate", bg='orange',
                                          variable=var67, onvalue=1, offvalue=0, font=('Arial', 9, 'normal'),
                                          command=chkHersheysWhiteCocoaChocolate).grid(row=20, sticky='w')
NestlesDarkSensation = Checkbutton(Packed_Food, text="Nestle's Dark Sensation", bg='orange', variable=var68, onvalue=1,
                                   offvalue=0, font=('Arial', 9, 'normal'), command=chkNestlesDarkSensation).grid(
    row=21, sticky='w')
Pedigree = Checkbutton(Packed_Food, text='Pedigree', bg='orange', variable=var69, onvalue=1, offvalue=0,
                       font=('Arial', 9, 'normal'), command=chkPedigree).grid(row=22, sticky='w')

''' DRINKS ENTRIES '''

TXT_MineralWater = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                         textvariable=EV_MineralWater)
TXT_MineralWater.grid(row=0, column=1, sticky='e')
TXT_HotCoffee = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                      textvariable=EV_HotCoffee)
TXT_HotCoffee.grid(row=1, column=1, sticky='e')
TXT_ColdCoffee = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                       textvariable=EV_ColdCoffee)
TXT_ColdCoffee.grid(row=2, column=1, sticky='e')
TXT_HotChocolate = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                         textvariable=EV_HotChocolate)
TXT_HotChocolate.grid(row=3, column=1, sticky='e')
TXT_Cappuccino = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                       textvariable=EV_Cappuccino)
TXT_Cappuccino.grid(row=4, column=1, sticky='e')
TXT_Tea = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                textvariable=EV_Tea)
TXT_Tea.grid(row=5, column=1, sticky='e')
TXT_IcedTea = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                    textvariable=EV_IcedTea)
TXT_IcedTea.grid(row=6, column=1, sticky='e')
TXT_ChocolateShake_R = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                             textvariable=EV_ChocolateShake_R)
TXT_ChocolateShake_R.grid(row=7, column=1, sticky='e')
TXT_OreoShake_R = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                        textvariable=EV_OreoShake_R)
TXT_OreoShake_R.grid(row=8, column=1, sticky='e')
TXT_StrawberryShake_R = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                              textvariable=EV_StrawberryShake_R)
TXT_StrawberryShake_R.grid(row=9, column=1, sticky='e')
TXT_PineappleShake_R = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                             textvariable=EV_PineappleShake_R)
TXT_PineappleShake_R.grid(row=10, column=1, sticky='e')
TXT_KitkatShake_R = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                          textvariable=EV_KitkatShake_R)
TXT_KitkatShake_R.grid(row=11, column=1, sticky='e')
TXT_ChocolateShake_T = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                             textvariable=EV_ChocolateShake_T)
TXT_ChocolateShake_T.grid(row=12, column=1, sticky='e')
TXT_OreoShake_T = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                        textvariable=EV_OreoShake_T)
TXT_OreoShake_T.grid(row=13, column=1, sticky='e')
TXT_StrawberryShake_T = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                              textvariable=EV_StrawberryShake_T)
TXT_StrawberryShake_T.grid(row=14, column=1, sticky='e')
TXT_PineappleShake_T = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                             textvariable=EV_PineappleShake_T)
TXT_PineappleShake_T.grid(row=15, column=1, sticky='e')
TXT_KitkatShake_T = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                          textvariable=EV_KitkatShake_T)
TXT_KitkatShake_T.grid(row=16, column=1, sticky='e')
TXT_ColdDrink_C = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                        textvariable=EV_ColdDrink_C)
TXT_ColdDrink_C.grid(row=17, column=1, sticky='e')
TXT_ColdDrink_S = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                        textvariable=EV_ColdDrink_S)
TXT_ColdDrink_S.grid(row=18, column=1, sticky='e')
TXT_VirginMojito = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                         textvariable=EV_VirginMojito)
TXT_VirginMojito.grid(row=19, column=1, sticky='e')
TXT_MoscowMule = Entry(Drinks_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                       textvariable=EV_MoscowMule)
TXT_MoscowMule.grid(row=20, column=1, sticky='e')
TXT_Martini = Entry(Drinks_Frame, font=('Arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                    textvariable=EV_Martini)
TXT_Martini.grid(row=21, column=1, sticky='e')
TXT_CranberryJuice = Entry(Drinks_Frame, font=('Arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                           textvariable=EV_CranberryJuice)
TXT_CranberryJuice.grid(row=22, column=1, sticky='e')

''' FOOD ITEMS ENTRIES '''

TXT_FrenchFries = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                        textvariable=EV_FrenchFries)
TXT_FrenchFries.grid(row=0, column=1, sticky='e')
TXT_CheeseBalls = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                        textvariable=EV_CheeseBalls)
TXT_CheeseBalls.grid(row=1, column=1, sticky='e')
TXT_VegSandwich = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                        textvariable=EV_VegSandwich)
TXT_VegSandwich.grid(row=2, column=1, sticky='e')
TXT_GrilledSandwich = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                            textvariable=EV_GrilledSandwich)
TXT_GrilledSandwich.grid(row=3, column=1, sticky='e')
TXT_GrilledCheeseSandwich = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left',
                                  state='disabled', textvariable=EV_GrilledCheeseSandwich)
TXT_GrilledCheeseSandwich.grid(row=4, column=1, sticky='e')
TXT_PaneerSandwich = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                           textvariable=EV_PaneerSandwich)
TXT_PaneerSandwich.grid(row=5, column=1, sticky='e')
TXT_NutellaSandwich = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                            textvariable=EV_NutellaSandwich)
TXT_NutellaSandwich.grid(row=6, column=1, sticky='e')
TXT_AlooTikkiBurger = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                            textvariable=EV_AlooTikkiBurger)
TXT_AlooTikkiBurger.grid(row=7, column=1, sticky='e')
TXT_VegWhooper = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                       textvariable=EV_VegWhooper)
TXT_VegWhooper.grid(row=8, column=1, sticky='e')
TXT_DoubleCheeseBurger = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                               textvariable=EV_DoubleCheeseBurger)
TXT_DoubleCheeseBurger.grid(row=9, column=1, sticky='e')
TXT_PaneerKingBurger = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                             textvariable=EV_PaneerKingBurger)
TXT_PaneerKingBurger.grid(row=10, column=1, sticky='e')
TXT_WhitePasta = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                       textvariable=EV_WhitePasta)
TXT_WhitePasta.grid(row=11, column=1, sticky='e')
TXT_RedPasta = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                     textvariable=EV_RedPasta)
TXT_RedPasta.grid(row=12, column=1, sticky='e')
TXT_SpecialItalianPasta = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                                textvariable=EV_SpecialItalianPasta)
TXT_SpecialItalianPasta.grid(row=13, column=1, sticky='e')
TXT_MargheritaPizza = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                            textvariable=EV_MargheritaPizza)
TXT_MargheritaPizza.grid(row=14, column=1, sticky='e')
TXT_SuperVeggiePizza = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                             textvariable=EV_SuperVeggiePizza)
TXT_SuperVeggiePizza.grid(row=15, column=1, sticky='e')
TXT_PaneerCrispPizza = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                             textvariable=EV_PaneerCrispPizza)
TXT_PaneerCrispPizza.grid(row=16, column=1, sticky='e')
TXT_PeriPeriPaneerPizza = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                                textvariable=EV_PeriPeriPaneerPizza)
TXT_PeriPeriPaneerPizza.grid(row=17, column=1, sticky='e')
TXT_ChefSpecialCountryConnectionPizza = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left',
                                              state='disabled', textvariable=EV_ChefSpecialCountryConnectionPizza)
TXT_ChefSpecialCountryConnectionPizza.grid(row=18, column=1, sticky='e')
TXT_MexicanTacos = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                         textvariable=EV_MexicanTacos)
TXT_MexicanTacos.grid(row=19, column=1, sticky='e')
TXT_PaneerWrap = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                       textvariable=EV_PaneerWrap)
TXT_PaneerWrap.grid(row=20, column=1, sticky='e')
TXT_SpringRoll = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                       textvariable=EV_SpringRoll)
TXT_SpringRoll.grid(row=21, column=1, sticky='e')
TXT_PizzaRolls = Entry(Food_Frame, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                       textvariable=EV_PizzaRolls)
TXT_PizzaRolls.grid(row=22, column=1, sticky='e')

''' PACKED FOOD ITEMS ENTRIES '''

TXT_Lays = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                 textvariable=EV_Lays)
TXT_Lays.grid(row=0, column=1, sticky='e')
TXT_Kurkure = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                    textvariable=EV_Kurkure)
TXT_Kurkure.grid(row=1, column=1, sticky='e')
TXT_Bingo = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                  textvariable=EV_Bingo)
TXT_Bingo.grid(row=2, column=1, sticky='e')
TXT_Nutella = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                    textvariable=EV_Nutella)
TXT_Nutella.grid(row=3, column=1, sticky='e')
TXT_HersheysChocolateSyrup = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left',
                                   state='disabled', textvariable=EV_HersheysChocolateSyrup)
TXT_HersheysChocolateSyrup.grid(row=4, column=1, sticky='e')
TXT_Bhujia = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                   textvariable=EV_Bhujia)
TXT_Bhujia.grid(row=5, column=1, sticky='e')
TXT_Mixture = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                    textvariable=EV_Mixture)
TXT_Mixture.grid(row=6, column=1, sticky='e')
TXT_SoyaStix = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                     textvariable=EV_SoyaStix)
TXT_SoyaStix.grid(row=7, column=1, sticky='e')
TXT_BrittaniaMarieGold = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                               textvariable=EV_BrittaniaMarieGold)
TXT_BrittaniaMarieGold.grid(row=8, column=1, sticky='e')
TXT_5050 = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                 textvariable=EV_5050)
TXT_5050.grid(row=9, column=1, sticky='e')
TXT_Oreo = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                 textvariable=EV_Oreo)
TXT_Oreo.grid(row=10, column=1, sticky='e')
TXT_HideandSeek = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                        textvariable=EV_HideandSeek)
TXT_HideandSeek.grid(row=11, column=1, sticky='e')
TXT_DarkFantasy = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                        textvariable=EV_DarkFantasy)
TXT_DarkFantasy.grid(row=12, column=1, sticky='e')
TXT_KinderJoy = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                      textvariable=EV_KinderJoy)
TXT_KinderJoy.grid(row=13, column=1, sticky='e')
TXT_Nachos = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                   textvariable=EV_Nachos)
TXT_Nachos.grid(row=14, column=1, sticky='e')
TXT_Bournvita = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                      textvariable=EV_Bournvita)
TXT_Bournvita.grid(row=15, column=1, sticky='e')
TXT_Complan = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                    textvariable=EV_Complan)
TXT_Complan.grid(row=16, column=1, sticky='e')
TXT_KellogsChocos = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                          textvariable=EV_KellogsChocos)
TXT_KellogsChocos.grid(row=17, column=1, sticky='e')
TXT_Rusk = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                 textvariable=EV_Rusk)
TXT_Rusk.grid(row=18, column=1, sticky='e')
TXT_DairyMilkSilk = Entry(Packed_Food, font=('Arial', 8, 'normal'), bd=2, width=3, justify='left', state='disabled',
                          textvariable=EV_DairyMilkSilk)
TXT_DairyMilkSilk.grid(row=19, column=1, sticky='e')
TXT_HersheysWhiteCocoaChocolate = Entry(Packed_Food, font=('Arial', 8, 'normal'), bd=2, width=3, justify='left',
                                        state='disabled', textvariable=EV_HersheysWhiteCocoaChocolate)
TXT_HersheysWhiteCocoaChocolate.grid(row=20, column=1, sticky='e')
TXT_NestlesDarkSensation = Entry(Packed_Food, font=('Arial', 8, 'normal'), bd=2, width=3, justify='left',
                                 state='disabled', textvariable=EV_NestlesDarkSensation)
TXT_NestlesDarkSensation.grid(row=21, column=1, sticky='e')
TXT_Pedigree = Entry(Packed_Food, font=('arial', 8, 'bold'), bd=2, width=3, justify='left', state='disabled',
                     textvariable=EV_Pedigree)
TXT_Pedigree.grid(row=22, column=1, sticky='e')

############################################## COST FRAME LABELS ##############################################
################################################# AND ENTRIES #################################################

''' LABELS '''

LBL_CostofDrinks = Label(Cost_Frame, font=('Arial', 10, 'bold'), bg='orange', text='Cost of Drinks')
LBL_CostofDrinks.grid(row=0, column=1, sticky='w')
LBL_CostofDrinks.grid_rowconfigure(0, weight=1)
LBL_CostofDrinks.grid_columnconfigure(1, weight=1)

LBL_CostofFood = Label(Cost_Frame, font=('Arial', 10, 'bold'), bg='orange', text='Cost of Food')
LBL_CostofFood.grid(row=1, column=1, sticky='w')
LBL_CostofFood.grid_columnconfigure(1, weight=1)
LBL_CostofFood.grid_rowconfigure(1, weight=1)

LBL_CostofPacked = Label(Cost_Frame, font=('Arial', 10, 'bold'), bg='orange', text='Cost of Packed Food Items')
LBL_CostofPacked.grid(row=2, column=1, sticky='w', rowspan=9)
LBL_CostofPacked.grid_rowconfigure(2, weight=1)
LBL_CostofPacked.grid_columnconfigure(1, weight=1)

LBL_GST = Label(Cost_Frame, font=('Arial', 10, 'bold'), bg='orange', text='\tGST')
LBL_GST.grid(row=0, column=3, sticky='w')
LBL_GST.grid_columnconfigure(3, weight=1)
LBL_GST.grid_rowconfigure(0, weight=1)

LBL_ServiceCharge = Label(Cost_Frame, font=('Arial', 10, 'bold'), bg='orange', text='\tService Charges')
LBL_ServiceCharge.grid(row=1, column=3, sticky='w')
LBL_ServiceCharge.grid_columnconfigure(3, weight=1)
LBL_ServiceCharge.grid_rowconfigure(1, weight=1)

LBL_TotalCost = Label(Cost_Frame, font=('Arial', 10, 'bold'), bg='orange', text='\tTotal Cost')
LBL_TotalCost.grid(row=2, column=3, sticky='w')
LBL_TotalCost.grid_columnconfigure(3, weight=1)
LBL_TotalCost.grid_rowconfigure(2, weight=1)

''' ENTRIES '''

TXT_CostofDrinks = Entry(Cost_Frame, font=('Arial', 9, 'normal'), bg='#feca5f', bd=2, insertwidth=2, justify='right',
                         textvariable=EV_CostofDrinks)
TXT_CostofDrinks.grid(row=0, column=2, sticky='e')
TXT_CostofDrinks.grid_columnconfigure(2, weight=1)
TXT_CostofDrinks.grid_rowconfigure(0, weight=1)

TXT_CostofFood = Entry(Cost_Frame, font=('Arial', 9, 'normal'), bg='#feca5f', bd=2, insertwidth=2, justify='right',
                       textvariable=EV_CostofFood)
TXT_CostofFood.grid(row=1, column=2, sticky='e')
TXT_CostofFood.grid_rowconfigure(1, weight=1)
TXT_CostofFood.grid_columnconfigure(2, weight=1)

TXT_CostofPacked = Entry(Cost_Frame, font=('Arial', 9, 'normal'), bg='#feca5f', bd=2, insertwidth=2, justify='right',
                         textvariable=EV_CostofPackedFood)
TXT_CostofPacked.grid(row=2, column=2, sticky='e')
TXT_CostofPacked.grid_columnconfigure(2, weight=1)
TXT_CostofPacked.grid_rowconfigure(2, weight=1)

TXT_GST = Entry(Cost_Frame, font=('Arial', 9, 'normal'), bg='#feca5f', bd=2, insertwidth=2, justify='right',
                textvariable=EV_GST)
TXT_GST.grid(row=0, column=5, sticky='e')
TXT_GST.grid_columnconfigure(5, weight=1)
TXT_GST.grid_rowconfigure(0, weight=1)

TXT_ServiceCharge = Entry(Cost_Frame, font=('Arial', 9, 'normal'), bg='#feca5f', bd=2, insertwidth=2, justify='right',
                          textvariable=EV_ServiceCharge)
TXT_ServiceCharge.grid(row=1, column=5, sticky='e')
TXT_ServiceCharge.grid_columnconfigure(5, weight=1)
TXT_ServiceCharge.grid_rowconfigure(1, weight=1)

TXT_TotalCost = Entry(Cost_Frame, font=('Arial', 9, 'normal'), bg='#feca5f', bd=2, insertwidth=2, justify='right',
                      textvariable=EV_TotalCost)
TXT_TotalCost.grid(row=2, column=5, sticky='e')
TXT_TotalCost.grid_columnconfigure(5, weight=1)
TXT_TotalCost.grid_rowconfigure(2, weight=1)

TXT_Receipt = Text(Receipt_Frame, width=46, height=43, bg='white', bd=3, font=('arial', 8, 'normal'), state='normal')
TXT_Receipt.grid(row=0, column=0)
TXT_Receipt.grid_columnconfigure(0, weight=1)
TXT_Receipt.grid_rowconfigure(0, weight=1)


############################################### RECEIPT BUTTON ###############################################
################################################## FUNCTIONS #################################################

def Exit():
    ques = tkmb.askyesno('Warning', 'Do you really want to exit?')
    if ques > 0:
        root.destroy()
    else:
        return


def Reset():
    EV_GST.set('')
    EV_TotalCost.set('')
    EV_CostofDrinks.set('')
    EV_CostofFood.set('')
    EV_CostofPackedFood.set('')
    EV_ServiceCharge.set('')
    TXT_Receipt.configure(state='normal')
    TXT_Receipt.delete('1.0', END)
    Text_Receipt_initial()

    EV_MineralWater.set('0')
    EV_HotCoffee.set('0')
    EV_ColdCoffee.set('0')
    EV_HotChocolate.set('0')
    EV_Cappuccino.set('0')
    EV_Tea.set('0')
    EV_IcedTea.set('0')
    EV_ChocolateShake_R.set('0')
    EV_OreoShake_R.set('0')
    EV_StrawberryShake_R.set('0')
    EV_PineappleShake_R.set('0')
    EV_KitkatShake_R.set('0')
    EV_ChocolateShake_T.set('0')
    EV_OreoShake_T.set('0')
    EV_StrawberryShake_T.set('0')
    EV_PineappleShake_T.set('0')
    EV_KitkatShake_T.set('0')
    EV_ColdDrink_C.set('0')
    EV_ColdDrink_S.set('0')
    EV_VirginMojito.set('0')
    EV_MoscowMule.set('0')
    EV_Martini.set('0')
    EV_CranberryJuice.set('0')

    EV_FrenchFries.set('0')
    EV_CheeseBalls.set('0')
    EV_VegSandwich.set('0')
    EV_GrilledSandwich.set('0')
    EV_GrilledCheeseSandwich.set('0')
    EV_PaneerSandwich.set('0')
    EV_NutellaSandwich.set('0')
    EV_AlooTikkiBurger.set('0')
    EV_VegWhooper.set('0')
    EV_DoubleCheeseBurger.set('0')
    EV_PaneerKingBurger.set('0')
    EV_WhitePasta.set('0')
    EV_RedPasta.set('0')
    EV_SpecialItalianPasta.set('0')
    EV_MargheritaPizza.set('0')
    EV_SuperVeggiePizza.set('0')
    EV_PaneerCrispPizza.set('0')
    EV_PeriPeriPaneerPizza.set('0')
    EV_ChefSpecialCountryConnectionPizza.set('0')
    EV_MexicanTacos.set('0')
    EV_PaneerWrap.set('0')
    EV_SpringRoll.set('0')
    EV_PizzaRolls.set('0')

    EV_Lays.set('0')
    EV_Kurkure.set('0')
    EV_Bingo.set('0')
    EV_Nutella.set('0')
    EV_HersheysChocolateSyrup.set('0')
    EV_Bhujia.set('0')
    EV_Mixture.set('0')
    EV_SoyaStix.set('0')
    EV_BrittaniaMarieGold.set('0')
    EV_5050.set('0')
    EV_Oreo.set('0')
    EV_HideandSeek.set('0')
    EV_DarkFantasy.set('0')
    EV_KinderJoy.set('0')
    EV_Nachos.set('0')
    EV_Bournvita.set('0')
    EV_Complan.set('0')
    EV_KellogsChocos.set('0')
    EV_Rusk.set('0')
    EV_NestlesDarkSensation.set('0')
    EV_DairyMilkSilk.set('0')
    EV_HersheysWhiteCocoaChocolate.set('0')
    EV_Pedigree.set('0')

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
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)
    var31.set(0)
    var32.set(0)
    var33.set(0)
    var34.set(0)
    var35.set(0)
    var36.set(0)
    var37.set(0)
    var38.set(0)
    var39.set(0)
    var40.set(0)
    var41.set(0)
    var42.set(0)
    var43.set(0)
    var44.set(0)
    var45.set(0)
    var46.set(0)
    var47.set(0)
    var48.set(0)
    var49.set(0)
    var50.set(0)
    var51.set(0)
    var52.set(0)
    var53.set(0)
    var54.set(0)
    var55.set(0)
    var56.set(0)
    var57.set(0)
    var58.set(0)
    var59.set(0)
    var60.set(0)
    var61.set(0)
    var62.set(0)
    var63.set(0)
    var64.set(0)
    var65.set(0)
    var66.set(0)
    var67.set(0)
    var68.set(0)
    var69.set(0)

    TXT_MineralWater.configure(state='disabled')
    TXT_HotCoffee.configure(state='disabled')
    TXT_ColdCoffee.configure(state='disabled')
    TXT_HotChocolate.configure(state='disabled')
    TXT_Cappuccino.configure(state='disabled')
    TXT_Tea.configure(state='disabled')
    TXT_IcedTea.configure(state='disabled')
    TXT_ChocolateShake_R.configure(state='disabled')
    TXT_OreoShake_R.configure(state='disabled')
    TXT_StrawberryShake_R.configure(state='disabled')
    TXT_PineappleShake_R.configure(state='disabled')
    TXT_KitkatShake_R.configure(state='disabled')
    TXT_ChocolateShake_T.configure(state='disabled')
    TXT_OreoShake_T.configure(state='disabled')
    TXT_StrawberryShake_T.configure(state='disabled')
    TXT_PineappleShake_T.configure(state='disabled')
    TXT_KitkatShake_T.configure(state='disabled')
    TXT_ColdDrink_C.configure(state='disabled')
    TXT_ColdDrink_S.configure(state='disabled')
    TXT_VirginMojito.configure(state='disabled')
    TXT_MoscowMule.configure(state='disabled')
    TXT_Martini.configure(state='disabled')
    TXT_CranberryJuice.configure(state='disabled')

    TXT_FrenchFries.configure(state='disabled')
    TXT_CheeseBalls.configure(state='disabled')
    TXT_VegSandwich.configure(state='disabled')
    TXT_GrilledSandwich.configure(state='disabled')
    TXT_GrilledCheeseSandwich.configure(state='disabled')
    TXT_PaneerSandwich.configure(state='disabled')
    TXT_NutellaSandwich.configure(state='disabled')
    TXT_AlooTikkiBurger.configure(state='disabled')
    TXT_VegWhooper.configure(state='disabled')
    TXT_DoubleCheeseBurger.configure(state='disabled')
    TXT_PaneerKingBurger.configure(state='disabled')
    TXT_WhitePasta.configure(state='disabled')
    TXT_RedPasta.configure(state='disabled')
    TXT_SpecialItalianPasta.configure(state='disabled')
    TXT_MargheritaPizza.configure(state='disabled')
    TXT_SuperVeggiePizza.configure(state='disabled')
    TXT_PaneerCrispPizza.configure(state='disabled')
    TXT_PeriPeriPaneerPizza.configure(state='disabled')
    TXT_ChefSpecialCountryConnectionPizza.configure(state='disabled')
    TXT_MexicanTacos.configure(state='disabled')
    TXT_PaneerWrap.configure(state='disabled')
    TXT_SpringRoll.configure(state='disabled')
    TXT_PizzaRolls.configure(state='disabled')

    TXT_Lays.configure(state='disabled')
    TXT_Kurkure.configure(state='disabled')
    TXT_Bingo.configure(state='disabled')
    TXT_Nutella.configure(state='disabled')
    TXT_HersheysChocolateSyrup.configure(state='disabled')
    TXT_Bhujia.configure(state='disabled')
    TXT_Mixture.configure(state='disabled')
    TXT_SoyaStix.configure(state='disabled')
    TXT_BrittaniaMarieGold.configure(state='disabled')
    TXT_5050.configure(state='disabled')
    TXT_Oreo.configure(state='disabled')
    TXT_HideandSeek.configure(state='disabled')
    TXT_DarkFantasy.configure(state='disabled')
    TXT_KinderJoy.configure(state='disabled')
    TXT_Nachos.configure(state='disabled')
    TXT_Bournvita.configure(state='disabled')
    TXT_Complan.configure(state='disabled')
    TXT_KellogsChocos.configure(state='disabled')
    TXT_Rusk.configure(state='disabled')
    TXT_DairyMilkSilk.configure(state='disabled')
    TXT_HersheysWhiteCocoaChocolate.configure(state='disabled')
    TXT_NestlesDarkSensation.configure(state='disabled')
    TXT_Pedigree.configure(state='disabled')

    x = random.randint(10010010, 999999999)
    RandomRefNo = str(x)


def Total_Cost():
    global Item1, Item2, Item3, Item4, Item5, Item6, Item7, Item8, Item9, Item10, Item11, Item12, Item13, Item14, Item15, Item16, Item17, Item18, Item19, Item20, Item21, Item22, Item23, Item24, Item25, Item27, Item26, Item28, Item29, Item30, Item31, Item32, Item33, Item34, Item35, Item36, Item37, Item38, Item39, Item40, Item41, Item42, Item43, Item44, Item45, Item46, Item47, Item48, Item49, Item50, Item51, Item52, Item53, Item54, Item55, Item56, Item57, Item58, Item59, Item60, Item62, Item61, Item63, Item64, Item65, Item66, Item67, Item68, Item69
    global GST, ServiceCharge, PriceofDrinks, PriceofFood, PriceofPackedFood
    global TotalCost
    Item1 = float(EV_MineralWater.get())
    Item2 = float(EV_HotCoffee.get())
    Item3 = float(EV_ColdCoffee.get())
    Item4 = float(EV_HotChocolate.get())
    Item5 = float(EV_Cappuccino.get())
    Item6 = float(EV_Tea.get())
    Item7 = float(EV_IcedTea.get())
    Item8 = float(EV_ChocolateShake_R.get())
    Item9 = float(EV_OreoShake_R.get())
    Item10 = float(EV_StrawberryShake_R.get())
    Item11 = float(EV_PineappleShake_R.get())
    Item12 = float(EV_KitkatShake_R.get())
    Item13 = float(EV_ChocolateShake_T.get())
    Item14 = float(EV_OreoShake_T.get())
    Item15 = float(EV_StrawberryShake_T.get())
    Item16 = float(EV_PineappleShake_T.get())
    Item17 = float(EV_KitkatShake_T.get())
    Item18 = float(EV_ColdDrink_C.get())
    Item19 = float(EV_ColdDrink_S.get())
    Item20 = float(EV_VirginMojito.get())
    Item21 = float(EV_MoscowMule.get())
    Item22 = float(EV_Martini.get())
    Item23 = float(EV_CranberryJuice.get())
    Item24 = float(EV_FrenchFries.get())
    Item25 = float(EV_CheeseBalls.get())
    Item26 = float(EV_VegSandwich.get())
    Item27 = float(EV_GrilledSandwich.get())
    Item28 = float(EV_GrilledCheeseSandwich.get())
    Item29 = float(EV_PaneerSandwich.get())
    Item30 = float(EV_NutellaSandwich.get())
    Item31 = float(EV_AlooTikkiBurger.get())
    Item32 = float(EV_VegWhooper.get())
    Item33 = float(EV_DoubleCheeseBurger.get())
    Item34 = float(EV_PaneerKingBurger.get())
    Item35 = float(EV_WhitePasta.get())
    Item36 = float(EV_RedPasta.get())
    Item37 = float(EV_SpecialItalianPasta.get())
    Item38 = float(EV_MargheritaPizza.get())
    Item39 = float(EV_SuperVeggiePizza.get())
    Item40 = float(EV_PaneerCrispPizza.get())
    Item41 = float(EV_PeriPeriPaneerPizza.get())
    Item42 = float(EV_ChefSpecialCountryConnectionPizza.get())
    Item43 = float(EV_MexicanTacos.get())
    Item44 = float(EV_PaneerWrap.get())
    Item45 = float(EV_SpringRoll.get())
    Item46 = float(EV_PizzaRolls.get())
    Item47 = float(EV_Lays.get())
    Item48 = float(EV_Kurkure.get())
    Item49 = float(EV_Bingo.get())
    Item50 = float(EV_Nutella.get())
    Item51 = float(EV_HersheysChocolateSyrup.get())
    Item52 = float(EV_Bhujia.get())
    Item53 = float(EV_Mixture.get())
    Item54 = float(EV_SoyaStix.get())
    Item55 = float(EV_BrittaniaMarieGold.get())
    Item56 = float(EV_5050.get())
    Item57 = float(EV_Oreo.get())
    Item58 = float(EV_HideandSeek.get())
    Item59 = float(EV_DarkFantasy.get())
    Item60 = float(EV_KinderJoy.get())
    Item61 = float(EV_Nachos.get())
    Item62 = float(EV_Bournvita.get())
    Item63 = float(EV_Complan.get())
    Item64 = float(EV_KellogsChocos.get())
    Item65 = float(EV_Rusk.get())
    Item66 = float(EV_DairyMilkSilk.get())
    Item67 = float(EV_HersheysWhiteCocoaChocolate.get())
    Item68 = float(EV_NestlesDarkSensation.get())
    Item69 = float(EV_Pedigree.get())

    CostofDrinks = (Item1 * 15) + (Item2 * 30) + (Item3 * 45) + (Item4 * 45) + (Item5 * 50) + (Item6 * 10) + (
                Item7 * 60) + (Item8 * 75) + (Item9 * 95) + (Item10 * 75) + (Item11 * 70) + (Item12 * 95) + (
                               Item13 * 100) + (Item14 * 130) + (Item15 * 100) + (Item16 * 95) + (Item17 * 130) + (
                               Item18 * 35) + (Item19 * 45) + (Item20 * 120) + (Item21 * 140) + (Item22 * 130) + (
                               Item23 * 140)
    CostofFood = (Item24 * 60) + (Item25 * 50) + (Item26 * 50) + (Item27 * 75) + (Item28 * 90) + (Item29 * 75) + (
                Item30 * 120) + (Item31 * 35) + (Item32 * 45) + (Item33 * 50) + (Item34 * 75) + (Item35 * 110) + (
                             Item36 * 110) + (Item37 * 130) + (Item38 * 120) + (Item39 * 130) + (Item40 * 150) + (
                             Item41 * 200) + (Item42 * 250) + (Item43 * 45) + (Item44 * 75) + (Item45 * 60) + (
                             Item46 * 90)
    CostofPackedFood = (Item47 * 20) + (Item48 * 20) + (Item49 * 20) + (Item50 * 750) + (Item51 * 320) + (
                Item52 * 45) + (Item53 * 60) + (Item54 * 30) + (Item55 * 30) + (Item56 * 10) + (Item57 * 30) + (
                                   Item58 * 30) + (Item59 * 40) + (Item60 * 40) + (Item61 * 35) + (Item62 * 400) + (
                                   Item63 * 225) + (Item64 * 300) + (Item65 * 65) + (Item66 * 75) + (Item67 * 290) + (
                                   Item68 * 100) + (Item69 * 260)

    if (CostofDrinks == 0) and (CostofFood == 0) and (CostofPackedFood != 0):

        PriceofDrinks = u"\u20B9", str('%.2f' % CostofDrinks)
        PriceofFood = u"\u20B9", str('%.2f' % CostofFood)
        PriceofPackedFood = u"\u20B9", str('%.2f' % CostofPackedFood)

        EV_CostofDrinks.set(PriceofDrinks)
        EV_CostofFood.set(PriceofFood)
        EV_CostofPackedFood.set(PriceofPackedFood)

        ServiceCharge = u"\u20B9", str('%.2f' % 0)
        EV_ServiceCharge.set(ServiceCharge)

        GST = u"\u20B9", str('%.2f' % 0)
        EV_GST.set(GST)

        TotalTax = ((CostofDrinks + CostofFood + CostofPackedFood + 0) * 0)
        TotalCost = u"\u20B9", str('%.2f' % (CostofDrinks + CostofFood + CostofPackedFood + 0 + TotalTax))
        EV_TotalCost.set(TotalCost)

    else:
        PriceofDrinks = u"\u20B9", str('%.2f' % CostofDrinks)
        PriceofFood = u"\u20B9", str('%.2f' % CostofFood)
        PriceofPackedFood = u"\u20B9", str('%.2f' % CostofPackedFood)

        EV_CostofDrinks.set(PriceofDrinks)
        EV_CostofFood.set(PriceofFood)
        EV_CostofPackedFood.set(PriceofPackedFood)

        ServiceCharge = u"\u20B9", str('%.2f' % 10)
        EV_ServiceCharge.set(ServiceCharge)

        GST = u"\u20B9", str('%.2f' % ((CostofDrinks + CostofFood + 10) * 0.04))

        EV_GST.set(GST)

        TotalTax = ((CostofDrinks + CostofFood + 10) * 0.04)
        TotalCost = u"\u20B9", str('%.2f' % (CostofDrinks + CostofFood + CostofPackedFood + 10 + TotalTax))
        EV_TotalCost.set(TotalCost)

    if (CostofDrinks == 0) and (CostofFood == 0) and (CostofPackedFood == 0):
        tkmb.showinfo('Important Info',
                      "Since you haven't bought anything and you want the total of\nyour purchase (which is 0) we would"
                      " still like to charge you the\ntax for breathing,watching,hearing and sensing !!")


def Text_Receipt_initial():
    global x, RandomRefNo
    with open('.\\data\\_receipt_num.txt', 'w') as rt:
        rt.write('')
        rt.close()
    x = random.randint(10100101, 99999999)
    RandomRefNo = str(x)

    TXT_Receipt.delete('1.0', END)

    TXT_Receipt.insert(END, '\t\t      | RECEIPT |')
    TXT_Receipt.insert(END, '\n\t             - - - - ----------- - - - -')
    TXT_Receipt.insert(END, '\n\t          - - - - BILL:  ' + RandomRefNo + ' - - - -')
    TXT_Receipt.insert(END, '\n\t         - - - - DATE: ' + EV_DateofOrder.get() + ' - - - -')
    TXT_Receipt.insert(END, '\n\n - - ITEM - -\t\t\t\t     - - COST - -\n')
    TXT_Receipt.configure(state='disabled')


def Text_Receipt():
    TXT_Receipt.configure(state='normal')
    TXT_Receipt.delete('1.0', END)
    TXT_Receipt.insert(END, '\t\t      | RECEIPT |')
    TXT_Receipt.insert(END, '\n\t             - - - - ----------- - - - -')
    TXT_Receipt.insert(END, '\n\t          - - - - BILL:  ' + RandomRefNo + ' - - - -')
    TXT_Receipt.insert(END, '\n\t         - - - - DATE: ' + EV_DateofOrder.get() + ' - - - -')
    TXT_Receipt.insert(END, '\n\n   - ITEM -\t\t\t\t         - COST -\n')

    Text_Receipt_Dict = {}

    if var1.get() == 1:
        Text_Receipt_Dict['Mineral Water'] = u"\u20B9" + str(Item1 * 15)

    if var2.get() == 1:
        Text_Receipt_Dict['Hot Coffee'] = u"\u20B9" + str(Item2 * 30)

    if var3.get() == 1:
        Text_Receipt_Dict['Cold Coffee'] = u"\u20B9" + str(Item3 * 45)

    if var4.get() == 1:
        Text_Receipt_Dict['Hot Chocolate'] = u"\u20B9" + str(Item4 * 45)

    if var5.get() == 1:
        Text_Receipt_Dict['Cappuccino'] = u"\u20B9" + str(Item5 * 50)

    if var6.get() == 1:
        Text_Receipt_Dict['Tea'] = u"\u20B9" + str(Item6 * 10)

    if var7.get() == 1:
        Text_Receipt_Dict['Iced Tea'] = u"\u20B9" + str(Item7 * 60)

    if var8.get() == 1:
        Text_Receipt_Dict['Chocolate Shake(Reg)'] = u"\u20B9" + str(Item8 * 75)

    if var9.get() == 1:
        Text_Receipt_Dict['Oreo Shake(Reg)'] = u"\u20B9" + str(Item9 * 95)

    if var10.get() == 1:
        Text_Receipt_Dict['Strawberry Shake(Reg)'] = u"\u20B9" + str(Item10 * 75)

    if var11.get() == 1:
        Text_Receipt_Dict['Pineapple Shake(Reg)'] = u"\u20B9" + str(Item11 * 70)

    if var12.get() == 1:
        Text_Receipt_Dict['Kitkat Shake(Reg)'] = u"\u20B9" + str(Item12 * 95)

    if var13.get() == 1:
        Text_Receipt_Dict['Chocolate Shake(Thick)'] = u"\u20B9" + str(Item13 * 100)

    if var14.get() == 1:
        Text_Receipt_Dict['Oreo Shake(Thick)'] = u"\u20B9" + str(Item14 * 130)

    if var15.get() == 1:
        Text_Receipt_Dict['Strawberry Shake(Thick)'] = u"\u20B9" + str(Item15 * 100)

    if var16.get() == 1:
        Text_Receipt_Dict['Pineapple Shake(Thick)'] = u"\u20B9" + str(Item16 * 95)

    if var17.get() == 1:
        Text_Receipt_Dict['KitKat Shake(Thick)'] = u"\u20B9" + str(Item17 * 130)

    if var18.get() == 1:
        Text_Receipt_Dict['Cold Drink(Canned)'] = u"\u20B9" + str(Item18 * 35)

    if var19.get() == 1:
        Text_Receipt_Dict['Cold Drink(Served)'] = u"\u20B9" + str(Item19 * 45)

    if var20.get() == 1:
        Text_Receipt_Dict['Virgin Mojito'] = u"\u20B9" + str(Item20 * 120)

    if var21.get() == 1:
        Text_Receipt_Dict['Moscow Mule'] = u"\u20B9" + str(Item21 * 140)

    if var22.get() == 1:
        Text_Receipt_Dict['Martini'] = u"\u20B9" + str(Item22 * 130)

    if var23.get() == 1:
        Text_Receipt_Dict['Cranberry Juice'] = u"\u20B9" + str(Item23 * 140)

    if var24.get() == 1:
        Text_Receipt_Dict['French Fries'] = u"\u20B9" + str(Item24 * 60)

    if var25.get() == 1:
        Text_Receipt_Dict['Cheese Balls'] = u"\u20B9" + str(Item25 * 50)

    if var26.get() == 1:
        Text_Receipt_Dict['Veg Sandwich'] = u"\u20B9" + str(Item26 * 50)

    if var27.get() == 1:
        Text_Receipt_Dict['Grilled Sandwich'] = u"\u20B9" + str(Item27 * 75)

    if var28.get() == 1:
        Text_Receipt_Dict['Grilled Cheese Sandwich'] = u"\u20B9" + str(Item28 * 90)

    if var29.get() == 1:
        Text_Receipt_Dict['Paneer Sandwich'] = u"\u20B9" + str(Item29 * 75)

    if var30.get() == 1:
        Text_Receipt_Dict['Nutella Sandwich'] = u"\u20B9" + str(Item30 * 120)

    if var31.get() == 1:
        Text_Receipt_Dict['Aloo Tikki Burger'] = u"\u20B9" + str(Item31 * 35)

    if var32.get() == 1:
        Text_Receipt_Dict['Veg Whooper'] = u"\u20B9" + str(Item32 * 45)

    if var33.get() == 1:
        Text_Receipt_Dict['Double Cheese Burger'] = u"\u20B9" + str(Item33 * 50)

    if var34.get() == 1:
        Text_Receipt_Dict['Paneer King Burger'] = u"\u20B9" + str(Item34 * 75)

    if var35.get() == 1:
        Text_Receipt_Dict['White Pasta'] = u"\u20B9" + str(Item35 * 110)

    if var36.get() == 1:
        Text_Receipt_Dict['Red Pasta'] = u"\u20B9" + str(Item36 * 110)

    if var37.get() == 1:
        Text_Receipt_Dict['Special Italian Pasta'] = u"\u20B9" + str(Item37 * 130)

    if var38.get() == 1:
        Text_Receipt_Dict['Margherita'] = u"\u20B9" + str(Item38 * 120)

    if var39.get() == 1:
        Text_Receipt_Dict['Super Veggie Pizza'] = u"\u20B9" + str(Item39 * 130)

    if var40.get() == 1:
        Text_Receipt_Dict['Paneer Crisp Pizza'] = u"\u20B9" + str(Item40 * 150)

    if var41.get() == 1:
        Text_Receipt_Dict['Peri Peri Paneer Pizza'] = u"\u20B9" + str(Item41 * 200)

    if var42.get() == 1:
        Text_Receipt_Dict['Country Connection Pizza'] = u"\u20B9" + str(Item42 * 250)

    if var43.get() == 1:
        Text_Receipt_Dict['Mexican Tacos'] = u"\u20B9" + str(Item43 * 45)

    if var44.get() == 1:
        Text_Receipt_Dict['Paneer Wrap'] = u"\u20B9" + str(Item44 * 75)

    if var45.get() == 1:
        Text_Receipt_Dict['Spring Roll'] = u"\u20B9" + str(Item45 * 60)

    if var46.get() == 1:
        Text_Receipt_Dict['Pizza Rolls'] = u"\u20B9" + str(Item46 * 90)

    if var47.get() == 1:
        Text_Receipt_Dict['Lays'] = u"\u20B9" + str(Item47 * 20)

    if var48.get() == 1:
        Text_Receipt_Dict['Kurkure'] = u"\u20B9" + str(Item48 * 20)

    if var49.get() == 1:
        Text_Receipt_Dict['Bingo'] = u"\u20B9" + str(Item49 * 20)

    if var50.get() == 1:
        Text_Receipt_Dict['Nutella'] = u"\u20B9" + str(Item50 * 750)

    if var51.get() == 1:
        Text_Receipt_Dict['Hersheys Chocolate Syrup'] = u"\u20B9" + str(Item51 * 320)

    if var52.get() == 1:
        Text_Receipt_Dict['Bhujia'] = u"\u20B9" + str(Item52 * 45)

    if var53.get() == 1:
        Text_Receipt_Dict["Haldiram's Mixture"] = u"\u20B9" + str(Item53 * 60)

    if var54.get() == 1:
        Text_Receipt_Dict['Soya Stix'] = u"\u20B9" + str(Item54 * 30)

    if var55.get() == 1:
        Text_Receipt_Dict['Brittania Marie Gold'] = u"\u20B9" + str(Item55 * 30)

    if var56.get() == 1:
        Text_Receipt_Dict['50-50 Maska Chaska'] = u"\u20B9" + str(Item56 * 10)

    if var57.get() == 1:
        Text_Receipt_Dict['Oreo'] = u"\u20B9" + str(Item57 * 30)

    if var58.get() == 1:
        Text_Receipt_Dict['Hide & Seek'] = u"\u20B9" + str(Item58 * 30)

    if var59.get() == 1:
        Text_Receipt_Dict['Dark Fantasy'] = u"\u20B9" + str(Item59 * 40)

    if var60.get() == 1:
        Text_Receipt_Dict['Kinder Joy'] = u"\u20B9" + str(Item60 * 40)

    if var61.get() == 1:
        Text_Receipt_Dict['Nachos'] = u"\u20B9" + str(Item61 * 35)

    if var62.get() == 1:
        Text_Receipt_Dict['Bournvita'] = u"\u20B9" + str(Item62 * 400)

    if var63.get() == 1:
        Text_Receipt_Dict['Complan'] = u"\u20B9" + str(Item63 * 225)

    if var64.get() == 1:
        Text_Receipt_Dict["Kellog's Chocos"] = u"\u20B9" + str(Item64 * 300)

    if var65.get() == 1:
        Text_Receipt_Dict['Rusk'] = u"\u20B9" + str(Item65 * 65)

    if var66.get() == 1:
        Text_Receipt_Dict['Dairy Milk Silk'] = u"\u20B9" + str(Item66 * 75)

    if var67.get() == 1:
        Text_Receipt_Dict["Hershey's White Cocoa Chocolate"] = u"\u20B9" + str(Item67 * 290)

    if var68.get() == 1:
        Text_Receipt_Dict["Nestle's Dark Sensation"] = u"\u20B9" + str(Item68 * 100)

    if var69.get() == 1:
        Text_Receipt_Dict['Pedigree'] = u"\u20B9" + str(Item69 * 260)

    Text_Receipt_DF = pd.DataFrame(Text_Receipt_Dict.values(), index=Text_Receipt_Dict.keys())

    print(Text_Receipt_Dict)
    print(Text_Receipt_DF)
    TXT_Receipt.insert(END, str(Text_Receipt_DF))

    TXT_Receipt.insert(END, '\n\n\n Cost of Drinks:\t\t\t\t' + str(PriceofDrinks))
    TXT_Receipt.insert(END, '\n Cost of Food:\t\t\t\t' + str(PriceofFood))
    TXT_Receipt.insert(END, '\n Cost of Packed Food Items:\t\t\t\t' + str(PriceofPackedFood))
    TXT_Receipt.insert(END, '\n Service Charges:\t\t\t\t' + str(ServiceCharge))
    TXT_Receipt.insert(END, '\n GST:\t\t\t\t' + str(GST))
    TXT_Receipt.insert(END, '\n\n\n  Total Charges:\t\t\t\t' + str(TotalCost))

    TXT_Receipt.configure(state='disabled')


def Save_Receipt():
    global text
    text = TXT_Receipt.get('1.0', END)
    TXT_Receipt.configure(state='normal')
    TXT_Receipt.delete('1.0', END)
    TXT_Receipt.insert(END, text.replace(u'\u20b9', 'Rs.'))

    data_dir = "data"
    folder = os.path.isdir(data_dir)

    if not folder:
        os.makedirs(data_dir)
        print("'data' folder does not exist.\nFolder created")
    else:
        print("Folder found.\nSaving data.")

    with open('.\\data\\receipt_num.txt', 'r') as rt:
        rt.readlines()

    with open('.\\data\\receipt_num.txt', 'a') as rt:
        rt.write(str(RandomRefNo))
        rt.close()

    with open('.\\data\\' + str(RandomRefNo) + '.json', 'a') as R_D:
        R_D.write('{')
        if var1.get() == 1:
            R_D.write('\n\t"Mineral Water": ' + str(Item1 * 15))
        if var2.get() == 1:
            R_D.write(',\n\t"Hot Coffee": ' + str(Item2 * 30))
        if var3.get() == 1:
            R_D.write(''',\n\t"Cold Coffee": ''' + str(Item3 * 45))
        if var4.get() == 1:
            R_D.write(',\n\t"Hot Chocolate": ' + str(Item4 * 45))
        if var5.get() == 1:
            R_D.write(',\n\t"Cappuccino": ' + str(Item5 * 50))
        if var6.get() == 1:
            R_D.write(',\n\t"Tea": ' + str(Item6 * 10))
        if var7.get() == 1:
            R_D.write(',\n\t"Iced Tea": ' + str(Item7 * 60))
        if var8.get() == 1:
            R_D.write(',\n\t"Chocolate Shake(Reg)": ' + str(Item8 * 75))
        if var9.get() == 1:
            R_D.write(',\n\t"Oreo Shake(Reg)": ' + str(Item9 * 95))
        if var10.get() == 1:
            R_D.write(',\n\t"Strawberry Shake(Reg)": ' + str(Item10 * 75))
        if var11.get() == 1:
            R_D.write(',\n\t"Pineapple Shake(Reg)": ' + str(Item11 * 70))
        if var12.get() == 1:
            R_D.write(',\n\t"Kitkat Shake(Reg)": ' + str(Item12 * 95))
        if var13.get() == 1:
            R_D.write(',\n\t"Chocolate Shake(Thick)": ' + str(Item13 * 100))
        if var14.get() == 1:
            R_D.write(',\n\t"Oreo Shake(Thick)": ' + str(Item14 * 130))
        if var15.get() == 1:
            R_D.write(',\n\t"Strawberry Shake(Thick)": ' + str(Item15 * 100))
        if var16.get() == 1:
            R_D.write(',\n\t"Pineapple Shake(Thick)": ' + str(Item16 * 95))
        if var17.get() == 1:
            R_D.write(',\n\t"KitKat Shake(Thick)": ' + str(Item17 * 130))
        if var18.get() == 1:
            R_D.write(',\n\t"Cold Drink(Canned)": ' + str(Item18 * 35))
        if var19.get() == 1:
            R_D.write(',\n\t"Cold Drink(Served)": ' + str(Item19 * 45))
        if var20.get() == 1:
            R_D.write(',\n\t"Virgin Mojito": ' + str(Item20 * 120))
        if var21.get() == 1:
            R_D.write(',\n\t"Moscow Mule": ' + str(Item21 * 140))
        if var22.get() == 1:
            R_D.write(',\n\t"Martini": ' + str(Item22 * 130))
        if var23.get() == 1:
            R_D.write(',\n\t"Cranberry Juice": ' + str(Item23 * 140))
        if var24.get() == 1:
            R_D.write(',\n\t"French Fries": ' + str(Item24 * 60))
        if var25.get() == 1:
            R_D.write(',\n\t"Cheese Balls": ' + str(Item25 * 50))
        if var26.get() == 1:
            R_D.write(',\n\t"Veg Sandwich": ' + str(Item26 * 50))
        if var27.get() == 1:
            R_D.write(',\n\t"Grilled Sandwich": ' + str(Item27 * 75))
        if var28.get() == 1:
            R_D.write(',\n\t"Grilled Cheese Sandwich": ' + str(Item28 * 90))
        if var29.get() == 1:
            R_D.write(',\n\t"Paneer Sandwich": ' + str(Item29 * 75))
        if var30.get() == 1:
            R_D.write(',\n\t"Nutella Sandwich": ' + str(Item30 * 120))
        if var31.get() == 1:
            R_D.write(',\n\t"Aloo Tikki Burger": ' + str(Item31 * 35))
        if var32.get() == 1:
            R_D.write(',\n\t"Veg Whooper": ' + str(Item32 * 45))
        if var33.get() == 1:
            R_D.write(',\n\t"Double Cheese Burger": ' + str(Item33 * 50))
        if var34.get() == 1:
            R_D.write(',\n\t"Paneer King Burger": ' + str(Item34 * 75))
        if var35.get() == 1:
            R_D.write(',\n\t"White Pasta": ' + str(Item35 * 110))
        if var36.get() == 1:
            R_D.write(',\n\t"Red Pasta": ' + str(Item36 * 110))
        if var37.get() == 1:
            R_D.write(',\n\t"Special Italian Pasta": ' + str(Item37 * 130))
        if var38.get() == 1:
            R_D.write(',\n\t"Margherita": ' + str(Item38 * 120))
        if var39.get() == 1:
            R_D.write(',\n\t"Super Veggie Pizza": ' + str(Item39 * 130))
        if var40.get() == 1:
            R_D.write(',\n\t"Paneer Crisp Pizza": ' + str(Item40 * 150))
        if var41.get() == 1:
            R_D.write(',\n\t"Peri Peri Paneer Pizza": ' + str(Item41 * 200))
        if var42.get() == 1:
            R_D.write(',\n\t"Country Connection Pizza": ' + str(Item42 * 250))
        if var43.get() == 1:
            R_D.write(',\n\t"Mexican Tacos": ' + str(Item43 * 45))
        if var44.get() == 1:
            R_D.write(',\n\t"Paneer Wrap": ' + str(Item44 * 75))
        if var45.get() == 1:
            R_D.write(',\n\t"Spring Roll": ' + str(Item45 * 60))
        if var46.get() == 1:
            R_D.write(',\n\t"Pizza Rolls": ' + str(Item46 * 90))
        if var47.get() == 1:
            R_D.write(',\n\t"Lays": ' + str(Item47 * 20))
        if var48.get() == 1:
            R_D.write(',\n\t"Kurkure": ' + str(Item48 * 20))
        if var49.get() == 1:
            R_D.write(',\n\t"Bingo": ' + str(Item49 * 20))
        if var50.get() == 1:
            R_D.write(',\n\t"Nutella": ' + str(Item50 * 750))
        if var51.get() == 1:
            R_D.write(',\n\t"Hersheys Chocolate Syrup": ' + str(Item51 * 320))
        if var52.get() == 1:
            R_D.write(',\n\t"Bhujia": ' + str(Item52 * 45))
        if var53.get() == 1:
            R_D.write(''',\n\t"Haldiram's Mixture": ''' + str(Item53 * 60))
        if var54.get() == 1:
            R_D.write(',\n\t"Soya Stix": ' + str(Item54 * 30))
        if var55.get() == 1:
            R_D.write(',\n\t"Brittania Marie Gold": ' + str(Item55 * 30))
        if var56.get() == 1:
            R_D.write(',\n\t"50-50 Maska Chaska": ' + str(Item56 * 10))
        if var57.get() == 1:
            R_D.write(',\n\t"Oreo": ' + str(Item57 * 30))
        if var58.get() == 1:
            R_D.write(',\n\t"Hide & Seek": ' + str(Item58 * 30))
        if var59.get() == 1:
            R_D.write(',\n\t"Dark Fantasy": ' + str(Item59 * 40))
        if var60.get() == 1:
            R_D.write(',\n\t"Kinder Joy": ' + str(Item60 * 40))
        if var61.get() == 1:
            R_D.write(',\n\t"Nachos": ' + str(Item61 * 35))
        if var62.get() == 1:
            R_D.write(',\n\t"Bournvita": ' + str(Item62 * 400))
        if var63.get() == 1:
            R_D.write(',\n\t"Complan": ' + str(Item63 * 225))
        if var64.get() == 1:
            R_D.write(''',\n\t"Kellog's Chocos": ''' + str(Item64 * 300))
        if var65.get() == 1:
            R_D.write(',\n\t"Rusk": ' + str(Item65 * 65))
        if var66.get() == 1:
            R_D.write(',\n\t"Dairy Milk Silk": ' + str(Item66 * 75))
        if var67.get() == 1:
            R_D.write(''',\n\t"Hershey's White Cocoa Chocolate": ''' + str(Item67 * 290))
        if var68.get() == 1:
            R_D.write(''',\n\t"Nestle's Dark Sensation": ''' + str(Item68 * 100))
        if var69.get() == 1:
            R_D.write(',\n\t"Pedigree": ' + str(Item69 * 260))
        R_D.write('\n}')
        R_D.write('\n')
        R_D.close()

    ans = tkmb.askyesno('Database?',
                        'Receipt has been saved in a {.txt} file.\nWould you like to save it to the Database?')
    if ans > 0:
        Save_Receipt_SQL()
        TXT_Receipt.configure(state='normal')
        TXT_Receipt.delete('1.0', END)
        TXT_Receipt.insert(END, text)
        TXT_Receipt.insert(END, '\n\n\n\n\n\n\t           RECEIPT RECORD SAVED !!')
        TXT_Receipt.insert(END, '\n \t\tSaved to Database !')
        TXT_Receipt.configure(state='disabled')
    else:
        TXT_Receipt.configure(state='normal')
        TXT_Receipt.delete('1.0', END)
        TXT_Receipt.insert(END, text)
        TXT_Receipt.insert(END, '\n\n\n\n\n\n\t           RECEIPT RECORD SAVED !!')
        TXT_Receipt.configure(state='disabled')
        return "Receipt Not Saved to Database"


"""
ADDING DATA
   TO SQL
"""

'''
def RsConverter():
    text = TXT_Receipt.get('1.0', END)
    TXT_Receipt.configure(state='normal')
    TXT_Receipt.delete('1.0', END)
    TXT_Receipt.insert(END, text.replace(u'\u20b9', 'Rs.'))
'''

def Save_Receipt_SQL():
    drinks_dict = dict()
    d_p_dict = dict()
    food_dict = dict()
    f_p_dict = dict()
    packed_food_dict = dict()
    p_f_p_dict = dict()

    if var1.get() == 1:
        drinks_dict['MineralWater'] = int(EV_MineralWater.get())
        d_p_dict['MineralWater'] = CostofMineralWater
    else:
        drinks_dict['MineralWater'] = 0
        d_p_dict['MineralWater'] = CostofMineralWater

    if var2.get() == 1:
        drinks_dict['HotCoffee'] = int(EV_HotCoffee.get())
        d_p_dict['HotCoffee'] = CostofHotCoffee
    else:
        drinks_dict['HotCoffee'] = 0
        d_p_dict['HotCoffee'] = CostofHotCoffee

    if var3.get() == 1:
        drinks_dict['ColdCoffee'] = int(EV_ColdCoffee.get())
        d_p_dict['ColdCoffee'] = CostofColdCoffee
    else:
        drinks_dict['ColdCoffee'] = 0
        d_p_dict['ColdCoffee'] = CostofColdCoffee

    if var4.get() == 1:
        drinks_dict['HotChocolate'] = int(EV_HotChocolate.get())
        d_p_dict['HotChocolate'] = CostofHotChocolate
    else:
        drinks_dict['HotChocolate'] = 0
        d_p_dict['HotChocolate'] = CostofHotChocolate

    if var5.get() == 1:
        drinks_dict['Cappuccino'] = int(EV_Cappuccino.get())
        d_p_dict['Cappuccino'] = CostofCappuccino
    else:
        drinks_dict['Cappuccino'] = 0
        d_p_dict['Cappuccino'] = CostofCappuccino

    if var6.get() == 1:
        drinks_dict['Tea'] = int(EV_Tea.get())
        d_p_dict['Tea'] = CostofTea
    else:
        drinks_dict['Tea'] = 0
        d_p_dict['Tea'] = CostofTea

    if var7.get() == 1:
        drinks_dict['IcedTea'] = int(EV_IcedTea.get())
        d_p_dict['IcedTea'] = CostofIcedTea
    else:
        drinks_dict['IcedTea'] = 0
        d_p_dict['IcedTea'] = CostofIcedTea

    if var8.get() == 1:
        drinks_dict['ChocolateShake_R'] = int(EV_ChocolateShake_R.get())
        d_p_dict['ChocolateShake_R'] = CostofChocolateShake_R
    else:
        drinks_dict['ChocolateShake_R'] = 0
        d_p_dict['ChocolateShake_R'] = CostofChocolateShake_R

    if var9.get() == 1:
        drinks_dict['OreoShake_R'] = int(EV_OreoShake_R.get())
        d_p_dict['OreoShake_R'] = CostofOreoShake_R
    else:
        drinks_dict['OreoShake_R'] = 0
        d_p_dict['OreoShake_R'] = CostofOreoShake_R

    if var10.get() == 1:
        drinks_dict['StrawberryShake_R'] = int(EV_StrawberryShake_R.get())
        d_p_dict['StrawberryShake_R'] = CostofStrawberryShake_R
    else:
        drinks_dict['StrawberryShake_R'] = 0
        d_p_dict['StrawberryShake_R'] = CostofStrawberryShake_R

    if var11.get() == 1:
        drinks_dict['PineappleShake_R'] = int(EV_PineappleShake_R.get())
        d_p_dict['PineappleShake_R'] = CostofPineappleShake_R
    else:
        drinks_dict['PineappleShake_R'] = 0
        d_p_dict['PineappleShake_R'] = CostofPineappleShake_R

    if var12.get() == 1:
        drinks_dict['KitkatShake_R'] = int(EV_KitkatShake_R.get())
        d_p_dict['KitkatShake_R'] = CostofKitkatShake_R
    else:
        drinks_dict['KitkatShake_R'] = 0
        d_p_dict['KitkatShake_R'] = CostofKitkatShake_R

    if var13.get() == 1:
        drinks_dict['ChocolateShake_T'] = int(EV_ChocolateShake_T.get())
        d_p_dict['ChocolateShake_T'] = CostofChocolateShake_T
    else:
        drinks_dict['ChocolateShake_T'] = 0
        d_p_dict['ChocolateShake_T'] = CostofChocolateShake_T

    if var14.get() == 1:
        drinks_dict['OreoShake_T'] = int(EV_OreoShake_T.get())
        d_p_dict['OreoShake_T'] = CostofOreoShake_T
    else:
        drinks_dict['OreoShake_T'] = 0
        d_p_dict['OreoShake_T'] = CostofOreoShake_T

    if var15.get() == 1:
        drinks_dict['StrawberryShake_T'] = int(EV_StrawberryShake_T.get())
        d_p_dict['StrawberryShake_T'] = CostofStrawberryShake_T
    else:
        drinks_dict['StrawberryShake_T'] = 0
        d_p_dict['StrawberryShake_T'] = CostofStrawberryShake_T

    if var16.get() == 1:
        drinks_dict['PineappleShake_T'] = int(EV_PineappleShake_T.get())
        d_p_dict['PineappleShake_T'] = CostofPineappleShake_T
    else:
        drinks_dict['PineappleShake_T'] = 0
        d_p_dict['PineappleShake_T'] = CostofPineappleShake_T

    if var17.get() == 1:
        drinks_dict['KitkatShake_T'] = int(EV_KitkatShake_T.get())
        d_p_dict['KitkatShake_T'] = CostofKitkatShake_T
    else:
        drinks_dict['KitkatShake_T'] = 0
        d_p_dict['KitkatShake_T'] = CostofKitkatShake_T

    if var18.get() == 1:
        drinks_dict['ColdDrink_C'] = int(EV_ColdDrink_C.get())
        d_p_dict['ColdDrink_C'] = CostofColdDrink_C
    else:
        drinks_dict['ColdDrink_C'] = 0
        d_p_dict['ColdDrink_C'] = CostofColdDrink_C

    if var19.get() == 1:
        drinks_dict['ColdDrink_S'] = int(EV_ColdDrink_S.get())
        d_p_dict['ColdDrink_S'] = CostofColdDrink_S
    else:
        drinks_dict['ColdDrink_S'] = 0
        d_p_dict['ColdDrink_S'] = CostofColdDrink_S

    if var20.get() == 1:
        drinks_dict['VirginMojito'] = int(EV_VirginMojito.get())
        d_p_dict['VirginMojito'] = CostofVirginMojito
    else:
        drinks_dict['VirginMojito'] = 0
        d_p_dict['VirginMojito'] = CostofVirginMojito

    if var21.get() == 1:
        drinks_dict['MoscowMule'] = int(EV_MoscowMule.get())
        d_p_dict['MoscowMule'] = CostofMoscowMule
    else:
        drinks_dict['MoscowMule'] = 0
        d_p_dict['MoscowMule'] = CostofMoscowMule

    if var22.get() == 1:
        drinks_dict['Martini'] = int(EV_Martini.get())
        d_p_dict['Martini'] = CostofMartini
    else:
        drinks_dict['Martini'] = 0
        d_p_dict['Martini'] = CostofMartini

    if var23.get() == 1:
        drinks_dict['CranberryJuice'] = int(EV_CranberryJuice.get())
        d_p_dict['CranberryJuice'] = CostofCranberryJuice
    else:
        drinks_dict['CranberryJuice'] = 0
        d_p_dict['CranberryJuice'] = CostofCranberryJuice

    if var24.get() == 1:
        food_dict['FrenchFries'] = int(EV_FrenchFries.get())
        f_p_dict['FrenchFries'] = CostofFrenchFries
    else:
        food_dict['FrenchFries'] = 0
        f_p_dict['FrenchFries'] = CostofFrenchFries

    if var25.get() == 1:
        food_dict['CheeseBalls'] = int(EV_CheeseBalls.get())
        f_p_dict['CheeseBalls'] = CostofCheeseBalls
    else:
        food_dict['CheeseBalls'] = 0
        f_p_dict['CheeseBalls'] = CostofCheeseBalls

    if var26.get() == 1:
        food_dict['VegSandwich'] = int(EV_VegSandwich.get())
        f_p_dict['VegSandwich'] = CostofVegSandwich
    else:
        food_dict['VegSandwich'] = 0
        f_p_dict['VegSandwich'] = CostofVegSandwich

    if var27.get() == 1:
        food_dict['GrilledSandwich'] = int(EV_GrilledSandwich.get())
        f_p_dict['GrilledSandwich'] = CostofGrilledSandwich
    else:
        food_dict['GrilledSandwich'] = 0
        f_p_dict['GrilledSandwich'] = CostofGrilledSandwich

    if var28.get() == 1:
        food_dict['GrilledCheeseSandwich'] = int(EV_GrilledCheeseSandwich.get())
        f_p_dict['GrilledCheeseSandwich'] = CostofGrilledCheeseSandwich
    else:
        food_dict['GrilledCheeseSandwich'] = 0
        f_p_dict['GrilledCheeseSandwich'] = CostofGrilledCheeseSandwich

    if var29.get() == 1:
        food_dict['PaneerSandwich'] = int(EV_PaneerSandwich.get())
        f_p_dict['PaneerSandwich'] = CostofPaneerSandwich
    else:
        food_dict['PaneerSandwich'] = 0
        f_p_dict['PaneerSandwich'] = CostofPaneerSandwich

    if var30.get() == 1:
        food_dict['NutellaSandwich'] = int(EV_NutellaSandwich.get())
        f_p_dict['NutellaSandwich'] = CostofNutellaSandwich
    else:
        food_dict['NutellaSandwich'] = 0
        f_p_dict['NutellaSandwich'] = CostofNutellaSandwich

    if var31.get() == 1:
        food_dict['AlooTikkiBurger'] = int(EV_AlooTikkiBurger.get())
        f_p_dict['AlooTikkiBurger'] = CostofAlooTikkiBurger
    else:
        food_dict['AlooTikkiBurger'] = 0
        f_p_dict['AlooTikkiBurger'] = CostofAlooTikkiBurger

    if var32.get() == 1:
        food_dict['VegWhooper'] = int(EV_VegWhooper.get())
        f_p_dict['VegWhooper'] = CostofVegWhooper
    else:
        food_dict['VegWhooper'] = 0
        f_p_dict['VegWhooper'] = CostofVegWhooper

    if var33.get() == 1:
        food_dict['DoubleCheeseBurger'] = int(EV_DoubleCheeseBurger.get())
        f_p_dict['DoubleCheeseBurger'] = CostofDoubleCheeseBurger
    else:
        food_dict['DoubleCheeseBurger'] = 0
        f_p_dict['DoubleCheeseBurger'] = CostofDoubleCheeseBurger

    if var34.get() == 1:
        food_dict['PaneerKingBurger'] = int(EV_PaneerKingBurger.get())
        f_p_dict['PaneerKingBurger'] = CostofPaneerKingBurger
    else:
        food_dict['PaneerKingBurger'] = 0
        f_p_dict['PaneerKingBurger'] = CostofPaneerKingBurger

    if var35.get() == 1:
        food_dict['WhitePasta'] = int(EV_WhitePasta.get())
        f_p_dict['WhitePasta'] = CostofWhitePasta
    else:
        food_dict['WhitePasta'] = 0
        f_p_dict['WhitePasta'] = CostofWhitePasta

    if var36.get() == 1:
        food_dict['RedPasta'] = int(EV_RedPasta.get())
        f_p_dict['RedPasta'] = CostofRedPasta
    else:
        food_dict['RedPasta'] = 0
        f_p_dict['RedPasta'] = CostofRedPasta

    if var37.get() == 1:
        food_dict['SpecialItalianPasta'] = int(EV_SpecialItalianPasta.get())
        f_p_dict['SpecialItalianPasta'] = CostofSpecialItalianPasta
    else:
        food_dict['SpecialItalianPasta'] = 0
        f_p_dict['SpecialItalianPasta'] = CostofSpecialItalianPasta

    if var38.get() == 1:
        food_dict['Margherita'] = int(EV_MargheritaPizza.get())
        f_p_dict['Margherita'] = CostofMargherita
    else:
        food_dict['Margherita'] = 0
        f_p_dict['Margherita'] = CostofMargherita

    if var39.get() == 1:
        food_dict['VeggiePizza'] = int(EV_SuperVeggiePizza.get())
        f_p_dict['VeggiePizza'] = CostofSuperVeggiePizza
    else:
        food_dict['VeggiePizza'] = 0
        f_p_dict['VeggiePizza'] = CostofSuperVeggiePizza

    if var40.get() == 1:
        food_dict['PaneerCrispPizza'] = int(EV_PaneerCrispPizza.get())
        f_p_dict['PaneerCrispPizza'] = CostofPaneerCrispPizza
    else:
        food_dict['PaneerCrispPizza'] = 0
        f_p_dict['PaneerCrispPizza'] = CostofPaneerCrispPizza

    if var41.get() == 1:
        food_dict['PeriPeriPaneerPizza'] = int(EV_PeriPeriPaneerPizza.get())
        f_p_dict['PeriPeriPaneerPizza'] = CostofPeriPeriPaneerPizza
    else:
        food_dict['PeriPeriPaneerPizza'] = 0
        f_p_dict['PeriPeriPaneerPizza'] = CostofPeriPeriPaneerPizza

    if var42.get() == 1:
        food_dict['ChefSpecialCountryConnectionPizza'] = int(EV_ChefSpecialCountryConnectionPizza.get())
        f_p_dict['ChefSpecialCountryConnectionPizza'] = CostofChefSpecialCountryConnectionPizza
    else:
        food_dict['ChefSpecialCountryConnectionPizza'] = 0
        f_p_dict['ChefSpecialCountryConnectionPizza'] = CostofChefSpecialCountryConnectionPizza

    if var43.get() == 1:
        food_dict['MexicanTacos'] = int(EV_MexicanTacos.get())
        f_p_dict['MexicanTacos'] = CostofMexicanTacos
    else:
        food_dict['MexicanTacos'] = 0
        f_p_dict['MexicanTacos'] = CostofMexicanTacos

    if var44.get() == 1:
        food_dict['PaneerWrap'] = int(EV_PaneerWrap.get())
        f_p_dict['PaneerWrap'] = CostofPaneerWrap
    else:
        food_dict['PaneerWrap'] = 0
        f_p_dict['PaneerWrap'] = CostofPaneerWrap

    if var45.get() == 1:
        food_dict['SpringRoll'] = int(EV_SpringRoll.get())
        f_p_dict['SpringRoll'] = CostofSpringRoll
    else:
        food_dict['SpringRoll'] = 0
        f_p_dict['SpringRoll'] = CostofSpringRoll

    if var46.get() == 1:
        food_dict['PizzaRolls'] = int(EV_PizzaRolls.get())
        f_p_dict['PizzaRolls'] = CostofPizzaRolls
    else:
        food_dict['PizzaRolls'] = 0
        f_p_dict['PizzaRolls'] = CostofPizzaRolls

    if var47.get() == 1:
        packed_food_dict['Lays'] = int(EV_Lays.get())
        p_f_p_dict['Lays'] = CostofLays
    else:
        packed_food_dict['Lays'] = 0
        p_f_p_dict['Lays'] = CostofLays

    if var48.get() == 1:
        packed_food_dict['Kurkure'] = int(EV_Kurkure.get())
        p_f_p_dict['Kurkure'] = CostofKurkure
    else:
        packed_food_dict['Kurkure'] = 0
        p_f_p_dict['Kurkure'] = CostofKurkure

    if var49.get() == 1:
        packed_food_dict['Bingo'] = int(EV_Bingo.get())
        p_f_p_dict['Bingo'] = CostofBingo
    else:
        packed_food_dict['Bingo'] = 0
        p_f_p_dict['Bingo'] = CostofBingo

    if var50.get() == 1:
        packed_food_dict['Nutella'] = int(EV_Nutella.get())
        p_f_p_dict['Nutella'] = CostofNutella
    else:
        packed_food_dict['Nutella'] = 0
        p_f_p_dict['Nutella'] = CostofNutella

    if var51.get() == 1:
        packed_food_dict['HersheysChocolateSyrup'] = int(EV_HersheysChocolateSyrup.get())
        p_f_p_dict['HersheysChocolateSyrup'] = CostofHersheysChocolateSyrup
    else:
        packed_food_dict['HersheysChocolateSyrup'] = 0
        p_f_p_dict['HersheysChocolateSyrup'] = CostofHersheysChocolateSyrup

    if var52.get() == 1:
        packed_food_dict['Bhujia'] = int(EV_Bhujia.get())
        p_f_p_dict['Bhujia'] = CostofBhujia
    else:
        packed_food_dict['Bhujia'] = 0
        p_f_p_dict['Bhujia'] = CostofBhujia

    if var53.get() == 1:
        packed_food_dict['Mixture'] = int(EV_Mixture.get())
        p_f_p_dict['Mixture'] = CostofMixture
    else:
        packed_food_dict['Mixture'] = 0
        p_f_p_dict['Mixture'] = CostofMixture

    if var54.get() == 1:
        packed_food_dict['SoyaStix'] = int(EV_SoyaStix.get())
        p_f_p_dict['SoyaStix'] = CostofSoyaStix
    else:
        packed_food_dict['SoyaStix'] = 0
        p_f_p_dict['SoyaStix'] = CostofSoyaStix

    if var55.get() == 1:
        packed_food_dict['BrittaniaMarieGold'] = int(EV_BrittaniaMarieGold.get())
        p_f_p_dict['BrittaniaMarieGold'] = CostofBrittaniaMarieGold
    else:
        packed_food_dict['BrittaniaMarieGold'] = 0
        p_f_p_dict['BrittaniaMarieGold'] = CostofBrittaniaMarieGold

    if var56.get() == 1:
        packed_food_dict['_5050_'] = int(EV_5050.get())
        p_f_p_dict['_5050_'] = Costof5050
    else:
        packed_food_dict['_5050_'] = 0
        p_f_p_dict['_5050_'] = Costof5050

    if var57.get() == 1:
        packed_food_dict['Oreo'] = int(EV_Oreo.get())
        p_f_p_dict['Oreo'] = CostofOreo
    else:
        packed_food_dict['Oreo'] = 0
        p_f_p_dict['Oreo'] = CostofOreo

    if var58.get() == 1:
        packed_food_dict['HideandSeek'] = int(EV_HideandSeek.get())
        p_f_p_dict['HideandSeek'] = CostofHideandSeek
    else:
        packed_food_dict['HideandSeek'] = 0
        p_f_p_dict['HideandSeek'] = CostofHideandSeek

    if var59.get() == 1:
        packed_food_dict['DarkFantasy'] = int(EV_DarkFantasy.get())
        p_f_p_dict['DarkFantasy'] = CostofDarkFantasy
    else:
        packed_food_dict['DarkFantasy'] = 0
        p_f_p_dict['DarkFantasy'] = CostofDarkFantasy

    if var60.get() == 1:
        packed_food_dict['KinderJoy'] = int(EV_KinderJoy.get())
        p_f_p_dict['KinderJoy'] = CostofKinderJoy
    else:
        packed_food_dict['KinderJoy'] = 0
        p_f_p_dict['KinderJoy'] = CostofKinderJoy

    if var61.get() == 1:
        packed_food_dict['Nachos'] = int(EV_Nachos.get())
        p_f_p_dict['Nachos'] = CostofNachos
    else:
        packed_food_dict['Nachos'] = 0
        p_f_p_dict['Nachos'] = CostofNachos

    if var62.get() == 1:
        packed_food_dict['Bournvita'] = int(EV_Bournvita.get())
        p_f_p_dict['Bournvita'] = CostofBournvita
    else:
        packed_food_dict['Bournvita'] = 0
        p_f_p_dict['Bournvita'] = CostofBournvita

    if var63.get() == 1:
        packed_food_dict['Complan'] = int(EV_Complan.get())
        p_f_p_dict['Complan'] = CostofComplan
    else:
        packed_food_dict['Complan'] = 0
        p_f_p_dict['Complan'] = CostofComplan

    if var64.get() == 1:
        packed_food_dict['KellogsChocos'] = int(EV_KellogsChocos.get())
        p_f_p_dict['KellogsChocos'] = CostofKellogsChocos
    else:
        packed_food_dict['KellogsChocos'] = 0
        p_f_p_dict['KellogsChocos'] = CostofKellogsChocos

    if var65.get() == 1:
        packed_food_dict['Rusk'] = int(EV_Rusk.get())
        p_f_p_dict['Rusk'] = CostofRusk
    else:
        packed_food_dict['Rusk'] = 0
        p_f_p_dict['Rusk'] = CostofRusk

    if var66.get() == 1:
        packed_food_dict['DairyMilkSilk'] = int(EV_DairyMilkSilk.get())
        p_f_p_dict['DairyMilkSilk'] = CostofDairyMilkSilk
    else:
        packed_food_dict['DairyMilkSilk'] = 0
        p_f_p_dict['DairyMilkSilk'] = CostofDairyMilkSilk

    if var67.get() == 1:
        packed_food_dict['NestlesDarkSensation'] = int(EV_NestlesDarkSensation.get())
        p_f_p_dict['NestlesDarkSensation'] = CostofNestlesDarkSensation
    else:
        packed_food_dict['NestlesDarkSensation'] = 0
        p_f_p_dict['NestlesDarkSensation'] = CostofNestlesDarkSensation

    if var68.get() == 1:
        packed_food_dict['HersheysWhiteCocoaChocolate'] = int(EV_HersheysWhiteCocoaChocolate.get())
        p_f_p_dict['HersheysWhiteCocoaChocolate'] = CostofHersheysWhiteCocoaChocolate
    else:
        packed_food_dict['HersheysWhiteCocoaChocolate'] = 0
        p_f_p_dict['HersheysWhiteCocoaChocolate'] = CostofHersheysWhiteCocoaChocolate

    if var69.get() == 1:
        packed_food_dict['Pedigree'] = int(EV_Pedigree.get())
        p_f_p_dict['Pedigree'] = CostofPedigree
    else:
        packed_food_dict['Pedigree'] = 0
        p_f_p_dict['Pedigree'] = CostofPedigree

    drinks_list = []
    food_list = []
    packed_food_list = []

    drinks_list.append(x)
    food_list.append(x)
    packed_food_list.append(x)

    for i in drinks_dict.keys():
        if drinks_dict.get(i) >= 0:
            drinks_list.append(drinks_dict.get(i))

    for j in packed_food_dict.keys():
        if packed_food_dict.get(j) >= 0:
            packed_food_list.append(packed_food_dict.get(j))

    for k in food_dict.keys():
        if food_dict.get(k) >= 0:
            food_list.append(food_dict.get(k))

    d_v = 'INSERT INTO drinks_info VALUES' + str(tuple(drinks_list))
    f_v = 'INSERT INTO food_info VALUES' + str(tuple(food_list))
    p_f_v = 'INSERT INTO packed_food_info VALUES' + str(tuple(packed_food_list))

    print(d_v)
    print()
    print(f_v)
    print()
    print(p_f_v)
    print()
    t_end = time.time() + 2
    print('Inserting Records...')
    while time.time() < t_end:
        l = '\|/-\|/-'
        for i in l:
            print(i, end='\r')
            time.sleep(0.15)
    t_end = time.time() + 2
    AddtoDrinks(d_v)
    while time.time() < t_end:
        l = '\|/-\|/-'
        for i in l:
            print(i, end='\r')
            time.sleep(0.15)
    AddtoFood(f_v)
    t_end = time.time() + 2
    while time.time() < t_end:
        l = '\|/-\|/-'
        for i in l:
            print(i, end='\r')
            time.sleep(0.15)
    AddtoPackedFood(p_f_v)
    print('Records Inserted')
    tkmb.showinfo('Insert Records', 'Records Inserted !')


def CASH():
    global TotalCost
    root2 = Tk()
    root2.geometry('200x200+0+0')
    root2.title('CASH Payment')
    Top_LBL = Label(root2, text='--Cash Payment--')
    Top_LBL.pack(anchor='nw')
    Transaction_Frame = Frame(root2, bd=1)
    Transaction_Frame.pack(anchor='nw')
    Moneytobepaid_LBL = Label(Transaction_Frame, text='Money to be paid: ' + EV_TotalCost.get(), font='timesnewroman 9 '
                                                                                                      'normal')
    Moneytobepaid_LBL.grid(row=0, column=0)


def foo(event):
    if cbvar.get() == 'CASH':
        answer = tkmb.askyesno('Payment Option', 'Do you want to continue with CASH?')
        if answer > 0:
            Payment_TXT.configure(state='normal')
            Payment_TXT.delete('1.0', END)
            Payment_TXT.insert(END, '\n\n\tPaid by cash')
            Payment_TXT.configure(state='disabled')
        else:
            return
    elif cbvar.get() == 'RuPay [ONLINE WALLET]':
        answer = tkmb.askyesno('Payment Option', 'Do you want to continue with RuPay [ONLINE WALLET]?')
        if answer > 0:
            Payment_TXT.configure(state='normal')
            Payment_TXT.delete('1.0', END)
            Payment_TXT.insert(END, '\n\n\tPaid through RuPay[ONLINE WALLET].')
            Payment_TXT.configure(state='disabled')


def proceed_payment(): pass

############################################# RECIPT AND BUTTONS #############################################
##############################################################################################################


BTN_Total = Button(Buttons_Frame, bd=2, padx=3, pady=2, fg='black', font=('arial', 9, 'bold'), width=6, text='Total',
                   bg='powder blue', command=Total_Cost).grid(row=0, column=0)
BTN_Receipt = Button(Buttons_Frame, bd=2, padx=3, pady=2, fg='black', font=('arial', 9, 'bold'), width=6,
                     text='Receipt', bg='powder blue', command=Text_Receipt).grid(row=0, column=1)
BTN_Reset = Button(Buttons_Frame, bd=2, padx=3, pady=2, fg='black', font=('arial', 9, 'bold'), width=6, text='Reset',
                   bg='powder blue', command=Reset).grid(row=0, column=2)
BTN_Save = Button(Buttons_Frame, bd=2, padx=3, pady=2, fg='black', font=('arial', 9, 'bold'), width=6, text='Save',
                  bg='orange', command=Save_Receipt).grid(row=0, column=3)
BTN_Exit = Button(Buttons_Frame, bd=2, padx=3, pady=2, fg='black', font=('arial', 9, 'bold'), width=6, text='Exit',
                  bg='red', command=Exit).grid(row=0, column=4)

################################################ PAYMENT ################################################
################################################## AREA #################################################

Payment_Combobox = ttk.Combobox(Payment_Frame, width=30, height=6, font=('Mongolian Baiti', 13, 'bold'),
                                textvariable=cbvar)
Payment_Combobox['values'] = ['CASH', 'RuPay [ONLINE WALLET]', 'Paytm [ONLINE WALLET]',
                              'AmazonPay [ONLINE WALLET]', 'PhonePe [ONLINE WALLET]',
                              'Freecharge [ONLINE WALLET]', 'Mobikwik [ONLINE WALLET]',
                              'American Express [CARD]', 'Mastercard [CARD]', 'BHIM UPI',
                              'HDFC [BANK]', 'SBI [BANK]', 'ICICI [BANK]', 'Axis [BANK]',
                              'Kotak [BANK]', 'ZETA [FOOD CARD]', 'Sodexo [FOOD CARD]']
Payment_Combobox.bind('<<ComboboxSelected>>')# , foo)
Payment_Combobox.current(0)
Payment_Combobox.grid(row=0, column=0, columnspan=4)

Payment_Proceed_BTN = Button(Payment_Frame, width=44, bg='light green', text='Proceed', bd=4,
                             command=proceed_payment) # line 2834
Payment_Proceed_BTN.grid(row=1, column=0,pady=2, columnspan=4)
Payment_Proceed_BTN.grid_rowconfigure(1, weight=1)
Payment_Proceed_BTN.grid_columnconfigure(0, weight=1)

Payment_TXT = Text(Payment_Frame,width=40, height=36, font=('Lucida Sans Unicode', 8, 'bold'))
Payment_TXT.grid(row=2, column=0, pady=1)
Payment_TXT.insert(1.0, '***THIS\nFEATURE\nHAS\nNOT\nBEEN\nENABLED\nYET***')
Payment_TXT.configure(state='disabled')

#- - - -   |\   |          - - -    /\   / ` ``  |`````       |\   | |````` |````` |``\  |````` |``\
#   |      | \  |         |        /__\  \_ _ _  |_ _ _       | \  | |_ _ _ |_ _ _ |   \ |_ _ _ |   \
#   |      |  \ |         |       /    \       \ |            |  \ | |      |      |   / |      |   /
#- - - -   |   \|          - - - /      \ _ _ _/ |_ _ _       |   \| |_ _ _ |_ _ _ |../  |_ _ _ |../

#                  |  |                                           |  |
#                  |  |                                           |  |
#                 \|  |/                                         \|  |/
#                  \  /                                           \  /
#                   \/                                             \/

'''
################################################ PAYMENT ################################################
############################################### FUNCTIONS ###############################################


def RUPAY(): pass


def AMERICANEXPRESS(): pass


def MASTERCARD(): pass


def _VISA(): pass


def AMAZONPAY(): pass


def PAYTM(): pass


def PHONEPE(): pass


def FREECHARGE(): pass


def MOBIKWIK(): pass


def BHIMUPI(): pass


def _HDFC(): pass


def _SBI(): pass


def _ICICI(): pass


def AXIS(): pass


def KOTAK(): pass


def ZETA(): pass


def SODEXO(): pass


############################################## PAYMENT LABELS ##############################################
################################################ AND BUTTONS ###############################################

Payment_LBL = Label(root, text='Payment via', width=19, font=('Comic Sans MS', 20, 'bold'), bg='red', bd=8,
                    relief='ridge',
                    fg='light green')
Payment_LBL.pack(anchor='n', ipady=10)

text = Text(Payment_Frame, wrap='none', height=35)
scrollbar = Scrollbar(Payment_Frame, orient='vertical', command=text.yview)
text.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side='right', fill='y')
text.pack(fill='both', expand=True)

CASH_BTN = Button(Payment_Frame, text='Cash', width=44, height=4, bg='light green')
text.window_create('end', window=CASH_BTN)
text.insert('end', '\n')

RuPay_BTN = Button(Payment_Frame, text='RuPay', width=44, height=3, command=RUPAY)
text.window_create('end', window=RuPay_BTN)
text.insert('end', '\n')

AmericanExpress_BTN = Button(Payment_Frame, text='AmericanExpress', width=44, height=3, command=AMERICANEXPRESS)
text.window_create('end', window=AmericanExpress_BTN)
text.insert('end', '\n')

Mastercard_BTN = Button(Payment_Frame, text='Mastercard', width=44, height=3, command=MASTERCARD)
text.window_create('end', window=Mastercard_BTN)
text.insert('end', '\n')

VISA_BTN = Button(Payment_Frame, text='VISA', width=44, height=3, command=_VISA)
text.window_create('end', window=VISA_BTN)
text.insert('end', '\n')

AmazonPay_BTN = Button(Payment_Frame, text='AmazonPay', width=44, height=3, command=AMAZONPAY)
text.window_create('end', window=AmazonPay_BTN)
text.insert('end', '\n')

Paytm_BTN = Button(Payment_Frame, text='Paytm', width=44, height=3, command=PAYTM)
text.window_create('end', window=Paytm_BTN)
text.insert('end', '\n')

PhonePe_BTN = Button(Payment_Frame, text='PhonePe', width=44, height=3, command=PHONEPE)
text.window_create('end', window=PhonePe_BTN)
text.insert('end', '\n')

Freecharge_BTN = Button(Payment_Frame, text='Freecharge', width=44, height=3, command=FREECHARGE)
text.window_create('end', window=Freecharge_BTN)
text.insert('end', '\n')

Mobikwik_BTN = Button(Payment_Frame, text='Mobikwik', width=44, height=3, command=MOBIKWIK)
text.window_create('end', window=Mobikwik_BTN)
text.insert('end', '\n')

BHIM_UPI_BTN = Button(Payment_Frame, text='BHIM_UPI', width=44, height=3, command=BHIMUPI)
text.window_create('end', window=BHIM_UPI_BTN)
text.insert('end', '\n')

HDFC_BTN = Button(Payment_Frame, text='HDFC', width=44, height=3, command=_HDFC)
text.window_create('end', window=HDFC_BTN)
text.insert('end', '\n')

SBI_BTN = Button(Payment_Frame, text='SBI', width=44, height=3, command=_SBI)
text.window_create('end', window=SBI_BTN)
text.insert('end', '\n')

ICICI_BTN = Button(Payment_Frame, text='ICICI', width=44, height=3, command=_ICICI)
text.window_create('end', window=ICICI_BTN)
text.insert('end', '\n')

Axis_BTN = Button(Payment_Frame, text='Axis', width=44, height=3, command=AXIS)
text.window_create('end', window=Axis_BTN)
text.insert('end', '\n')

Kotak_BTN = Button(Payment_Frame, text='Kotak', width=44, height=3, command=KOTAK)
text.window_create('end', window=Kotak_BTN)
text.insert('end', '\n')

Zeta_BTN = Button(Payment_Frame, text='Zeta', width=44, height=3, command=ZETA)
text.window_create('end', window=Zeta_BTN)
text.insert('end', '\n')

Sodexo_BTN = Button(Payment_Frame, text='Sodexo', width=44, height=3, command=SODEXO)
text.window_create('end', window=Sodexo_BTN)

text.configure(state='disabled')
'''

Text_Receipt_initial()

root.tk_focusFollowsMouse()
root.mainloop()
