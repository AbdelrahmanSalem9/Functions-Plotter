from tkinter import Button, Entry, Label, Tk, messagebox, font,StringVar
from controller import xor_check, check_errors,evaluation
import constant as const
import matplotlib.pyplot as plt


def plot(expr, x_min, x_max):

    fig = plt.figure(figsize=(8, 5))

    # evaluate f(x) and plot it
    x,y = evaluation(expr,x_min,x_max)
    plt.plot(x, y)

    # Show the plot
    plt.title(const.PLOT_WINDOW_TITLE+f"\n{expr}", fontsize=20)
    plt.xlabel(const.PLOT_LABEL_X, fontsize=15)
    plt.ylabel(const.PLOT_LABEL_Y, fontsize=15)
    plt.grid(True)
    plt.show()


def error_box(message):
    return messagebox.showinfo('Error', message)


def proceed(expr, x_min, x_max):

    # check any error pre-defined
    """
    1- Missing function expression
    2- Invalid function expression or complicated function can't be computed naively
    3- Missing Min or Max inputs
    4- Invalid Ranges for Min and Max inputs, (min > max)

    """
    # check for "^" operator and replace by "**" as python convention
    expr = xor_check(expr)
    err = check_errors(expr, x_min, x_max)
    if not err:
        plot(expr, x_min, x_max)
    else:
        error_box(err)
        pass


def launch_app(test_fun=None, test_min=None, test_max=None):

    # main window creating
    main = Tk()
    main.title(const.APP_NAME)
    main.geometry(const.MAIN_WINDOW_DIMENSIONS)
    main.resizable(False, False)
    main.eval('tk::PlaceWindow . center')
    title = Label(main, text=const.APP_WINDOW_TITLE,
                  font=(const.FONT_TYPE, 18))

    # input user variables
    expr = StringVar()
    min_input = StringVar()
    max_input = StringVar()

    # UI components creating
    function_entry = Entry(main, textvariable=expr, font=(const.FONT_TYPE, 15))
    min_entry = Entry(main, textvariable=min_input, font=(const.FONT_TYPE, 10))
    max_entry = Entry(main, textvariable=max_input, font=(const.FONT_TYPE, 10))
    x_min = Label(main, text='Min', font=(const.FONT_TYPE, 10))
    x_max = Label(main, text='Max', font=(const.FONT_TYPE, 10))

    # Procced Button and action taken
    next_button = Button(main, text=const.MAIN_WINDOW_BUTTON_TEXT,
                         command=lambda: proceed(function_entry.get(), min_entry.get(), max_entry.get()))

    # unpack and placing the UI components
    title.pack()
    function_entry.pack()
    x_min.pack()
    x_max.pack()
    min_entry.pack()
    max_entry.pack()
    next_button.pack()

    function_entry.place(x=100, y=40, height=30, width=300)
    x_min.place(x=175, y=90)
    min_entry.place(x=220, y=90, height=20, width=60)
    x_max.place(x=175, y=120)
    max_entry.place(x=220, y=120, height=20, width=60)
    next_button.place(x=225, y=160)
    main.mainloop()


if __name__ == '__main__':
    launch_app()
