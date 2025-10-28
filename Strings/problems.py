
# WAP to display a user centered name followed by Good Afternoon using input() function

name = input("Enter your name: ")

print(f"Good Afternoon {name}")

# WAP to fill in a letter template given below with name and date

letter  ='''
            Dear <|Name|>,
            You are selected!
            <|Date|>
            '''

print(letter.replace("<|Name|>", "Nilesh").replace("<|Date|>", "28 October 2035"))

# WAP to detect doubl space in a string

new = "Python is one  of the most popular programming languages"

print(new.find("  "))
print(new.replace("  ", " "))

#* Strings are immutable which means that you cannot change them by running functions on them

# Write a program to format the following letter using escape sequence characters

Letter = "Dear Nishant,\n\tthis javascript course is nice. \nThanks!"
print(Letter)
