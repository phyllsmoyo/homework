# Searcheable address book
my_address_book = {
    "David": {
        "mobile phone number": "123-456-7890",
        "work phone number": "098-765-4321",
        "personal email address": "david@home-email.com",
        "home address": "1234 Somewhere Dr., Denver, CO, 80221 USA",
    },
    "Zofia": {
        "work phone number": "098-765-4321",
        "work address": "4321 Workplace St., New York, NY, 10001 USA",
    },
    "Bukhosi": {
        "home phone number": "098-765-4321",
        "personal email address": "bukhosi@home-email.com",
        "home address": "123 Here Ave., Johanensburg, GP, 2006 ZA",
    },
}

print("Enter the name:")
search_name = input()

if search_name in my_address_book.keys():
    print(f"Contact information found for {search_name}!")
    for key, value in my_address_book.get(search_name).items():
        print(f"{search_name} can be reached via their {key} at {value} ")

else:
    print(
        f"No contact information found for {search_name}! Be sure to ask them for their contact details next time you see them."
    )
