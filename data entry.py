from tkinter import *
root=Tk()



Label(root,text="Welcome to Hardik's Gui " ,font= "Arial 16 italic").grid(row=0,column=0)
name=Label(root,text="Name")
phone=Label(root,text="Phone")
Gender=Label(root,text="Gender")
Payment=Label(root,text="Payment")
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
Gender.grid(row=3,column=2)
Payment.grid(row=4,column=2)

nameval=StringVar()
phoneval=StringVar()
genderval=StringVar()
paymentval=StringVar()
foodservicetval=IntVar()

def getval():
    print("submitted succesfully")
    print(f"{nameval.get(),phoneval.get(),genderval.get(),paymentval.get(),foodservicetval.get()}\n")

    with open("record.txr",'a') as f:
        f.write(f"{nameval.get(),phoneval.get(),genderval.get(),paymentval.get(),foodservicetval.get()}\n")

nameentry=Entry(root,textvariable=nameval)
phonentry=Entry(root,textvariable=phoneval)
genderentry=Entry(root,textvariable=genderval)
paymententry=Entry(root,textvariable=paymentval)




nameentry.grid(row=1,column=3)
phonentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
paymententry.grid(row=4,column=3)

#chechbox
foodservice=Checkbutton(text="Want to Pre book meal",variable=foodservicetval)
foodservice.grid(row=6,column=3)

Button(text="Submit to My program",command=getval).grid(row=7,column=3)





root.mainloop()
