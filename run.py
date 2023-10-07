import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Back, Style
from tabulate import tabulate
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
ALLOWED_NAME_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
    'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ']
ALLOWED_PHONE_CHARACTERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ' ']

panel = """                                                  
              ### #           ##   #                       #   
                #  # # ###     # #  #  # # ### ### ### # # 
                #  ### ##      ##   #  # # ##  # # # # ##  
                #  # # ###     # #  ## ### ### ### ### # # 
                #              ##                               
"""
print(Fore.BLUE, panel)
print(Fore.YELLOW + '           *** Welcome to the Smurf collectors Contact Book ***')
print(Fore.WHITE)


def important_message():
    """
    This function displays a consent message to the users
    allowing the program or not to share their contact data with members.
    If the user consent the program will start.
    If the user does not consent, the program exit.
    """
    print('                                 IMPORTANT\n')
    print(' * As this is a public dataset we require your consent to share')
    print('   your contact details with other members of The Blueook Community.\n')
    print(' * You have a choice between sharing your phone number or email. :)\n')
    print(' * Please remember to be polite and respectful to all our members.\n')
    important = input(Fore.YELLOW + ' ◔ I hereby consent to sharing my contact details on The Blueook system. y/n: \n')
    print(' ')
    if important == 'y' or important == 'Y':
        print(' ')

    elif important == 'n' or important == 'N':
        print(Fore.WHITE + ' Hi! My name is Azriel and I am a Blueook member.')
        print(' I decided to share only my email and now I am part of this community.')          
        israel = """
:+**##:                     
   .  :#=                         Bye-bye!
       +#.         .          
       .*=        .==.     .  
        ==+=-.    ==*+===+*:  
       :+##****+=+====**++-   
     -*+##*****###- ..*=::=   
    .***#+=++*++*#+:.-=...    
    +#**.        =*#*+*:      
    -*#*:         :+***:   Azriel 
        """
        print(Fore.RED)
        print(israel)
        print(Fore.WHITE)
        print(' * We appreciated your visit.')
        print(' * We hope to see you again!\n')
        exit_program()
    else:
        panel = """                                                  
        ### #           ##   #                       #   
         #  # # ###     # #  #  # # ### ### ### # # 
         #  ### ##      ##   #  # # ##  # # # # ##  
         #  # # ###     # #  ## ### ### ### ### # # 
         #              ##                               
"""
        print(Fore.BLUE, panel)
        print(Fore.WHITE)
        print(' * Ooops! Not quite right.\n')
        print(Fore.GREEN + ' * If you want to say YES type "y".')
        print(Fore.RED + ' * If you want to say NO type "n".')
        print(Fore.WHITE)
        main()


def get_contact_data():
    """
    This function gets the name, phone, location
    and email contact from the user and place them
    into a list.
    """
    panel = """                                                  
        ### #           ##   #                       #   
         #  # # ###     # #  #  # # ### ### ### # # 
         #  ### ##      ##   #  # # ##  # # # # ##  
         #  # # ###     # #  ## ### ### ### ### # # 
         #              ##                               
    """
    print(Fore.BLUE, panel)
    print(Fore.YELLOW + '     ***Welcome to the Smurf collectors Contact Book***')
    print(Fore.WHITE)
    smurfette = """                    
**//***     
  /////    .         
  (#(    ,,,..         
  ((/   ,.,. ..          
  /((  ..,,***,,          
  ((  /*/%%&@#%/        Hi! I am Smurfette. Nice to meet you!
  /( /(/  *.& (//,      
  .((#&(((##(##%(/,,    This is a contact book for Smurf lovers!
  ((%%%&/%%,%((//**          
  /((%((#/,..,##/*          Please follow the instructons below,
  (#   *,...,/,,##((                     
  /#  ,*.....,,,                         and Blueook yourself...
 /(    #%  #(          
*((  ##%%(###(.    
.*(....,/......  Smurfette. 
"""
    print(smurfette)
    print(Fore.WHITE, Style.BRIGHT)
    print(' * Please enter your name and surname.')
    print(' * Data must contain only letters.')
    print(Fore.YELLOW)
    print(' > Example: Philip Grant.\n')
    print(Fore.CYAN + '--------------------------------------------------------------S2')
    name_str = get_name_data()
    print(Fore.CYAN + '--------------------------------------------------------------S2')    
    print(Fore.WHITE + ' * Please enter your Phone Number.')
    print(' * Data must contain only numbers.\n')
    print(Fore.YELLOW + ' > Example: 00 353 892516666\n')
    print(Fore.RED + ' * If you do not want to share your phone number.')
    print(Fore.WHITE + ' * Enter a single zero "0".\n')
    print(Fore.YELLOW + ' > Example: 0\n')
    print(Fore.CYAN + '--------------------------------------------------------------S2')
    phone_number_str = get_phone_number()
    print(Fore.CYAN + '--------------------------------------------------------------S2')    
    print(Fore.WHITE + ' * In which country are you located?\n')
    print(Fore.YELLOW + ' > Example: Ireland.\n')
    location_str = input(Fore.WHITE + ' ◔ Enter your location here: \n')
    print(Fore.GREEN)
    print(f' * The location provided is {location_str}.\n')
    print(Fore.CYAN + '--------------------------------------------------------------S2')
    print(Fore.WHITE + ' * Please enter your email.\n')
    print(Fore.YELLOW + ' > Example: phil123@gmail.com.\n')
    email_str = input(Fore.WHITE + ' ◔  Enter your email here: \n')
    print(' ')
    print(Fore.GREEN)
    print(f' * The email provided is {email_str}\n')
    print(Fore.WHITE)
    return [name_str, phone_number_str, location_str, email_str]


def get_name_data():
    """
    This function gets the name data from the user
    and returns the input question until receives valid data.
    """
    name_str = input(Fore.WHITE + ' ◔  Enter your name here: \n')
    print(' ')
    print(Fore.BLUE)
    print(' *_* Validating...\n')
    if any(x not in ALLOWED_NAME_CHARACTERS for x in name_str):
        print(Fore.RED + " * Error: invalid character\n")
        print(' * Oh no! Gargamel is going to catch you.')
        print(Fore.GREEN + ' * Use only letters to avoid this.')
        print(Fore.WHITE)
        name_str = get_name_data()
    else:
        print(Fore.GREEN)
        print(" * No error. :)\n")
        print(f' * The name {name_str} was added successfully!')
        print(' ')
        print(Fore.WHITE)
    return name_str


def get_phone_number():
    """
    This function gets the phone number data from the user
    and returns the input question until receives valid data.
    """
    contact_phone_number_str = input(Fore.WHITE + ' ◔  Enter your phone number here: \n')
    print(Fore.BLUE)
    print(' *_* Validating...\n')
    if any(x not in ALLOWED_PHONE_CHARACTERS for x in contact_phone_number_str):
        print(Fore.RED + " * Error: Invalid character, please enter numbers only.")
        print(Fore.WHITE)
        contact_phone_number_str = get_phone_number()
        print(' ')
    else:
        print(Fore.GREEN)
        print(" * No error. :)\n")
        print(f' * The number {contact_phone_number_str} was added successfully!\n')
    return contact_phone_number_str


def update_contact_worksheet(data):
    """
    This function updates the contact worksheet
    and appends a new row of data.
    """
    house = """
 .::.              
           =+=---:            
   -*=    +*+=--:-:           
    *-  .+*+===---=  ...        Welcome home...
    +-.-**++===--+******:       
   :*+****+++====+******+.      Now you are part of a select group!
   =*##**++++===++*#**##=.    
 :*###***++++=====+*****=:.     If you want to connect with other
.*####***++++++====++*++++:     collectors around the world, please
.*#####*****++++++++++====:::   access their contacts below.
 .=**#####****++++++***=  -==.
    ##***++==---:::.:**-      
    ##**++=--::::::.:=*+:     
   ++****+==-------::---.  Mushroom house. 
    """
    print(Fore.BLUE + ' *_* Updating contact worksheet...')
    contact = SHEET.worksheet('contact')
    contact.append_row(data)
    print(' *_* Contact worksheet updated successfully!\n')
    print(Fore.WHITE)
    print(house)
    print(' ')


def display_data():
    """
    This function gives the option of displaying the other
    member's contact data.
    """
    print(Fore.CYAN + '-------------------------------------------------------------------------S2')
    display_contact = input(Fore.WHITE + ' ◔  Would you like to display the collectors contact list? y/n: \n')
    print(' ')
    if display_contact == 'y' or display_contact == 'Y':
        contact = SHEET.worksheet('contact')
        data = contact.get_all_values()
        print(tabulate(data, tablefmt='fancy_grid'))
    else:
        israel = """
:+**##:                     
   .  :#=                        Bye-bye! 
       +#.         .          
       .*=        .==.     .  
        ==+=-.    ==*+===+*:  
       :+##****+=+====**++-   
     -*+##*****###- ..*=::=   
    .***#+=++*++*#+:.-=...    
    +#**.        =*#*+*:      
    -*#*:         :+***:   Azriel 
        """
        print(Fore.RED)
        print(israel)
        print(Fore.BLUE)
        print(' * Thanks for using The Blueook.')
        print(' * See you soon!\n')
        print(Fore.WHITE)


def exit_blueook():
    """
    This function gives the user the option to exit the program.
    Differently of the exit function, the exit_blueook function 
    let the user to decide if there is anything else left to do
    or simply exit.
    """
    print(' ')
    print(Fore.CYAN + '-------------------------------------------------------------------------S2')
    bye_blueook = input(Fore.WHITE + ' ◔  Would you like to exit The Blueook? y/n: \n')
    print(' ')
    if bye_blueook == 'y' or bye_blueook == 'Y':
        israel = """
:+**##:                     
   .  :#=                       Bye-bye!  
       +#.         .          
       .*=        .==.     .  
        ==+=-.    ==*+===+*:  
       :+##****+=+====**++-   
     -*+##*****###- ..*=::=   
    .***#+=++*++*#+:.-=...    
    +#**.        =*#*+*:      
    -*#*:         :+***:   Azriel 
        """
        print(Fore.RED)
        print(israel)
        print(Fore.BLUE)
        print(' * Thanks for using The Blueook.')
        print(' * See you soon!\n')
        print(Fore.WHITE)
    else:
        print(Fore.GREEN + ' * If you want to add a new contact then please exit and re-start the program.\n')
        print(Fore.BLUE + ' * If you want to access the contact list one more time type "y" or "Y" below.\n')
        print(Fore.RED + ' * If you want to exit The blueook type "n" or "N" below.\n')
        display_data()


def exit_program():
    """
    This function exit the system.
    This function is mostly used in the program when a quick exit is required.
    """
    exit(0)


def main():
    """
    Here lies all the program functions.
    This function serves as the starting point for The Blueook program execution.
    It controls The Blueook execution by directing the calls to other functions in the program.
    """
    important_message()
    data = get_contact_data()
    update_contact_worksheet(data)
    display_data()
    exit_blueook()
    exit(0)


main()


