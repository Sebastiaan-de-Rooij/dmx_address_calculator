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
nr_of_channels = 32
nr_of_fixtures = 8


def generate_address_table(group_name, first_address, nr_of_channels, nr_of_fixtures):
    table = []
    current_fixture = 1
    current_address = first_address
    while current_fixture <= nr_of_fixtures:
        current_row = [group_name, current_fixture, current_address]
        table.append(current_row)
        current_fixture += 1
        current_address += nr_of_channels
    return table


adress_table = generate_address_table(
    group_name, first_address, nr_of_channels, nr_of_fixtures
)


def print_table(address_table):
    for item in address_table:
        print(item[0], item[1], item[2])


print_table(adress_table)
