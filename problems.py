"""Wap a program to print Twinkle Twinkle little star poem in python"""

print('''Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.

Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.''')

"""Use REPL and print the table of 5 using it"""

"""Install an external module and use it to perform an operation of your interest"""

import pyttsx3
engine = pyttsx3.init()
engine.say("Donald Trump is a joker")
engine.runAndWait()

"""WAP to print the contents of a direcory using the os module."""

import os

# Ask the user to enter a directory path
directory = '/New Folder'

# Check if the directory exists
if os.path.exists(directory):
    print(f"\nContents of directory '{directory}':\n")
    
    # List all files and folders in the directory
    for item in os.listdir(directory):
        print(item)
else:
    print("The specified directory does not exist.")

"""

"""
# The provided code stub reads an integer, n, from STDIN. For all non-negative integers i<n, print i^2.
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)
