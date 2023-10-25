from tkinter import*
import tkinter.messagebox as msg
import math

mainWindow = Tk()
mainWindow.title("Hesap Makinesi")
mainWindow.geometry("330x210")
mainWindow.resizable(width=False, height=False)
#mainWindow.configure(bg='white')

total = ""

def add(number):
    global total
    total = total + number
    printt()
    
def delete():
    global total
    total = total[0: len(total)-1]
    printt()
    
def clear():
    global total
    total = ""
    printt()
    
def calculate():
    global result, total
    try:
        eval(total)
    except Exception as e:
        return msg.showerror("Error", str(e))
    result.delete(0,END)
    result.insert(0, eval(total))
    total = str(eval(total))

result = Entry(width=35)#state="disabled"
result.grid(row=0, column=0, columnspan = 6, rowspan = 1)


def printt():
    global result
    result.delete(0,END)
    result.insert(0, total)


Button(text="1", width=2, height=2, command=lambda: add("1")).grid(row=1, column=0)
Button(text="2", width=2, height=2, command=lambda: add("2")).grid(row=1, column=1)
Button(text="3", width=2, height=2, command=lambda: add("3")).grid(row=1, column=2)
Button(text="+", width=2, height=2, command=lambda: add("+")).grid(row=1, column=3)
Button(text="%", width=2, height=2, command=lambda: (add("/100"), calculate()) ).grid(row=1, column=4)

Button(text="4", width=2, height=2, command=lambda: add("4")).grid(row=2, column=0)
Button(text="5", width=2, height=2, command=lambda: add("5")).grid(row=2, column=1)
Button(text="6", width=2, height=2, command=lambda: add("6")).grid(row=2, column=2)
Button(text="-", width=2, height=2, command=lambda: add("-")).grid(row=2, column=3)

Button(text="7", width=2, height=2, command=lambda: add("7")).grid(row=3, column=0)
Button(text="8", width=2, height=2, command=lambda: add("8")).grid(row=3, column=1)
Button(text="9", width=2, height=2, command=lambda: add("9")).grid(row=3, column=2)
Button(text="0", width=2, height=2, command=lambda: add("0")).grid(row=4, column=1)
Button(text=",", width=2, height=2, command=lambda: add(".")).grid(row=4, column=0)
Button(text="C", width=2, height=2, command= clear).grid(row=4, column=4)
Button(text="←", width=2, height=2, command= delete).grid(row=3, column=4)
Button(text="*", width=2, height=2, command=lambda: add("*")).grid(row=3, column=3)
Button(text="/", width=2, height=2, command=lambda: add("/")).grid(row=4, column=3)

Button(text="=", width=2, height=2, command=calculate ).grid(row=4, column=2)

mainWindow.mainloop()
