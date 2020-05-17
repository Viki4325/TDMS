from tkinter import *
import tkinter.messagebox
from tkinter import Scrollbar
from tkinter.ttk import Treeview

import tenants_BackEnd


class Tenants:
    def __init__(self, root):
        self.root = root
        self.root.title("Tenants Database Managment System")
        self.root.geometry("1450x850")
        self.root.config(bg="grey")

        # variables
        AptNo = StringVar()
        Fname1= StringVar()
        Lname1 = StringVar()
        Fname2=StringVar()
        Lname2=StringVar()
        phoneNo = StringVar()
        workPhoneNo = StringVar()
        parkingStallNo = StringVar()
        canopyStallNo = StringVar()
        email = StringVar()
        Description = StringVar()

        # --------------Functions-----------------------------------
        def iExit():
            iExit = tkinter.messagebox.askyesno("Tenants Database Management System", "Confirm if you want to Exit")
            if (iExit):
                root.destroy()
                return

        def clearData():
            self.txtAptNo.delete(0, END)
            self.txtFname1.delete(0,END)
            self.txtLname1.delete(0,END)
            self.txtFname2.delete(0,END)
            self.txtLname2.delete(0,END)
            self.txtphoneNo.delete(0, END)
            self.txtworkNo.delete(0, END)
            self.txtparking.delete(0, END)
            self.txtcanopy.delete(0, END)
            self.txtextra.delete(0, END)

        def addData():
            if len(AptNo.get()) != 0:
                tenants_BackEnd.addTenantRcd(AptNo.get(), Fname1.get(), Lname1.get(), Fname2.get(), Lname2.get() ,phoneNo.get(), workPhoneNo.get(), parkingStallNo.get(), canopyStallNo.get(), Description.get())

                tenantList.delete(0, END)
                tenantList.insert(END, (AptNo.get() ,Fname1.get(),Lname1.get(),Fname2.get(), Lname2.get(),phoneNo.get(), workPhoneNo.get(), parkingStallNo.get(), canopyStallNo.get(), Description.get()))
             else:
                tkinter.messagebox.showerror("Tenant Database Management System ERROR", "SUITE / UNIT NUMBER MUST BE INCLUDED!!")

        def show():
            frame = Tk()

            cols = (
                'Unit', 'First Name', 'Last Name', '2. First Name', '2. Last Name', 'Personal Phone No.', 'Work Phone No.', 'Parking Stall No.', 'Canopy Stall No.',
                'Extra Info')
            tree = ttk.Treeview(frame, columns=cols, show='headings')
            tree.pack(side='left')

            # set the heading
            for col in cols:
                tree.heading(col, text=col)

            scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
            scroll.pack(side='right', fill='y')

            tree.configure(yscrollcommand=scroll.set)
            i = 0
            for val in tenants_BackEnd.viewData():
                tree.insert('', 'end', values=(
                    tenants_BackEnd.viewData()[i][1], tenants_BackEnd.viewData()[i][2],
                    tenants_BackEnd.viewData()[i][3],
                    tenants_BackEnd.viewData()[i][4], tenants_BackEnd.viewData()[i][5], tenants_BackEnd.viewData()[i][6]
                    , tenants_BackEnd.viewData()[i][7], tenants_BackEnd.viewData()[i][8],
                    tenants_BackEnd.viewData()[i][9]))
                i = i + 1
            # RemoveButton = Button(frame, text="Remove", width=15, command=DeleteData())
            frame.mainloop()
            
        def DisplayData():
            tenantList.delete(0,END)
            for row in tenants_BackEnd.viewData():
             tenantList.insert(END, row, str(""))
            show()
           

        def TenantRec(event):
            global td
            searchStd = tenantList.curselection()[0]
            td = tenantList.get(searchStd)

            self.txtAptNo.delete(0, END)
            self.txtAptNo.insert(END, td[1])
            
            self.txtFname1.delete(0, END)
            self.txtFname1.insert(END, td[2])
            
            self.txtLname1.delete(0,END)
            self.txtLname1.insert(END,td[3])

            self.txtFname2.delete(0, END)
            self.txtFname2.insert(END, td[4])
            
            self.txtLname2.delete(0, END)
            self.txtLname2.insert(END, td[5])

            self.txtphoneNo.delete(0, END)
            self.txtphoneNo.insert(END, td[6])
            
            self.txtworkNo.delete(0, END)
            self.txtworkNo.insert(END, td[7])
            
            self.txtparking.delete(0, END)
            self.txtparking.insert(END, td[8])
            
            self.txtcanopy.delete(0, END)
            self.txtcanopy.insert(END, td[9])
            
            self.txtextra.delete(0, END)
            self.txtextra.insert(END, td[10])

        def DeleteData():
            if (len(AptNo.get()) != 0):
                ask=tkinter.messagebox.askokcancel(Tenant Database Management System WARNING","Are you sure you want to permanently remove this record?")
                if(ask):                                 
                    tenants_BackEnd.deleteRec(td[0]) #0 INSTEAD OF 0
                    clearData()
                    DisplayData()

        def searchDatabase():
            tenantList.delete(0, END)
            for row in tenants_BackEnd.searchData(AptNo.get(), Fname1.get(), Lname1.get() ,Fname2.get(), Lname2.get(),phoneNo.get(), workPhoneNo.get(), parkingStallNo.get(), canopyStallNo.get(), Description.get()):
                tenantList.insert(END, row, str(""))

        def update():
            if (len(AptNo.get()) != 0):
                tenants_BackEnd.deleteRec(td[0])
            if (len(AptNo.get()) != 0):
                tenants_BackEnd.addTenantRcd(AptNo.get(), Fname1.get(),Lname1.get(),Fname2.get(),Lname2.get() ,phoneNo.get(), workPhoneNo.get(), parkingStallNo.get(),
                                             canopyStallNo.get(), Description.get())
                tenantList.delete(0, END)
                tenantList.insert(AptNo.get(), Fname1.get(), Lname1.get(), Fname2.get(),Lname2.get(),phoneNo.get(), workPhoneNo.get(), parkingStallNo.get(), canopyStallNo.get(), Description.get())

        # ------------Main Frame----------#
        mainFrame = Frame(self.root, bg="grey")
        mainFrame.grid()

        TitFrame = Frame(mainFrame, bd=2, padx=50, pady=8, bg="grey")
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Tenant Database Management System",
                            bg="orange")
        self.lblTit.grid()

        ButtonFrame = Frame(mainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(mainFrame, bd=4, width=2000, height=600, padx=20, pady=20, relief=RIDGE, bg="grey")
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=500, height=600, padx=10, relief=RIDGE, bg="ghost white",
                                   font=('raleway', 25, 'bold'), text="Tenant Information\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, pady=3,
                                    bg="ghost white", font=('raleway', 25, 'bold'), text="Tenant Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

        # --------------------------------------------Labels an Entry Widgets----------------------------------------------------------
        self.txtAptNo = Label(DataFrameLEFT, font=('raleway', 20, 'italic'), text="Apartment No", padx=2, pady=2,
                              bg="ghost white")
        self.txtAptNo.grid(row=0, column=0, sticky=W)
        self.txtAptNo = Entry(DataFrameLEFT, font=('raleway', 20, 'italic'), textvariable=AptNo, width=30)
        self.txtAptNo.grid(row=0, column=1)

        self.txtFname1 = Label(DataFrameLEFT, font=('raleway', 20, 'italic'), text="Tenant 1 FirstName", padx=2, pady=2,
                               bg="ghost white")
        self.txtFname1.grid(row=1, column=0, sticky=W)
        self.txtFname1 = Entry(DataFrameLEFT, font=('raleway', 20, 'italic'), textvariable=Fname1, width=30)
        self.txtFname1.grid(row=1, column=1)

        self.txtLname1 = Label(DataFrameLEFT, font=('raleway', 20, 'italic'), text="Tenant 1 LastName ", padx=2, pady=2,
                               bg="ghost white")
        self.txtLname1.grid(row=2, column=0, sticky=W)
        self.txtLname1 = Entry(DataFrameLEFT, font=('raleway', 20, 'italic'), textvariable=Lname1, width=30)
        self.txtLname1.grid(row=2, column=1)

        self.txtFname2 = Label(DataFrameLEFT, font=('raleway', 20, 'italic'), text="Tenant 2 FirstName", padx=2, pady=2,
                               bg="ghost white")
        self.txtFname2.grid(row=3, column=0, sticky=W)
        self.txtFname2 = Entry(DataFrameLEFT, font=('raleway', 20, 'italic'), textvariable=Fname2, width=30)
        self.txtFname2.grid(row=3, column=1)

        self.txtLname2 = Label(DataFrameLEFT, font=('raleway', 20, 'italic'), text="Tenant 2 LastName ", padx=2, pady=2,
                               bg="ghost white")
        self.txtLname2.grid(row=4, column=0, sticky=W)
        self.txtLname2 = Entry(DataFrameLEFT, font=('raleway', 20, 'italic'), textvariable=Lname2, width=30)
        self.txtLname2.grid(row=4, column=1)

        self.txtphoneNo = Label(DataFrameLEFT, font=('raleway', 20, 'italic'), text="Personal(Cell) No", padx=2, pady=2,
                                bg="ghost white")
        self.txtphoneNo.grid(row=5, column=0, sticky=W)
        self.txtphoneNo = Entry(DataFrameLEFT, font=('raleway', 20, 'italic'), textvariable=phoneNo, width=30)
        self.txtphoneNo.grid(row=5, column=1)

        self.txtworkNo = Label(DataFrameLEFT, font=('raleway', 20, 'italic'), text="Work-Phone No", padx=2, pady=2,
                               bg="ghost white")
        self.txtworkNo.grid(row=6, column=0, sticky=W)
        self.txtworkNo = Entry(DataFrameLEFT, font=('raleway', 20, 'italic'), textvariable=workPhoneNo, width=30)
        self.txtworkNo.grid(row=6, column=1)

        self.txtparking = Label(DataFrameLEFT, font=('raleway', 20, 'italic'), text="Parking-Stall No", padx=2, pady=2,
                                bg="ghost white")
        self.txtparking.grid(row=7, column=0, sticky=W)
        self.txtparking = Entry(DataFrameLEFT, font=('raleway', 20, 'italic'), textvariable=parkingStallNo, width=30)
        self.txtparking.grid(row=7, column=1)

        self.txtcanopy = Label(DataFrameLEFT, font=('raleway', 20, 'italic'), text="Canopy-Stall No", padx=2, pady=2,
                               bg="ghost white")
        self.txtcanopy.grid(row=8, column=0, sticky=W)
        self.txtcanopy = Entry(DataFrameLEFT, font=('raleway', 20, 'italic'), textvariable=canopyStallNo, width=30)
        self.txtcanopy.grid(row=8, column=1)


        self.txtextra = Label(DataFrameLEFT, font=('raleway', 20, 'italic'), text="Extra Information", padx=2, pady=2,
                              bg="ghost white")
        self.txtextra.grid(row=10, column=0, sticky=W)
        self.txtextra = Entry(DataFrameLEFT, font=('raleway', 20, 'italic'), textvariable=Description, width=30)
        self.txtextra.grid(row=10, column=1)

        # ----------------------------------------------ListBox and scrollbar widget-----------------------------
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky=N+S+E+W)

        scrollbar2=Scrollbar(DataFrameRIGHT,orient="horizontal")
        scrollbar2.grid(row=1,column=0,sticky=N+S+E+W)

        tenantList1 = Listbox(DataFrameRIGHT, width=60, height=21, font=('raleway', 12, 'bold'),
                             yscrollcommand=scrollbar.set)
        tenantList = Listbox(DataFrameRIGHT, width=60, height=21, font=('raleway', 12, 'bold'),
                             xscrollcommand=scrollbar2.set)


        tenantList.bind('<<ListboxSelect>>', TenantRec)
        tenantList.grid(row=0, column=0, padx=8)

        scrollbar.config(command=tenantList1.yview)
        scrollbar2.config(command=tenantList.xview)

        # ----------------------------------------------Buttons widgets--------------------------------------------
        self.btnAddData = Button(ButtonFrame, text="Add New", font=("raleway,20,bold"), height=1, width=16, bd=4,
                                 command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=("raleway,20,bold"), height=1, width=16, bd=4,
                                     command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=("raleway,20,bold"), height=1, width=16, bd=4,
                                   command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Remove", font=("raleway,20,bold"), height=1, width=16, bd=4,
                                    command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=("raleway,20,bold"), height=1, width=16, bd=4,
                                    command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=("raleway,20,bold"), height=1, width=16, bd=4,
                                    command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="EXIT", font=("raleway,20,bold"), height=1, width=16, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)


if __name__ == '__main__':
    root = Tk()
    application = Tenants(root)
    root.mainloop()
