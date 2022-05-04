import tkinter
from tkinter import Button, Entry, Label, Tk
import tkinter
from tkinter import messagebox
from controller import xor_check
from controller import check_errors
from variables import SAMPLING_FREQ
import matplotlib.pyplot as plt
import numpy as np


def plot(expr, x_min, x_max):
    expr = xor_check(expr)
    x = np.linspace(int(x_min), int(x_max), SAMPLING_FREQ)
    fig = plt.figure(figsize=(8, 5))

    # Create the plot
    y = eval(expr)
    plt.plot(x, y)

    # Show the plot
    plt.title("Function Plot", fontsize=20)
    plt.xlabel("x", fontsize=15)
    plt.ylabel("f(x)", fontsize=15)
    plt.grid(True)
    plt.show()


def error_box(message):
    return messagebox.showinfo('Error', message)


def proceed(expr, x_min, x_max):

    err = check_errors(expr, x_min, x_max)
    if not err:
        plot(expr, x_min, x_max)
    else:
        error_box(err)
        pass


main = Tk()
main.title('Function Plotter Program')
main.geometry("500x200")
main.resizable(False, False)
main.eval('tk::PlaceWindow . center')

title = Label(main, text='Enter Function', font=("Arial", 18))
error_message = Label(main, text='Error: Invalid Function',
                      fg='#f00', font=("Arial", 13))
expr = tkinter.StringVar()
min_input = tkinter.StringVar()
max_input = tkinter.StringVar()

function_entry = Entry(main, textvariable=expr, font=("Arial", 15))
x_min = Label(main, text='Min', font=("Arial", 10))
x_max = Label(main, text='Max', font=("Arial", 10))
min_entry = Entry(main, textvariable=min_input, font=("Arial", 10))
max_entry = Entry(main, textvariable=max_input, font=("Arial", 10))

next_button = Button(main, text='Proceed',
                     command=lambda: proceed(function_entry.get(), min_entry.get(), max_entry.get()))

title.pack()
function_entry.pack()
function_entry.place(x=100, y=40, height=30, width=300)
x_min.pack()
x_min.place(x=175, y=90)
min_entry.pack()
min_entry.place(x=220, y=90, height=20, width=60)

x_max.pack()
x_max.place(x=175, y=120)
max_entry.pack()
max_entry.place(x=220, y=120, height=20, width=60)

next_button.pack()
next_button.place(x=225, y=160)
main.mainloop()
