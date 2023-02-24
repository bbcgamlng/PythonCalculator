
import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the title and size of the window
root.title("My GUI")
root.geometry("320x500")
# Define a function to be executed when the button is clicked
def button_click1():
    print("1")
def button_click2():
    print("2")
def button_click3():
    print("3")
def button_click4():
    print("4")
def button_click5():
    print("5")
def button_click6():
    print("6")
def button_click7():
    print("7")
def button_click8():
    print("8")
def button_click9():
    print("9")
def button_click0():
    print("0")
def button_clickplus():
    print("+")

# Create the buttons and add them to the main window
button1 = tk.Button(root, text="1", command=button_click1, width=5, height=2)
button1.grid(row=0, column=0)
button2 = tk.Button(root, text="2", command=button_click2, width=5, height=2)
button2.grid(row=0, column=1)
button3 = tk.Button(root, text="3", command=button_click3, width=5, height=2)
button3.grid(row=0, column=2)
button4 = tk.Button(root, text="4", command=button_click4, width=5, height=2)
button4.grid(row=1, column=0)
button5 = tk.Button(root, text="5", command=button_click5, width=5, height=2)
button5.grid(row=1, column=1)
button6 = tk.Button(root, text="6", command=button_click6, width=5, height=2)
button6.grid(row=1, column=2)
button7 = tk.Button(root, text="7", command=button_click7, width=5, height=2)
button7.grid(row=2, column=0)
button8 = tk.Button(root, text="8", command=button_click8, width=5, height=2)
button8.grid(row=2, column=1)
button9 = tk.Button(root, text="9", command=button_click9, width=5, height=2)
button9.grid(row=2, column=2)
button0 = tk.Button(root, text="0", command=button_click0, width=5, height=2)
button0.grid(row=3, column=1)
buttonplus = tk.Button(root, text="+", command=button_clickplus, width=5, height=2)
buttonplus.grid(row=4, column=4)

# Start the main event loop
root.mainloop()
