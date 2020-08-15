from tkinter import *
import math

class calculator():  #calculator object initialization

    def __init__(self): #initialization
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def display(self, value): #displaying input to screen
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def sign(self): #plus or minus function
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self): # square root function
        self.Result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def clear_entry(self): # clearing current entry
        self.Result = False
        self.current = '0'
        self.display(0)
        self.input_value = True

    def clear_all(self): # clearing total
        self.clear_entry()
        self.total = 0

    def insert_value(self, value): # inserting a number onto the screen
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(value)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self): #equals function
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def valid_function(self): #determining which operation to use
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total/= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)


    def operation(self, op): #adding text value in order to determine if function is valid
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False



added_value = calculator()
root = Tk()
root.title('calculator')
#root.resizeable(width = False, height = False)
calc = Frame(root)
calc.grid()
label = Label(calc, bg = 'red')
#label.pack()
txtDisplay = Entry(calc, font =('arial', 20, 'bold'), bg = 'powder blue', bd = 30, width = 28, justify = RIGHT) #initializing the text display box as an Entry to calculators frame
txtDisplay.grid(row = 0, column = 0, columnspan = 4, pady = 1)
txtDisplay.insert(0, '0')

#first row_______________________
CE_button = Button(calc , pady = 1, bd = 4, fg = 'black', font =('arial',20, 'bold'), width = 6, height = 2, text = 'CE', bg = "red", command = added_value.clear_entry).grid(row = 1, column = 0) #clear entry
C_button = Button(calc, pady = 1, fg = 'black', bd = 4, font = ('arial', 20, 'bold'), height = 2, width = 6, text = 'CA', bg = 'red', command = added_value.clear_all).grid(row = 1, column = 1) #clear all memory button
sqrt_button = Button(calc, pady = 1,fg = 'black', bd = 4, font = ('arial', 20, 'bold'), height = 2, width = 6, text = u"\u221A", bg = 'red', command = added_value.squared).grid(row = 1, column = 2) # square root button
add_button = Button(calc, pady = 1, fg = 'black', bd = 4, font=('arial', 20, 'bold'), height = 2, width = 6, text = '+', bg = 'red', command = lambda: added_value.operation("add")).grid(row = 1, column = 3) #add button
#Second row______________________
btn9 = Button(calc, pady = 1, bd = 4, font = ('arial', 20, 'bold'), width = 6, height = 2, text = '9', bg = 'powder blue', command = lambda: added_value.insert_value('9')).grid(row = 2, column = 2)
btn8 = Button(calc, pady = 1, bd = 4, font = ('arail',20,'bold'), width = 6, height = 2, text = '8', bg = "powder blue",command = lambda: added_value.insert_value('8')).grid(row = 2, column = 1)
btn7 = Button(calc, pady=1, bd=4,  font =('arial', 20, 'bold'), width = 6, height = 2, text = '7', bg = "powder blue",command = lambda: added_value.insert_value('7')).grid(row = 2, column = 0)
btn_sub = Button(calc, pady = 1, bd = 4, font=('arial', 20, 'bold'), width = 6, height = 2, text = '-', bg = 'red',command = lambda: added_value.operation("sub")).grid(row = 2, column = 3)
#row three_______________________
btn6 = Button(calc, pady=1, bd=4, font=('arial', 20, 'bold'), width = 6, height = 2,text = '6', bg = 'powder blue',command = lambda: added_value.insert_value('6')).grid(row = 3, column = 2)
btn5 = Button(calc, pady = 1, bd=4, font=('arial', 20, 'bold'), width = 6, height = 2, text = '5', bg = 'powder blue',command = lambda: added_value.insert_value('5')).grid(row = 3, column = 1)
btn4 = Button(calc, pady = 1, bd=4, font=('arial', 20, 'bold'), width = 6, height = 2, text = '4', bg = 'powder blue',command = lambda: added_value.insert_value('4')).grid(row = 3, column = 0)
btn_mult = Button(calc, pady = 1, bd = 4, font = ('arial', 20, 'bold'), width = 6, height = 2, text = '*', bg = 'red',command = lambda: added_value.operation("multi")).grid(row = 3, column = 3)
#row four_______________________
btn3 = Button(calc, pady = 1, bd= 4, font =('arial', 20, 'bold'), width = 6, height =2, text = '3', bg = 'powder blue',command = lambda: added_value.insert_value('3')).grid(row = 4 , column = 2)
btn2 = Button(calc, pady = 1, bd = 4, font = ('arial', 20, 'bold'), width = 6, height =2, text = '2', bg = 'powder blue',command = lambda: added_value.insert_value('2')).grid(row = 4, column = 1)
btn1 = Button(calc, pady = 1, bd = 4, font = ('arial', 20, 'bold'), width = 6, height = 2,text = '1', bg = 'powder blue', command = lambda: added_value.insert_value('1')).grid(row = 4, column =0)
btn_div = Button(calc, pady = 1, bd = 4, fg= 'black', font=('arial', 20, 'bold'), width = 6, height = 2 , text = '/', bg = 'red',command = lambda: added_value.operation("divide")).grid(row = 4, column = 3)
#row five_____________________
btn0 = Button(calc,pady = 1, bd = 4, font = ('arial', 20, 'bold'), width = 6, height = 2, text = '0',bg = 'powder blue',command = lambda: added_value.insert_value('0')).grid(row = 5, column = 0)
DotBtn = Button(calc,pady = 1, bd = 4, font = ('arial', 20, 'bold'), width = 6, height = 2, text = '0',bg = 'powder blue', command = lambda: added_value.insert_value('.')).grid(row = 5, column = 1)
btnPM = Button(calc, pady = 1, bd = 4, font = ('arial', 20, 'bold'), width = 6, height = 2, text = chr(177), bg= 'powder blue', command = added_value.sign).grid(row = 5, column = 2)
btnEq = Button(calc, pady = 1, bd = 4, font = ('arial', 20, 'bold'), height = 2, width = 6, text = '=', bg = 'powder blue', command = added_value.sum_of_total).grid(row = 5, column = 3)




root.mainloop()