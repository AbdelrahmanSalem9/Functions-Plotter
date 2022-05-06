import constant as const
import numpy as np
from numpy import e,sin,cos,tan,log2,log10


def check_errors(expr, x_min, x_max):

    if expr == "":
        return "Please Enter the function expression"
    try:
        x = 0
        fx = eval(expr)
    except:
        return "Invalid Expression"

    if x_min == "" or x_max == "":
        return "Please Enter Maximum and Minimum"

    if int(x_min) > int(x_max):
        return "Ranges are invalid"
    return None


def xor_check(expr):
    if "^" in expr:
        return expr.replace("^", "**")
    return expr


def evaluation(expr, x_min, x_max):
    x = np.linspace(int(x_min), int(x_max), const.SAMPLING_FREQ)
    y = eval(expr)

    return x, y
