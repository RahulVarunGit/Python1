class TestError(Exception):
    pass

raise TestError("Test Error")
x = 1

try:
    #print(x/0)
    if not type(x) is str:
        raise TypeError("Only string is allowed")

except ZeroDivisionError:
    print("Number cannot be devided by zero")

except TypeError:
    print("Only string value should be used.")

else:
    print("No errors")

finally:
    print("Always run")





