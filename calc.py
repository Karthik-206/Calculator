import tkinter as tk

# Create window
window = tk.Tk()
window.title('Calculator')

# Configure rows & columns to center frame
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

# Frame in center
frame = tk.Frame(window)
frame.grid(row=1, column=1)

# Entry widget
entry = tk.Entry(frame, width=60, bg='black', fg='white')
entry.grid(row=0, column=1, columnspan=4, ipady=10)

# --- Functions ---

# Insert numbers/operators
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Clear all
def clear():
    entry.delete(0, tk.END)

# Backspace
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# Evaluate
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Percentage: divide current number by 100
def percent():
    try:
        current = float(entry.get())
        result = current / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# --- Buttons style ---
btn_style = {'width': 10, 'height': 4, 'bg': 'black', 'fg': 'white', 'font': ('timesnewroman', 10)}

# --- Buttons Layout ---

# Row 1
tk.Button(frame, text='AC', **btn_style, command=clear).grid(column=1, row=1)
tk.Button(frame, text='<-', **btn_style, command=backspace).grid(column=2, row=1)
tk.Button(frame, text='+', **btn_style, command=lambda: click('+')).grid(column=3, row=1)
tk.Button(frame, text='-', **btn_style, command=lambda: click('-')).grid(column=4, row=1)

# Row 2
tk.Button(frame, text='1', **btn_style, command=lambda: click('1')).grid(column=1, row=2)
tk.Button(frame, text='2', **btn_style, command=lambda: click('2')).grid(column=2, row=2)
tk.Button(frame, text='3', **btn_style, command=lambda: click('3')).grid(column=3, row=2)
tk.Button(frame, text='X', **btn_style, command=lambda: click('*')).grid(column=4, row=2)  # X means *

# Row 3
tk.Button(frame, text='4', **btn_style, command=lambda: click('4')).grid(column=1, row=3)
tk.Button(frame, text='5', **btn_style, command=lambda: click('5')).grid(column=2, row=3)
tk.Button(frame, text='6', **btn_style, command=lambda: click('6')).grid(column=3, row=3)
tk.Button(frame, text='/', **btn_style, command=lambda: click('/')).grid(column=4, row=3)

# Row 4
tk.Button(frame, text='7', **btn_style, command=lambda: click('7')).grid(column=1, row=4)
tk.Button(frame, text='8', **btn_style, command=lambda: click('8')).grid(column=2, row=4)
tk.Button(frame, text='9', **btn_style, command=lambda: click('9')).grid(column=3, row=4)
tk.Button(frame, text='x^n', **btn_style, command=lambda: click('**')).grid(column=4, row=4)  # Power means **

# Row 5
tk.Button(frame, text='%', **btn_style, command=percent).grid(column=1, row=5)  # Call percent()
tk.Button(frame, text='0', **btn_style, command=lambda: click('0')).grid(column=2, row=5)
tk.Button(frame, text='.', **btn_style, command=lambda: click('.')).grid(column=3, row=5)
tk.Button(frame, text='=', **btn_style, command=equal).grid(column=4, row=5)

# Run
window.mainloop()
