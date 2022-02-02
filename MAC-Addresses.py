# MAC Addresses
# Objective: Given a file, find all the unique MAC Addresses

import re

def unique_addresses(filename):
    """ Parses through a file to find all the unique MAC addresses. """

    with open(filename) as file:
        file = file.read()

    pattern = r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})"

    matches = re.finditer(pattern, file)

    # for item in matches: 
    #     print(item.group(0))

    # List comprehension:
    mac_addresses = [item.group(0) for item in matches]

    # Throws out the duplicates
    unique_mac_addresses = set(mac_addresses)

    print('Amount of all MAC Addresses:', len(mac_addresses))
    print('All MAC Addresses:', mac_addresses)
    print('\n')
    print('Amount of unique MAC Addresses:', len(unique_mac_addresses))
    print('Unique set of MAC Addresses:', unique_mac_addresses)


unique_addresses('ifconfig.rtf') # Enter name of filename here. 