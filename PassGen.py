# Imports
import random
from tkinter import *
from tkinter import ttk
import os


def passgen():
    # This is the seed magics
    seed_password = random.randint(1, 999999999999999999)

    # Variables
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()_+"
    lower_upper = lowercase + uppercase
    lower_upper_num = lower_upper + numbers
    lower_upper_sym = lower_upper + symbols
    lower_upper_num_sym = lower_upper_num + symbols

    # This is the starting window_pass
    window_pass = Tk()
    window_pass.title("Password Generator")
    window_pass.geometry("350x250")

    def check_password(password, user_input):
        # Check the type of password the user wants and set the variables accordingly
        check_lowercase = False
        check_uppercase = False
        if user_input == 0:
            check_numbers = False
            check_symbols = False
        elif user_input == 1:
            check_numbers = False
            check_symbols = True
        elif user_input == 2:
            check_numbers = True
            check_symbols = False
        else:
            check_numbers = True
            check_symbols = True

        # Check if the password has all the character types required
        for i in range(len(lowercase)):
            if lowercase[i] in password:
                check_lowercase = True
            else:
                pass
        for i in range(len(uppercase)):
            if uppercase[i] in password:
                check_uppercase = True
            else:
                pass
        if str(check_box_n.state()) == "('focus', 'selected')" or str(check_box_n.state()) == "('selected',)":
            for i in range(len(numbers)):
                if numbers[i] in password:
                    check_numbers = True
                else:
                    pass
        if str(check_box_s.state()) == "('focus', 'selected')" or str(check_box_s.state()) == "('selected',)":
            for i in range(len(symbols)):
                if symbols[i] in password:
                    check_symbols = True
                else:
                    pass

        if check_lowercase and check_uppercase and check_numbers and check_symbols:
            return password
        else:
            return update_password(check_lowercase, check_uppercase, check_numbers, check_symbols, password, user_input)

    def update_password(check_lowercase, check_uppercase, check_numbers, check_symbols, password, user_input):
        # Update the password if it doesn't have all the character types required
        if check_lowercase and check_uppercase and check_numbers:
            password = password[:-1] + random.choice(symbols)
        elif check_lowercase and check_uppercase and check_symbols:
            password = password[:-1] + random.choice(numbers)
        elif check_lowercase and check_numbers and check_symbols:
            password = password[:-1] + random.choice(uppercase)
        elif check_uppercase and check_numbers and check_symbols:
            password = password[:-1] + random.choice(lowercase)
        elif check_lowercase and check_uppercase:
            password = password[:-2] + random.choice(numbers) + random.choice(symbols)
        elif check_lowercase and check_numbers:
            password = password[:-2] + random.choice(uppercase) + random.choice(symbols)
        elif check_lowercase and check_symbols:
            password = password[:-2] + random.choice(uppercase) + random.choice(numbers)
        elif check_uppercase and check_numbers:
            password = password[:-2] + random.choice(lowercase) + random.choice(symbols)
        elif check_uppercase and check_symbols:
            password = password[:-2] + random.choice(lowercase) + random.choice(numbers)
        elif check_numbers and check_symbols:
            password = password[:-2] + random.choice(lowercase) + random.choice(uppercase)
        elif check_lowercase:
            password = password[:-3] + random.choice(uppercase) + random.choice(numbers) + random.choice(symbols)
        elif check_uppercase:
            password = password[:-3] + random.choice(lowercase) + random.choice(numbers) + random.choice(symbols)
        elif check_numbers:
            password = password[:-3] + random.choice(lowercase) + random.choice(uppercase) + random.choice(symbols)
        elif check_symbols:
            password = password[:-3] + random.choice(lowercase) + random.choice(uppercase) + random.choice(numbers)
        else:
            pass
        return check_password(password, user_input)

    # This is the function that will be used to generate the password
    def generate_password():
        seed_password = text_box_seed.get()
        random.seed(seed_password)

        number_of_characters = number_roll.get()
        if number_of_characters == "" or number_of_characters == " " or int(number_of_characters) < 5:
            number_of_characters = 8
        number_of_characters = int(number_of_characters)
        password = ""

        if str(check_box_n.state()) == "('focus', 'selected')" and str(check_box_s.state()) == "('focus', 'selected')" or \
                str(check_box_n.state()) == "('focus', 'selected')" and str(check_box_s.state()) == "('selected',)" or \
                str(check_box_n.state()) == "('selected',)" and str(check_box_s.state()) == "('focus', 'selected')" or \
                str(check_box_n.state()) == "('selected',)" and str(check_box_s.state()) == "('selected',)":
            user_input = 0
            for i in range(number_of_characters):
                password += random.choice(lower_upper_num_sym)

        elif str(check_box_n.state()) == "('focus', 'selected')" or str(check_box_n.state()) == "('selected',)":
            user_input = 1
            for i in range(number_of_characters):
                password += random.choice(lower_upper_num)
        elif str(check_box_s.state()) == "('focus', 'selected')" or str(check_box_s.state()) == "('selected',)":
            user_input = 2
            for i in range(number_of_characters):
                password += random.choice(lower_upper_sym)
        else:
            user_input = 3
            for i in range(number_of_characters):
                password += random.choice(lower_upper)

        # Checks to see if the password is valid (contains every character type the user wants)
        password = check_password(password, user_input)

        # This is the text box that will be used to display the password
        text_box.delete(0, END)
        text_box.insert(END, password)
        text_box.pack()

    # This is the function that will be used to close the window
    def close_pass():
        exit(print("Bye!"))

    def exit_pass():
        exit(print("Bye!"))

    # This is the label that will be used to make the number roll to choose the number of characters
    label = Label(window_pass, text="How many characters would you like in your password?")
    label.pack()
    number_roll = Spinbox(window_pass, from_=8, to=32)
    number_roll.pack()

    # This is the label that will be used to ask the user if they want numbers in their password
    check_box_n = ttk.Checkbutton(window_pass, text="Numbers")
    check_box_n.pack()
    check_box_n.state(['!alternate'])

    # This is the label that will be used to ask the user if they want symbols in their password
    check_box_s = ttk.Checkbutton(window_pass, text=" Symbols")
    check_box_s.pack()
    check_box_s.state(['!alternate'])

    # This is the button that will be used to generate the password
    button = Button(window_pass, text="Generate Password", command=generate_password)
    button.pack()

    # This is the text box that will be used to display the password
    label = Label(window_pass, text="Your password is :")
    label.pack()
    text_box = Entry(window_pass, width=35, justify=CENTER)
    text_box.pack()

    # This is the label that will be used to ask the user for the seed
    label = Label(window_pass, text="The seed is :")
    label.pack()
    text_box_seed = Entry(window_pass, width=35, justify=CENTER)
    text_box_seed.insert(END, seed_password)
    text_box_seed.pack()

    # This is the button that will be used to exit the program
    button = Button(window_pass, text="Quit", command=exit_pass)
    button.pack()

    # This is the main loop
    window_pass.protocol("WM_DELETE_WINDOW", close_pass)
    window_pass.mainloop()

passgen()