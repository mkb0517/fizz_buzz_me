#!/usr/bin/env python

import sys

def fizz_buzz(number):
    """Return a string representing the number, or 'fizz'/'buzz'/'fizzbuzz'"""
    if number%3==0:
        result = "fizz"
        if number%5==0:
            result = "fizzbuzz"
    elif number%5==0:
        result = "buzz"
    else:
        result = str(number) 
    return result    

def main():
    """Print sample output of fizz_buzz function"""
    NUMBER = 20
    print("Sample fizz_buzz output for 1 to {0}:".format(NUMBER))
    for i in range(1, NUMBER+1):
        print(fizz_buzz(i))


##########################

if __name__ == '__main__':
    main()
