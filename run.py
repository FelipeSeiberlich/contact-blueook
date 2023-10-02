import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('blueook')
ALLOWED_NAME_CHARACTERS=['a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
    'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N',
    'O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
ALLOWED_PHONE_CHARACTERS=['1','2','3','4','5','6','7','8','9','0',' ']


def get_contact_data():
    """
    Get name, phone, location and email contact from the user.
    """
    print('Please enter your name and surname.')
    print('Data should contain only letters.')
    print('Example: Philip Grant.\n')

    name_str = input('Enter your name here: \n')
    print('Validating...')
    if any(x not in ALLOWED_NAME_CHARACTERS for x in name_str):
        print("error: invalid character\n")
        get_name_data()
    else:
        print("no error\n")
        print(f'The name {name_str} is validated!')
    
    print('Please enter your Phone Number.')
    print('Data contains only numbers.\n')
    print('Example: 00 353 892516666')

    phone_number_str = input('Enter your phone number here: ')
    if any(x not in ALLOWED_PHONE_CHARACTERS for x in phone_number_str):
        print("\nerror: Invalid character, please enter numbers only.")
        get_phone_number()
    else:
        print("no error")
    
    print('Please enter in which country you are located.')
    print('Example: Ireland.\n')
    location_str = input('Enter your location here: ')
    print(f'The location provided is {location_str}\n')

    print('\nPlease enter your email.')
    print('Example: phil123@gmail.com.\n')
    email_str = input('Enter your email here: ')
    print(f'The email provided is {email_str}\n')


def get_name_data():
    """
    Get Name and Surname data from the user.
    """
    name_str = input('Enter your name here: \n')
    print('Validating...')
    if any(x not in ALLOWED_NAME_CHARACTERS for x in name_str):
        print("error: invalid character\n")
        get_name_data()
    else:
        print("no error\n")
        print(f'The name {name_str} is validated!')

def get_phone_number():
    """
    Get Phone number data from the user.
    """
    phone_number_str = input('Enter your phone number here: ')
    if any(x not in ALLOWED_PHONE_CHARACTERS for x in phone_number_str):
        print("\nerror: Invalid character, please enter numbers only.")
        phone_number_str = input('Enter your phone number here: ')
    else:
        print("no error")



get_contact_data()
        


