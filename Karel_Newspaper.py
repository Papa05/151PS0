#====================================================
# Filename: Karel_Newspaper.py
# 
# Your name:papa lynch
# Who did you work with (if anyone)?: prof. calvin 
# Estimate for time spent (in hrs)?: 4hr im still no good
#====================================================

# I've just laid out a basic starting function below. 
# While this problem is fairly simple, you should still practice
# the good habit of writing helper functions to decompose the problem
# into smaller pieces. I have provided you with a template for the
# main function and then 3 helping functions as outlined in the pdf

import karel


def main():
    """ Function to cause Karel to retrieve the newspaper. """
    # You can add your sequence of commands below here!
    # Remember you can use the defined helper functions!
    move()
    move()
    move()
    turn_left()
    pick_beeper()
   
    
    
    


def move_to_newspaper():
    """ Helping function to move Karel to the newspaper location. """
     move()



def pick_up_paper():
    """ Helping function to have Karel pick up the newspaper. """
    # Yes, this will probably be VERY simple and mshort
    pick_beeper()



def return_to_start():
    """ Helping function to move Karel back to its starting position. """
    move()
    turn_left()
