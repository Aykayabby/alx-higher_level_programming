#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        tab = ""
        if ((i % 3 == 0) and (i % 5 == 0)):
        tab = "FB"
        elif i % 3 == 0:
            tab = "F"
        elif i % 5 == 0:
            tab = "B"
    print("{}" .format(i if tab == "" else tab), end=" ")
