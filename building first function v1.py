# group_name = "Spiider"
# adress = 20
# group_list = [
#     [group_name, 1, adress],
#     [group_name, 2, adress],
#     [group_name, 3, adress],
#     [group_name, 4, adress],
# ]

# for item in group_list:
#     print(item[0], item[1], item[2])
"""This is how the list can be printed, Streamlit should be able to write this too...


Now how to CREATE this list containing lists?
we need a loop that doest this on each iteration:
    - creates a list with [group_name, fixture_number, address]
    - appends this list as an item in group_list


"""

group_name = "Spiider"
first_address = 1
number_of_channels = 12
number_of_fixtures = 12

group_list = []
count = 1
current_fixture = 1
current_address = first_address
while count <= number_of_fixtures:
    current_row = [group_name, current_fixture, current_address]
    current_fixture += 1
    current_address += number_of_channels
    count += 1
    group_list.append(current_row)

for item in group_list:
    print(item[0], item[1], item[2])
