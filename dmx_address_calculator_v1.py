"""
Docstring for Jottacloud.programming.python_project.dmx_adres_calculator.dmx_adres_calculator

an app to calculate ranges of dmx adresses for lighting fixtures

possible approach:
- a function that asks all input by using 4 input function calls
- a function that calculates a list of dmx values based on the input given
- a for loop that prints each adres on a new line




A lesser light asked Ummon:
is using a loop that repeats a calculation and appends the result to a list a good way of filling a list in python?

Yes — using a loop to repeat a calculation and append the result to a list is a perfectly good and very common way to fill a list in Python. It’s clear, explicit, and easy to debug.
Example:


results = []

for i in range(10):
    value = i * i
    results.append(value)


This is idiomatic Python, especially when:
The calculation is non-trivial
You need conditionals (if, break, continue)
You’re still learning and want clarity
You want step-by-step control


There might be a lot of comments explaining the workings of the code
These are my training wheels since this is my 8th week of learning Python

"""


def ask_input():
    number_fixtures = int(input("Enter the number of fixtures: "))
    number_channels = int(input("Enter the number of DMX channels per fixture: "))
    start_address = int(input("Enter the starting address: "))
    return number_fixtures, number_channels, start_address


# note that the int function is highlighted differently (VS Code color scheme: Dark Modern)
# this is probably because its a built in type conversion function
# we use it because the other used functions need integers


def fill_list(number_fixtures, number_channels, start_address):
    list_of_addresses = [start_address]
    iteration_count = 1
    while iteration_count < number_fixtures:
        next_address = list_of_addresses[-1] + number_channels
        list_of_addresses.append(next_address)
        iteration_count += 1
    return list_of_addresses


# list_of_addresses[-1] is the last element of the list
# negative numbers are used to indicate items from last to first
# iteration+count += 1 is short for iteration_count = iteration_count + 1
# remember that list_of_addresses.append(next_adres) is using a method, not a regular function
# methods are called after the variable ist's working on and are preced by a .
# += is a unique operator, not a combo of + and = which are entirely different operators
# this function seems to be doing a lot, I might want to refactor to smaller functions


def print_list(range_name, list_addresses, number_channels):
    last_channel = list_addresses[-1] + number_channels - 1
    if last_channel > 512:
        print("This is more than 512 channels, try again!")
    else:
        for fixture_number, fixture_address in enumerate(list_addresses, start=1):
            print(f"{range_name} {fixture_number} = {fixture_address}")


# enumerate is clever, but too advanced for now, I will refactor
# the goal is to get a fixture number and an adress in each iteration
# may be this should even be multiple functions
# maybe each line should already be a list or a tuple with range name, fixture number and adress
# the function now does three different things:
# check if the last dmx channel is 512 or less (one dmx universe is 512 channels)
# it attaches a fixture number to an address
# it prints a list with on every line the range name, fixture number and adres

range_name = input("Enter a name for this range: ")
# can i move this to ask_input? what are the consequences for the other functions?

number_fixtures, number_channels, start_address = ask_input()
# apperently I can declare multiple values and assign one function call to Fill 'em All
list_of_addresses = fill_list(number_fixtures, number_channels, start_address)
# creates the list of dmx addresses using the variables that just got their values via the ask_input function!
print_list(range_name, list_of_addresses, number_channels)
# again, does too much!

# do the functions depend too much on eachother?
# how does this scale?
# how reusable is all of this?
# #refactor?
# use GitHub?
