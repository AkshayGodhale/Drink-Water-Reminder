from tkinter import *# import everything from tkinter module

expression = ""# globally declare the expression variable

def press(num):

	global expression
	expression = expression + str(num)
	equation.set(expression)
 
def equalpress():

	try:

		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""
  
  	# if error is generate then handle
	# by the except block
	except:

		equation.set(" error ")
		expression = ""
  
def clear():
	global expression
	expression = ""
	equation.set("")

# Driver code
if __name__ == "__main__":
	gui = Tk()
 	# StringVar() is the variable class
	# we create an instance of this class
	equation = StringVar()
	expression_field = Entry(gui,border=5,  textvariable=equation)
	expression_field.place(x=100, y=150,height=170, width=230 )
 
gui.configure(background="light green")


button1 = Button(gui, text=' 50ml ', fg='blue',
					command=lambda: press(50  ), height=1, width=7)
button1.place(x=20, y=100)

button2 = Button(gui, text=' 100ml ', fg='blue',
					command=lambda: press(100) , height=1, width=7)
button2.place(x=90, y=100)

button3 = Button(gui, text=' 150ml ', fg='blue',
					command=lambda: press(150), height=1, width=7)
button3.place(x=160, y=100)

button4 = Button(gui, text=' 250ml ', fg='blue',
					command=lambda: press(250), height=1, width=7)
button4.place(x=230, y=100)

button5 = Button(gui, text=' 350ml ', fg='blue',
					command=lambda: press(350), height=1, width=7)
button5.place(x=300, y=100)

button6 = Button(gui, text=' 500ml ', fg='blue',
					command=lambda: press(500), height=1, width=7)
button6.place(x=370, y=100)

plus = Button(gui, text=' TOTAL ', fg='black',
				command=lambda: press("+"), height=1, width=7)
plus.place(x=25, y=300)

equal = Button(gui, text=' TOTAL ', fg='black',
				command=equalpress, height=1, width=7)
equal.place(x=20, y=300)


lbl=Label(gui, text="Time to drink some water", fg='red', font=("Helvetica", 16))
lbl.place(x=100, y=50)

lbl=Label(gui, text="Amount of water                              water in ml", fg='Dark blue', font=("Helvetica", 8))
lbl.place(x=100, y=150)

gui.title('Drink Water Reminder')
gui.geometry("450x400+10+20")
gui.mainloop()