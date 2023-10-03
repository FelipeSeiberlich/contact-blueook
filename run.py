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

panel = """                                                  
### #           ##   #                       #   
 #  # # ###     # #  #  # # ### ### ### # # 
 #  ### ##      ##   #  # # ##  # # # # ##  
 #  # # ###     # #  ## ### ### ### ### # # 
 #              ##                               
"""
print(panel)
print('***Welcome to the Smurfs collectors Contact Book***')
smurfette = """                    
         **//***     
          /////    .         
          (#(    ,,,..         
          ((/   ,.,. ..          Hi! I am Smurfette. Nice to meet you.
          /((  ..,,***,,      
           ((  /*/%%&@#%/        
           /( /(/  *.& (//,      
           .((#&(((##(##%(/,,    
            ((%%%&/%%,%((//**     I will give you some tips about this program...
           /((%((#/,..,##/*     
            (#   *,...,/,,##((      This is a contact book for Smurfs lovers!
            /#  ,*.....,,,    
            /(    #%  #(          Please follow the instructons below.
           *((  ##%%(###(.    
          .*(....,/......     
"""
print(smurfette)
def get_contact_data():
    """
    Get name, phone, location and email contact from the user.
    """
    print(' ')
    print('Please enter your name and surname.')
    print('Data must contain only letters.\n')
    print('Example: Philip Grant.\n')
    name_str = input('Enter your name here: \n')
    print(' ')
    print('Validating...\n')
    if any(x not in ALLOWED_NAME_CHARACTERS for x in name_str):
        print("Error: invalid character. :(\n")
        get_name_data()
    else:
        print("No error. :)")
        print(f'The name {name_str} was added successfully!\n')
    
    print('Please enter your Phone Number.')
    print('Data must contain only numbers.\n')
    print('Example: 00 353 892516666\n')
    phone_number_str = input('Enter your phone number here: \n')
    if any(x not in ALLOWED_PHONE_CHARACTERS for x in phone_number_str):
        print("\nError: Invalid character. :(\n")
        get_phone_number()
    else:
        print(' ')
        print("No error. :)")
        print(f'The number {phone_number_str} was added successfully!\n')
    
    print('The country I am located is...?')
    print('Example: Ireland.\n')
    location_str = input('Enter your location here: \n')
    print(' ')
    print(f'The location provided is {location_str}.\n')
    print('Please enter your email.\n')
    print('Example: phil123@gmail.com.\n')
    email_str = input('Enter your email here: \n')
    print(' ')
    print(f'The email provided is {email_str}\n')
    
def get_name_data():
    """
    Get Name and Surname data from the user.
    """
    name_str = input('Enter your name here: \n')
    print(' ')
    print('Validating...\n')
    if any(x not in ALLOWED_NAME_CHARACTERS for x in name_str):
        print("Error: invalid character\n")
        get_name_data()
    else:
        print("No error. :)\n")
        print(f'The name {name_str} was added successfully!')
        print(' ')
def get_phone_number():
    """
    Get Phone number data from the user.
    """
    phone_number_str = input('Enter your phone number here: ')
    if any(x not in ALLOWED_PHONE_CHARACTERS for x in phone_number_str):
        print("\nError: Invalid character, please enter numbers only.")
        phone_number_str = input('Enter your phone number here: ')
        print(' ')
    else:
        print(' ')
        print("No error. :)")
        print(f'The number {phone_number_str} was added successfully!\n')

def update_contact_worksheet(data):
    """
    Update worksheet with data values, add a new row with the list data provided.
    """
    print('Updating contact worksheet...')
    contact = SHEET.worksheet('contact')
    contact.append_row(data)
    print('Contact worksheet updated successfully!\n')
    add_new_entry()

def add_new_entry():
    new_entry = input('Would you like to add a new collector to the Blueook y/n?')
    if new_entry == 'y' or new_entry == 'Y':
        print(' ')
        get_contact_data()
        print(' ')
    else:
        print(' ')
        print('Thanks for using The Blueook.')
        print('See you soon!') 

          

def main():
    contact_data = (f'{name_str}, {phone_number_str}, {location_str}, {email_str}')
    data = contact_data.split(',')
    add_new_entry()

data = get_contact_data()
update_contact_worksheet(data)


