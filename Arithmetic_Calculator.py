import tkinter as tk

# Step 1: Create a window and its attributes
window = tk.Tk()  # Create a Window
window.title('Arithmetic Calculator')  # set window title
window.geometry('320x200')  # Set the window size ('widthxheight')


# Step 4: define the functions for buttons
def addition():
    try:
        # Code inside try block watches/monitor for runtime errors (exceptions)
        # fetch the data from text fields
        n1 = int(ent_number1.get())
        n2 = int(ent_number2.get())
        result = n1 + n2
        ent_answer['state'] = 'normal'
        ent_answer.delete(0, tk.END)
        ent_answer.insert(0, str(result))
        ent_answer['state'] = 'disabled'
    except:
        # Program control enter here if runtime error occurs
        ent_answer['state'] = 'normal'
        ent_answer.delete(0, tk.END)
        ent_answer.insert(0, 'Not a Number')
        ent_answer['state'] = 'disabled'


def subtraction():
    try:
        # Code inside try block watches/monitor for runtime errors (exceptions)
        # fetch the data from text fields
        n1 = int(ent_number1.get())
        n2 = int(ent_number2.get())
        result = n1 - n2
        ent_answer['state'] = 'normal'
        ent_answer.delete(0, tk.END)
        ent_answer.insert(0, str(result))
        ent_answer['state'] = 'disabled'
    except:
        # Program control enter here if runtime error occurs
        ent_answer['state'] = 'normal'
        ent_answer.delete(0, tk.END)
        ent_answer.insert(0, 'Not a Number')
        ent_answer['state'] = 'disabled'


def multiplication():
    try:
        # Code inside try block watches/monitors for runtime errors (exceptions)
        # fetch the data from text fields
        n1 = int(ent_number1.get())
        n2 = int(ent_number2.get())
        result = n1 * n2
        ent_answer['state'] = 'normal'
        ent_answer.delete(0, tk.END)
        ent_answer.insert(0, str(result))
        ent_answer['state'] = 'disabled'
    except:
        # Program control enter here if runtime error occurs
        ent_answer['state'] = 'normal'
        ent_answer.delete(0, tk.END)
        ent_answer.insert(0, 'Not a Number')
        ent_answer['state'] = 'disabled'


def division():
    try:
        # Code inside try block watches/monitors for runtime errors (exceptions)
        # fetch the data from text fields
        n1 = int(ent_number1.get())
        n2 = int(ent_number2.get())
        result = n1 / n2
        ent_answer['state'] = 'normal'
        ent_answer.delete(0, tk.END)
        ent_answer.insert(0, str(result))
        ent_answer['state'] = 'disabled'
    except ValueError:
        # Program control enter here if runtime error occurs
        ent_answer['state'] = 'normal'
        ent_answer.delete(0, tk.END)
        ent_answer.insert(0, 'Not a Number')
        ent_answer['state'] = 'disabled'
    except ZeroDivisionError:
        ent_answer['state'] = 'normal'
        ent_answer.delete(0, tk.END)
        ent_answer.insert(0, 'Infinity')
        ent_answer['state'] = 'disabled'


# Step 2: Create widgets inside the window ( Label , Entry , Button
lbl_number1 = tk.Label(master=window, text='Enter First Number')
lbl_number2 = tk.Label(master=window, text='Enter Second Number')
lbl_answer = tk.Label(master=window, text='Answer')

ent_number1 = tk.Entry(master=window, width=20)
ent_number2 = tk.Entry(master=window, width=20)
ent_answer = tk.Entry(master=window, width=20)
# setting answer field as disabled
ent_answer['state'] = 'disabled'

button_add = tk.Button(master=window, text='ADD', width=8, command=addition)
button_sub = tk.Button(master=window, text='SUBTRACT', width=8, command=subtraction)
button_mul = tk.Button(master=window, text='MULTIPLY', width=8, command=multiplication)
button_div = tk.Button(master=window, text='DIVIDE', width=8, command=division)

# Step 3: Adding the widgets to the window
# window.place() is used for explicit positioning
lbl_number1.place(x=20, y=20)
lbl_number2.place(x=20, y=60)
lbl_answer.place(x=20, y=100)

ent_number1.place(x=170, y=20)
ent_number2.place(x=170, y=60)
ent_answer.place(x=170, y=100)

button_add.place(x=10, y=140)
button_sub.place(x=85, y=140)
button_mul.place(x=160, y=140)
button_div.place(x=235, y=140)

# this mainloop keep the window alive and listen for events and react
window.mainloop()
