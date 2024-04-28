from tkinter import *
import tkinter.messagebox
import Dbmssqlconnector


class USER:
    def __init__(self,root):
        self.root = root
        self.root.title('User Database Management System')
        self.root.geometry('1350x750+0+0')
        self.root.config(bg='cadet blue')

        UserID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        # =============================================== Functions ================================================= #

        def iExit():
            iExit = tkinter.messagebox.askyesno('User Database Management System','Confirm if you want to exit ?')
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtUserID.delete(0, END)
            self.txtfna.delete(0, END)
            self.txtSna.delete(0, END)
            self.txtDoB.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtAdr.delete(0, END)
            self.txtMobile.delete(0, END)

        def addData():
            if len(UserID.get()) !=0:
                Dbmssqlconnector.addUsrRec(UserID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get())
                userlist.delete(0,END)
                userlist.insert(END,(UserID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()))

        def DisplayData():
            userlist.delete(0,END)
            for row in Dbmssqlconnector.viewData():
                userlist.insert(END,row,str(''))

        def UserRec(event):
            global sd
            searchUser = userlist.curselection()
            sd = userlist.get(searchUser)

            self.txtUserID.delete(0,END)
            self.txtUserID.insert(END,sd[1])
            self.txtfna.delete(0,END)
            self.txtfna.insert(END,sd[2])
            self.txtSna.delete(0,END)
            self.txtSna.insert(END,sd[3])
            self.txtDoB.delete(0,END)
            self.txtDoB.insert(END,sd[4])
            self.txtAge.delete(0,END)
            self.txtAge.insert(END,sd[5])
            self.txtGender.delete(0,END)
            self.txtGender.insert(END,sd[6])
            self.txtAdr.delete(0,END)
            self.txtAdr.insert(END,sd[7])
            self.txtMobile.delete(0,END)
            self.txtMobile.insert(END,sd[8])


        def DeleteData():
            global sd
            if len(UserID.get()) != 0:
                Dbmssqlconnector.deleteRec(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            userlist.delete(0,END)
            for row in Dbmssqlconnector.searchData(UserID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()):
                userlist.insert(END,row,str(''))

        def update():
            if len(UserID.get()) != 0:
                Dbmssqlconnector.deleteRec(sd[0])

            if len(UserID.get()) != 0:
                Dbmssqlconnector.addUsrRec(UserID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get())
                userlist.delete(0,END)
                userlist.insert(END,(UserID.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()))


        #=================================================== Frame ======================================================#
        MainFrame = Frame(self.root, bg='cadet blue')
        MainFrame.grid()

        TitFrame = Frame(MainFrame,bd=2,padx=14,pady=6, bg='Ghost White',relief='ridge')
        TitFrame.pack(side='top')

        self.lblTit = Label(TitFrame,font=('Comic Sans MS',40,'bold'),text='User Database Management System',bg='Ghost White')
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame,bd=10,width=1350,height=70,padx=18,pady=10, bg='Ghost White',relief='ridge')
        ButtonFrame.pack(side='bottom')

        DataFrame = Frame(MainFrame,bd=1,width=1300,height=400,padx=10,pady=20, bg='cadet blue',relief='ridge')
        DataFrame.pack(side='bottom')

        DataFrameLEFT = LabelFrame(DataFrame,bd=1,width=1000,height=600,padx=15, bg='Ghost White',relief='ridge',font=('Comic Sans MS',20,'bold'),text='User Info\n')
        DataFrameLEFT.pack(side='left')

        DataFrameRIGHT = LabelFrame(DataFrame,bd=1,width=450,height=300,padx=11,pady=3, bg='Ghost White',relief='ridge',font=('Comic Sans MS',16,'bold'),text='User Details\n')
        DataFrameRIGHT.pack(side='right')

        #===================================== Labels and Entry Widget ===============================================#

        self.lblUserID = Label(DataFrameLEFT,font=('Comic Sans MS',20,'bold'),text='User ID: ',padx=2,pady=2,bg='Ghost White')
        self.lblUserID.grid(row=0,column=0,sticky=W)
        self.txtUserID = Entry(DataFrameLEFT,font=('Comic Sans MS',20,'bold'),textvariable=UserID,width=39)
        self.txtUserID.grid(row=0,column=1)

        self.lblfna = Label(DataFrameLEFT,font=('Comic Sans MS',20,'bold'),text='Firstname: ',padx=2,pady=2,bg='Ghost White')
        self.lblfna.grid(row=1,column=0,sticky=W)
        self.txtfna = Entry(DataFrameLEFT,font=('Comic Sans MS',20,'bold'),textvariable=Firstname,width=39)
        self.txtfna.grid(row=1,column=1)

        self.lblSna = Label(DataFrameLEFT,font=('Comic Sans MS',20,'bold'),text='Surname: ',padx=2,pady=2,bg='Ghost White')
        self.lblSna.grid(row=2,column=0,sticky=W)
        self.txtSna = Entry(DataFrameLEFT,font=('Comic Sans MS',20,'bold'),textvariable=Surname,width=39)
        self.txtSna.grid(row=2,column=1)

        self.lblDoB = Label(DataFrameLEFT,font=('Comic Sans MS',20,'bold'),text='Date of Birth: ',padx=2,pady=3,bg='Ghost White')
        self.lblDoB.grid(row=3,column=0,sticky=W)
        self.txtDoB = Entry(DataFrameLEFT,font=('Comic Sans MS',20,'bold'),textvariable=DoB,width=39)
        self.txtDoB.grid(row=3,column=1)

        self.lblAge = Label(DataFrameLEFT,font=('Comic Sans MS',20,'bold'),text='Age: ',padx=2,pady=3,bg='Ghost White')
        self.lblAge.grid(row=4,column=0,sticky=W)
        self.txtAge = Entry(DataFrameLEFT,font=('Comic Sans MS',20,'bold'),textvariable=Age,width=39)
        self.txtAge.grid(row=4,column=1)

        self.lblGender = Label(DataFrameLEFT,font=('Comic Sans MS',20,'bold'),text='Gender: ',padx=2,pady=3,bg='Ghost White')
        self.lblGender.grid(row=5,column=0,sticky=W)
        self.txtGender = Entry(DataFrameLEFT,font=('Comic Sans MS',20,'bold'),textvariable=Gender,width=39)
        self.txtGender.grid(row=5,column=1)

        self.lblAdr = Label(DataFrameLEFT,font=('Comic Sans MS',20,'bold'),text='Address: ',padx=2,pady=3,bg='Ghost White')
        self.lblAdr.grid(row=6,column=0,sticky=W)
        self.txtAdr = Entry(DataFrameLEFT,font=('Comic Sans MS',20,'bold'),textvariable=Address,width=39)
        self.txtAdr.grid(row=6,column=1)

        self.lblMobile = Label(DataFrameLEFT,font=('Comic Sans MS',20,'bold'),text='Mobile: ',padx=2,pady=3,bg='Ghost White')
        self.lblMobile.grid(row=7,column=0,sticky=W)
        self.txtMobile = Entry(DataFrameLEFT,font=('Comic Sans MS',20,'bold'),textvariable=Mobile,width=39)
        self.txtMobile.grid(row=7,column=1)

        #========================================ListBox & Scrollbar Widget ================================================#

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        userlist = Listbox(DataFrameRIGHT,width=41,height=16,font=('Comic Sans MS',12,'bold'),yscrollcommand=scrollbar.set)
        userlist.bind('<<ListboxSelect>>',UserRec)
        userlist.grid(row=0,column=0)
        scrollbar.config(command = userlist.yview)

        #=================================================== Button Widget ================================================#

        self.btnAddData = Button(ButtonFrame,text='Add New',font=('Comic Sans MS',20,'bold'),height=1,width=10,bd=4,command=addData)
        self.btnAddData.grid(row=0,column=0)

        self.btnDisplayData = Button(ButtonFrame,text='Display',font=('Comic Sans MS',20,'bold'),height=1,width=10,bd=4,command=DisplayData)
        self.btnDisplayData.grid(row=0,column=1)

        self.btnClearData = Button(ButtonFrame,text='Clear',font=('Comic Sans MS',20,'bold'),height=1,width=10,bd=4,command=clearData)
        self.btnClearData.grid(row=0,column=2)

        self.btnDeleteData = Button(ButtonFrame,text='Delete',font=('Comic Sans MS',20,'bold'),height=1,width=10,bd=4,command=DeleteData)
        self.btnDeleteData.grid(row=0,column=3)

        self.btnSearchData = Button(ButtonFrame,text='Search',font=('Comic Sans MS',20,'bold'),height=1,width=10,bd=4,command=searchDatabase)
        self.btnSearchData.grid(row=0,column=4)

        self.btnUpdateData = Button(ButtonFrame,text='Update',font=('Comic Sans MS',20,'bold'),height=1,width=10,bd=4,command=update)
        self.btnUpdateData.grid(row=0,column=5)

        self.btnExit = Button(ButtonFrame,text='Exit',font=('Comic Sans MS',20,'bold'),height=1,width=10,bd=4,command=iExit)
        self.btnExit.grid(row=0,column=6)


        menubar = Menu(MainFrame,tearoff=0)

        editmenu = Menu(menubar,tearoff=0)
        editmenu.add_cascade(label='Edit',accelerator='Alt+E',menu=editmenu)
        editmenu.add_command(label='Copy',accelerator='Ctrl+C',command=lambda:menubar.focus_get().event_generate('<<Copy>>'))
        editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=lambda:menubar.focus_get().event_generate('<<Cut>>'))
        editmenu.add_separator()
        editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=lambda:menubar.focus_get().event_generate('<<Paste>>'))

        optionmenu = Menu(menubar,tearoff=0)
        optionmenu.add_cascade(label='Options',accelerator='Alt+O',menu=optionmenu)
        optionmenu.add_command(label='Save',accelerator='Ctrl+S',command=addData)


if __name__=='__main__':
    root = Tk()
    application = USER(root)
    root.mainloop()
