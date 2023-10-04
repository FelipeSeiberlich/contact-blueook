import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Back, Style
colorama.init()
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
print(Fore.BLUE, panel)
print(Fore.YELLOW + '     ***Welcome to the Smurfs collectors Contact Book***')
print(Fore.WHITE)
smurfette = """                    
**//***     
/////    .         
(#(    ,,,..         
((/   ,.,. ..         Hi! I am Smurfette. Nice to meet you! 
/((  ..,,***,,          
((  /*/%%&@#%/        
/( /(/  *.& (//,      This is a contact book for Smurfs lovers!
.((#&(((##(##%(/,,    
((%%%&/%%,%((//**          Please follow the instructons below,
/((%((#/,..,##/*     
(#   *,...,/,,##((                     and Blueook yourself...
/#  ,*.....,,,    
/(    #%  #(          
*((  ##%%(###(.    
.*(....,/......  
"""
print(smurfette)

def get_contact_data():
    """
    Get name, phone, location and email contact from the user.
    """
    print(Fore.WHITE, Style.BRIGHT)
    print('Please enter your name and surname.')
    print('Data must contain only letters.')
    print(Fore.YELLOW)
    print('Example: Philip Grant.')
    print(Fore.WHITE)
    name_str = input('Enter your name here: \n')
    print(' ')
    print(Fore.BLUE + 'Validating...\n')
    if any(x not in ALLOWED_NAME_CHARACTERS for x in name_str):
        print(Fore.RED +'Error: invalid character. :(\n')
        print('Oooops! I will tell Papa Smurf that you did not follow the instructions.\n')
        print(Fore.GREEN + 'This time use only letters. :)')
        print(Fore.WHITE)
        get_name_data()
    else:
        print(Fore.GREEN + 'No error. :)')
        print(f'The name {name_str} was added successfully!\n')

    print(Fore.WHITE + 'Please enter your Phone Number.')
    print('Data must contain only numbers.\n')
    print(Fore.YELLOW + 'Example: 00 353 892516666\n')
    print(Fore.WHITE)
    phone_number_str = input('Enter your phone number here: \n')
    print(' ')
    print(Fore.BLUE + 'Validating...\n')
    if any(x not in ALLOWED_PHONE_CHARACTERS for x in phone_number_str):
        print(Fore.RED + '\nError: Invalid character. :(\n')
        print('Israel just managed to Blueook himself.')
        print(Fore.GREEN)
        print('You can do it! This time use only numbers. :)')
        print(Fore.WHITE)
        get_phone_number()
    else:
        print(Fore.GREEN + 'No error. :)')
        print(f'The number {phone_number_str} was added successfully!\n')
        print(Fore.WHITE)
    
    print('In which country are you located?\n')
    print(Fore.YELLOW + 'Example: Ireland.\n')
    print(Fore.WHITE)
    location_str = input('Enter your location here: \n')
    print(Fore.GREEN)
    print(f'The location provided is {location_str}.\n')
    print(Fore.WHITE + 'Please enter your email.\n')
    print(Fore.YELLOW + 'Example: phil123@gmail.com.')
    print(Fore.WHITE)
    email_str = input('Enter your email here: \n')
    print(' ')
    print(Fore.GREEN)
    print(f'The email provided is {email_str}\n')
    print(Fore.WHITE)

def get_name_data():
    """
    Get Name and Surname data from the user.
    """
    name_str = input('Enter your name here: \n')
    print(' ')
    print(Fore.BLUE)
    print('Validating...\n')
    if any(x not in ALLOWED_NAME_CHARACTERS for x in name_str):
        print(Fore.RED + "Error: invalid character\n")
        print('Oh no! Gargamel is going to catch you.')
        print(Fore.GREEN + 'Use only letters to avoid this.')
        print(Fore.WHITE)
        get_name_data()
    else:
        print(Fore.GREEN)
        print("No error. :)\n")
        print(f'The name {name_str} was added successfully!')
        print(' ')
        print(Fore.WHITE)

def get_phone_number():
    """
    Get Phone number data from the user.
    """
    phone_number_str = input(Fore.WHITE + 'Enter your phone number here: \n')
    print(Fore.BLUE)
    print('Validating...\n')
    if any(x not in ALLOWED_PHONE_CHARACTERS for x in phone_number_str):
        print(Fore.RED + "Error: Invalid character, please enter numbers only.")
        print(Fore.WHITE)
        get_phone_number()
        print(' ')
    else:
        print(' ')
        print(Fore.GREEN)
        print("No error. :)\n")
        print(f'The number {phone_number_str} was added successfully!\n')
        print(Fore.WHITE)

def update_contact_worksheet(data):
    """
    Update worksheet with data values, add a new row with the list data provided.
    """
    print(Fore.BLUE + 'Updating contact worksheet...')
    contact = SHEET.worksheet('contact')
    contact.append_row(data)
    print('Contact worksheet updated successfully!\n')
    print(Fore.WHITE)
    add_new_entry()

def add_new_entry():
    new_entry = input(Fore.WHITE + 'Would you like to add a new collector to the Blueook? y/n: \n')
    if new_entry == 'y' or new_entry == 'Y':
        print(' ')
        get_contact_data()
        print(' ')
        update_contact_worksheet(data)
    else:
        print(' ')
        print(Fore.BLUE)
        print('Thanks for using The Blueook.')
        print('See you soon!\n')
 
def main():
    contact_data = (f'{name_str}, {phone_number_str}, {location_str}, {email_str}')
    data = contact_data.split(',')
    add_new_entry()

data = get_contact_data()
update_contact_worksheet(data)


