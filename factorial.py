def factorial(x):
    factor = 0
    if x > 0:
        for each in range(x):
            if x == 1:
                factor = x * 1
            else:
                factor = x * (each - 1)
        return factor
    else:
        print "not a positive number"
