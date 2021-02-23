def division(a, b):
    try:
        return round(a / b, 9)  # round to 9 decimals to match cvs test case

    except:
        return "Error: Cannot be divided by 0."
