class User:
    '''
    A program that will accept input from the user in order to
    build a User object that can then be stored in a system.
    '''

    def __init__(self, first_name, last_name, age, address, phone_number, email_address, birth_date= None):
        
        #Ensuring that the first name entered is not empty
        try:
            if first_name == "":
                raise NameError('First Name cannot be an empty string')
            elif not isinstance(first_name, str):
                raise NameError('First Name can only be a string')
            else:
                self.first_name = first_name
        except NameError as e:
                print(e)
        
        #Ensuring that the last name entered is not empty
        try:
            if last_name == "":
                raise NameError('First Name cannot be an empty string')
            elif not isinstance(last_name, str):
                raise NameError('First Name can only be a string')
            else:
                self.last_name = last_name
        except NameError as e:
            print(e)

        #Ensuring that the age is a valid number between 18 and 100
        try:
            if isinstance(age, int):
                if age < 18:
                    print ("User underage, exiting...")
                    exit(0)
                elif age > 100:
                    raise ValueError('Not a valid number')
                else:
                    self.age = int(age)
            else:
                raise ValueError('Please enter your age in numeric format')
        except ValueError as e:
            print(e)

        # Ensuring that the address contains 6 parts
        try:
            #test if address string has 6 parts
            address_list = address.split()
            if len(address_list) == 6:
                self.address = address
            else:
                raise ValueError('Must contain 6 parts: an address number, street name, city, province/state, ZIP code, and country')
        except ValueError as e:
            print(e)

        # Testing if phone number contains at least 10 digits
        try:
            if isinstance(phone_number, int):
                if len(str(phone_number)) == 10:
                    self.phone_number = phone_number
                else:
                    raise ValueError('Phone number must contain 10 digits')
            else:
                raise ValueError('Phone number must contain 10 digits')
        
        except ValueError as e:
            print (e)
        
        # Testing if email adress meets the required validation
        try:
            if len(email_address) > 5 and (('@' and '.') in email_address):
                self.email_address = email_address
            else:
                raise ValueError('Not a valid email addrees')

        except ValueError as e:
            print(e)

        self.birth_date = birth_date

    def fullname(self):
        # Printing the full name
        print (self.first_name, self.last_name)

    def __str__(self):
        # Printing the user details
        return f"Hello {self.first_name} \nThank you for registering with the following information: \nFirst Name: {self.first_name} \nLast Name: {self.last_name} \nAge: {self.age}\nAddress: {self.address} \nPhone Number: {self.phone_number} \nEmail Address: {self.email_address}"
      
phil = User("Phillip", "Moyo", 30, "50 3rd Avenue Jhb 2092 South_Africa", 7861242333, "phylls@gmail.com", "10-02-2021")
phil.fullname()
print(phil)
