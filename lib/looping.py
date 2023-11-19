#!/usr/bin/env python3


def happy_new_year():
    i = 1
    while i < 11:
        print (f'{i}\n')
        i += 1
        print ("Happy New Year!")


def square_integers(int_list):
    result = []
    for value in int_list:
        squared = abs(value ** 2)
        result.append(squared)
    return result

def fizzbuzz():
    # prints 1 to 100 with fizz 3x, buzz 5s, fizzbuzz 3and5s
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print ("FizzBuzz")
        elif i % 3 == 0:
            print ("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        else:
            print (i)
      
