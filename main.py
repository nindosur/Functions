    # 1
def task1():
    print('''“Don't compare yourself with anyone in this world…
             if you do so, you are insulting yourself.”
                                                        Bill Gates''')
task1()

    # 2
def task2():
    for i in range(x,y):
        if i % 2 == 0:
            print(i)
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
task2()

    # 3
def draw_square(n, s, f):
    r = s * n
    if not f:
        m = s + " " * (n - 2) + s
    else:
        m = r
    print(r)
    for i in range(n - 2):
        print(m)
    print(r)
draw_square(5, "#", True)
print("")
draw_square(5, "*", False)

    # 4
import random
def minx(x):
    y = min(x)
    print(y)
x = [random.randint(-100,100) for i in range(5)]
print(x)
minx(x)

    # 5
def proizv(x,y):
    if y<x:
        x, y = y, x
    a = 1
    for i in range(x,y+1):
        a *= i
        print(a)
x = int(input("Введите перове число: "))
y = int(input("Введите второе число: "))
proizv(x,y)

    # 6
def qwe(x):
    res = 0
    for i in range(len(str(x))):
        res += 1
    print("В числе", x, "-", res, "цифр(ы).")
x = int(input("Введите число: "))
qwe(x)

    # 7
def palindrom(x):
    pr = ''.join(reversed(str(x)))
    return str(x) == str(pr)
x = input("Введите число: ")
if palindrom(x):
    print("True")
else:
    print("False")
