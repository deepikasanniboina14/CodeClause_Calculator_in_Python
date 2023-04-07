#The code is using the tkinter library to create a GUI calculator.
from tkinter import *
#The Calculator class is defined with an __init__ method that initializes the master window and sets its title.
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.entry = Entry(master, width=25, font=("Arial", 16))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#The create_button method is defined to create buttons for the calculator and set their attributes.
        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("/", 1, 3)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)
        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("-", 3, 3)
        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("+", 4, 3)
        self.create_button("%", 5, 3)
        self.create_button("C", 6, 0, 2, 2)
        self.create_button("=", 6, 0, 1, 4)
 #set their attributes. It also sets up a lambda function to handle button clicks.
    def create_button(self, text, row, column, rowspan=1, columnspan=1):
        button = Button(self.master, text=text, width=5, height=2, font=("Arial", 12), command=lambda: self.button_click(text))
        button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=5, pady=5)
#The button_click method is defined to handle button clicks based on the button text. 
#If the text is "C", the entry field is cleared. If the text is "=", the expression in the entry field is evaluated and the result is displayed in the entry field. If there is an error in the evaluation, "Error" is displayed in the entry field. Otherwise, the button text is appended to the entry field.
    def button_click(self, text):
        if text == "C":
            self.entry.delete(0, END)
        elif text == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, END)
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(END, text)
#The main program creates a Tkinter window, instantiates a Calculator object, and starts the main event loop using root.mainloop().
root = Tk()
calculator = Calculator(root)
root.mainloop()
