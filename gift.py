from datetime import datetime
from termcolor import colored


def heart_print():
    
    heart = """
         *********     *********
       ************   ************
     *************** ***************
    *********************************
    *********************************
    *********************************
     *******************************
       ***************************
         ***********************
           *******************
             ***************
               ***********
                 *******
                  *****
                    *
    """
    print(colored((heart), "red"))


def days_passed_since(start_date):
   
    start_date = datetime.strptime(start_date, '%d.%m.%Y')
    current_date = datetime.now()
    delta = current_date - start_date
    return delta.days

def message_print():

    start_date = "10.08.2023"
    days_passed = days_passed_since(start_date)
    print(colored(
        "Oh, how time flies when love is in the air!\n"
        "It's been {} days since your enchanting smile"
        "stole my heart!".format(days_passed), "green"))
    
message_print()
heart_print()