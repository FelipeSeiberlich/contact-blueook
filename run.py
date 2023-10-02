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
        get_contact_data()
    else:
        print("no error\n")
        print(f'The name {name_str} is validated!')

get_contact_data()
        


