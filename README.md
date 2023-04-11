# A simple calculator GUI built using Python and the Tkinter library.

# Usage:
To use the calculator, simply run the calculator.py file.

# Dependencies:
The calculator requires the Tkinter library, which should be included with most Python installations.

# Development:
To make changes to the calculator, modify the calculator.py file.

# Buttons:
Numbers: Click on the buttons with numbers to input them into the calculator.
Operators: Click on the buttons with operators (+, -, *, /, %) to perform calculations.
Clear: Click on the C button to clear the calculator's input.
Equal: Click on the = button to evaluate the calculator's input and display the result.

# Algorithm:
step1:Import the tkinter library.
step2:Define a class named Calculator that takes in a master parameter.
step3:Initialize the class by setting the master parameter to the instance variable master and setting the title of the window to "Calculator".
step4:Create an Entry widget and set its width to 25, font to Arial 16, and add padding of 10 pixels to the left and right, and top and bottom.
step5:Create buttons for numbers 1 to 9, 0, and decimal point, and mathematical operators +, -, *, /, and %, and set their position on the grid using the create_button method.
step6:Define the create_button method that takes in text, row, column, rowspan, and columnspan parameters.
step7:Create a Button widget with text, width, height, font, and command attributes, and set its position on the grid using the grid method.
step8:Define the button_click method that takes in a text parameter.
step9:If the text is "C", clear the entry widget.
step10:If the text is "=", evaluate the expression entered in the entry widget using the eval method, clear the entry widget, and insert the result.
step11:If the text is any other number or operator, insert it into the entry widget.
step12:Create a Tk() instance named root.
step13:Create an instance of the Calculator class named calculator with root as its parameter.
step14:Call the mainloop() method of the root window to start the event loop.

# Credits:
The calculator was developed by Sanniboina Deepika.

