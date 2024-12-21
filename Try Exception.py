def devide(x,y):
    return x/y

try:
    print(devide(10, 0))
except ZeroDivisionError:
    print("Error: can't devide over 0")


print('='*10)


def fun(x):
    if x < 5:
        y = x/(x-3)
    return f'y = {y}'

try:
    # a = fun(3)
    # a = fun(5)
    a = fun(2)
except ZeroDivisionError:
    print("Error: Can't devide over zero.")
except NameError:
    print("Error: No variable has name y.")
except:
    print("Error!")
else:
    print(a)
finally:
    print("Finally always executed.")

