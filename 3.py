# from tkinter import *

# def insert():
#     entry.insert(0, "Hello")

# def delete():
#     entry.delete(0,END)    

# root = Tk()
# root.title("My first app")
# # root.minsize(300*450)
# root.geometry("200x140")

# label = Label(text="Say hello", font=("Arial",16,"bold"))
# label.config(bd=10)
# label.pack()

# entry = Entry(width=30)
# entry.pack()

# buttonInsept = Button(text = "Click me",background="#ffffff", fg = "#000000",width = 10, height = 1)
# buttonInsept.config(command=insert)
# buttonInsept.pack(side = LEFT,padx=10,pady=15)

# buttonDelete = Button(text = "Delete", bg ="#ffffff",width=10,height = 1)
# buttonDelete.config(command=delete)
# buttonDelete.pack(side=RIGHT,padx=10,pady=15)

# root.mainloop()

# from tkinter import*

# def red():
#     label.config(text="Red")
#     entry.delete(0,END)
#     entry.insert(0,"B21B0C")


# root = Tk()
# root.title("colors")
# root.geometry("180x240")

# label = Label(root, anchor="c",) 
# label.pack()

# entry = Entry(root,justify="center",bd = 5)
# entry.pack()

# buttonRed = Button(width = 16,bg="red",command=red)
# buttonRed.pack()
# root.mainloop()


# from tkinter import*

# def name():
#     entry.get(0,END)

# def show():
#     name = entry.get()
#     surname = entry2.get()
#     fullname = f"Name : {name} Surname : {surname}"
#     label3.config(text = fullname)

# root = Tk()
# root.title("Name")
# root.geometry("180x240")
# label = Label(root,anchor="c")
# label.pack()
# label2 = Label(root,anchor="c")
# label2.pack()
# entry = Entry(root,justify="left",bd=2)
# entry.pack()
# entry2 = Entry(root,justify="left",bd=2)
# entry2.pack()
# button = Button(root,text = "Show",font=("Arial",10),width=13,height=1 )
# button.config(bd=5,command=show)
# button.pack()
# label3= Label(root,anchor="c")
# label3.pack()
# root.mainloop()


from tkinter import*
def sum():
    buttonSum.getdouble(0,END)
    
def Sum():
    num1 = float(entry.get())
    num2 = float(entry2.get())
    result = f"Result{num1+num2}"
    label2.config(text=result)
   


root = Tk()
root.title("Calculate")
root.geometry("180x240")
label = Label(root,anchor="c")
label.pack()
label2 = Label(root,anchor="c")
label2.pack()
entry = Entry(root,justify="left",bd=2)
entry.pack()
entry2 = Entry(root,justify="left",bd=2)
entry2.pack()
buttonSum = Button(root,text = "Sum",command=Sum)
buttonSum.pack()
buttonMin = Button(root,text ="Min")
buttonMin.pack()
buttonDil = Button(root,text="Dil")
buttonDil.pack()
buttonMn = Button(root,text="Mn")
buttonMn.pack()
label2= Label(root)
label2.pack()
root.mainloop()