def check_errors(expr, x_min, x_max):
    if "^" in expr:
        expr = expr.replace("^", "*")
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
