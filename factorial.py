def factorial(x):
    factor = 1
    if x > 0:
        if x == 1:
            factor = x * 1
        else:
            while x > 0:
                factor = factor * x
                x = x-1
        return factor
    else:
        print "not a positive number"
