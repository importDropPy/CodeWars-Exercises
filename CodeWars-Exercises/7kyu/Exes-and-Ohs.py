



# __/\\\\\\\\\\\\\\\__/\\\_______/\\\__/\\\\\\\\\\\\\\\_____/\\\\\\\\\\\___        
#  _\/\\\///////////__\///\\\___/\\\/__\/\\\///////////____/\\\/////////\\\_       
#   _\/\\\_______________\///\\\\\\/____\/\\\______________\//\\\______\///__      
#    _\/\\\\\\\\\\\_________\//\\\\______\/\\\\\\\\\\\_______\////\\\_________     
#     _\/\\\///////___________\/\\\\______\/\\\///////___________\////\\\______    
#      _\/\\\__________________/\\\\\\_____\/\\\_____________________\////\\\___   
#       _\/\\\________________/\\\////\\\___\/\\\______________/\\\______\//\\\__  
#        _\/\\\\\\\\\\\\\\\__/\\\/___\///\\\_\/\\\\\\\\\\\\\\\_\///\\\\\\\\\\\/___ 
#         _\///////////////__\///_______\///__\///////////////____\///////////_____





# _____/\\\\\\\\\_____/\\\\\_____/\\\__/\\\\\\\\\\\\____                           
#  ___/\\\\\\\\\\\\\__\/\\\\\\___\/\\\_\/\\\////////\\\__                          
#   __/\\\/////////\\\_\/\\\/\\\__\/\\\_\/\\\______\//\\\_                         
#    _\/\\\_______\/\\\_\/\\\//\\\_\/\\\_\/\\\_______\/\\\_                        
#     _\/\\\\\\\\\\\\\\\_\/\\\\//\\\\/\\\_\/\\\_______\/\\\_                       
#      _\/\\\/////////\\\_\/\\\_\//\\\/\\\_\/\\\_______\/\\\_                      
#       _\/\\\_______\/\\\_\/\\\__\//\\\\\\_\/\\\_______/\\\__                     
#        _\/\\\_______\/\\\_\/\\\___\//\\\\\_\/\\\\\\\\\\\\/___                    
#         _\///________\///__\///_____\/////__\////////////_____                   





# _______/\\\\\_______/\\\________/\\\_____/\\\\\\\\\\\___                         
#  _____/\\\///\\\____\/\\\_______\/\\\___/\\\/////////\\\_                        
#   ___/\\\/__\///\\\__\/\\\_______\/\\\__\//\\\______\///__                       
#    __/\\\______\//\\\_\/\\\\\\\\\\\\\\\___\////\\\_________                      
#     _\/\\\_______\/\\\_\/\\\/////////\\\______\////\\\______                     
#      _\//\\\______/\\\__\/\\\_______\/\\\_________\////\\\___                    
#       __\///\\\__/\\\____\/\\\_______\/\\\__/\\\______\//\\\__                   
#        ____\///\\\\\/_____\/\\\_______\/\\\_\///\\\\\\\\\\\/___                  
#         ______\/////_______\///________\///____\///////////_____



'''
SOLVE: Figure out whether a given argument passing through a function has same the amount of x's and o's

EXAMPLES:   ("ooxx",    True),
            ("xooxx",   False),
            ("ooxXm",   True), # Comparison is case-insensitive
            ("zpzpzpp", True), # when no 'x' and 'o' is present should return true
            ("zzoo",    False),
            ("oxOx",    True),
            ("",        True),

RESULT TYPE: Boolean
                                                                                                    '''











# define your function and parameters
def xo(s):
    
    # We use the lower() function to put all letters in lowercase and assign it to a variable to be further developed
    s = s.lower()
    
    # We use the count() function to count the amount of specified string letters in the argument 
    result = s.count('x') == s.count('o')
    
    # We print the result in the terminal/console/shell to see if it is working properly
    print(result)
    
    # print() function will not return a value to be utilized in other parts of the script
    # We return the result so that it can be utilized in other parts of the script
    # The result will return a Boolean value of either True of False since we utilized the '==' operator
    return result


# For this function call your argument must be a string
xo('xylophone')









'''
THESE ARE OTHER VIABLE AND WORKING SOLUTIONS FOR THIS EXERCISE
PLEASE MAKE SURE TO CHECK FOR SPELLING OR SYNTAX ERRORS
SO FAR I DID NOT FIND ANY MISTAKES BUT FEEL FREE TO HAVE A FIELD DAY 

**ANYTHING WITH A HASHTAG IN THE BEGINNING OF THE LINE IS A ONE LINE COMMENT IN PYTHON
ANYTHING WITH THREE ' <--IS A MULTIPLE LINE COMMENT, CLOSE MULTIPLE LINE COMMENT WITH AN ADDITIONAL THREE ' <--
####################################################################################################

# _______/\\\\\_______/\\\\\\\\\\\\\\\__/\\\________/\\\__/\\\\\\\\\\\\\\\____/\\\\\\\\\_____                                                                             
#  _____/\\\///\\\____\///////\\\/////__\/\\\_______\/\\\_\/\\\///////////___/\\\///////\\\___                                                                            
#   ___/\\\/__\///\\\________\/\\\_______\/\\\_______\/\\\_\/\\\_____________\/\\\_____\/\\\___                                                                           
#    __/\\\______\//\\\_______\/\\\_______\/\\\\\\\\\\\\\\\_\/\\\\\\\\\\\_____\/\\\\\\\\\\\/____                                                                          
#     _\/\\\_______\/\\\_______\/\\\_______\/\\\/////////\\\_\/\\\///////______\/\\\//////\\\____                                                                         
#      _\//\\\______/\\\________\/\\\_______\/\\\_______\/\\\_\/\\\_____________\/\\\____\//\\\___                                                                        
#       __\///\\\__/\\\__________\/\\\_______\/\\\_______\/\\\_\/\\\_____________\/\\\_____\//\\\__                                                                       
#        ____\///\\\\\/___________\/\\\_______\/\\\_______\/\\\_\/\\\\\\\\\\\\\\\_\/\\\______\//\\\_                                                                      
#         ______\/////_____________\///________\///________\///__\///////////////__\///________\///__                                                                     





# _____/\\\\\\\\\\\_________/\\\\\_______/\\\______________/\\\________/\\\__/\\\\\\\\\\\\\\\__/\\\\\\\\\\\_______/\\\\\_______/\\\\\_____/\\\_____/\\\\\\\\\\\___        
#  ___/\\\/////////\\\_____/\\\///\\\____\/\\\_____________\/\\\_______\/\\\_\///////\\\/////__\/////\\\///______/\\\///\\\____\/\\\\\\___\/\\\___/\\\/////////\\\_       
#   __\//\\\______\///____/\\\/__\///\\\__\/\\\_____________\/\\\_______\/\\\_______\/\\\___________\/\\\_______/\\\/__\///\\\__\/\\\/\\\__\/\\\__\//\\\______\///__      
#    ___\////\\\__________/\\\______\//\\\_\/\\\_____________\/\\\_______\/\\\_______\/\\\___________\/\\\______/\\\______\//\\\_\/\\\//\\\_\/\\\___\////\\\_________     
#     ______\////\\\______\/\\\_______\/\\\_\/\\\_____________\/\\\_______\/\\\_______\/\\\___________\/\\\_____\/\\\_______\/\\\_\/\\\\//\\\\/\\\______\////\\\______    
#      _________\////\\\___\//\\\______/\\\__\/\\\_____________\/\\\_______\/\\\_______\/\\\___________\/\\\_____\//\\\______/\\\__\/\\\_\//\\\/\\\_________\////\\\___   
#       __/\\\______\//\\\___\///\\\__/\\\____\/\\\_____________\//\\\______/\\\________\/\\\___________\/\\\______\///\\\__/\\\____\/\\\__\//\\\\\\__/\\\______\//\\\__  
#        _\///\\\\\\\\\\\/______\///\\\\\/_____\/\\\\\\\\\\\\\\\__\///\\\\\\\\\/_________\/\\\________/\\\\\\\\\\\____\///\\\\\/_____\/\\\___\//\\\\\_\///\\\\\\\\\\\/___ 
#         ___\///////////__________\/////_______\///////////////_____\/////////___________\///________\///////////_______\/////_______\///_____\/////____\///////////_____

####################################################################################################







# Define your function and its parameters in the paranthesis
def xo(s):

    # We utilize the lower() function to lower case all letters in the argument
    # We utilize the count() function to count the amount of repetitive specified character strings
    # We utilize the double equal operator to tell us if the amount of lower case 'x's is equal to the amount of lowercase 'o's
    # The returned value should give us a Boolean value of either True of False depending on the argument inputted for the function call
    return s.lower().count('x') == s.lower().count('o')


# Call your function here
xo(xylophone)





####################################################################################################



# There is another solution below that is similar to this one with notes

def xo(s):

    # We assign exes aka 'x's to the value of 0
    exes = 0
    
    # We assign ohs aka 'o's to the value of 0
    ohs = 0

    # We utilize a for loop that iterates through every letter(c) in the argument called from the function call
    # We also make sure that the entire argument 's' is in lower case with the lower() functionality
    for c in s.lower():
        
        # If the current character in the string when lower cased is equal to 'x' then we increment 'exes' by + 1
        if c == 'x':
        exes += 1
        
        # If the current character in the string when lower cased is equal to 'o' then we increment 'ohs' by + 1
        elif c == 'o':
        ohs += 1

    # - After the last iteration in the for loop, we then will compare the values of the variables exes and ohs 
    #       to see if they return True or False
    return exes == ohs


# Call your function here
xo('xylophone')


####################################################################################################



# There is another solution below that utilizes this same function and library with notes and comments



# We import the functionality of Counter from the library collections at the top of our Python file
from collections import Counter

def xo(s):

    # - We assign the variable 'd' to the Counter() functionality and make sure to make the entire 
    #       string lowercase by use of the lower() functionality
    d = Counter(s.lower())
    
    # We then return the 'key: value' pairs of 'x' and 'o' and compare their integer values by use of the '==' operator
    # This line will return a Boolean value that is either True or False depending on the argument called in the function call
    return d.get('x', 0) == d.get('o', 0)



# Call your function here
xo('xylophone')






####################################################################################################


# This is a ternary operator that assigns True if 's.lower().count('x') == s.lower().count('o')' is satisfied
# Otherwise 'else False' will fire meaning the word has an unequal amount of exes and ohs

def xo(s):
    return True if s.lower().count('x') == s.lower().count('o') else False
    
# Call your function here
xo('xylophone')



####################################################################################################


# - Another clever solution that uses the 'is' operator to return either a True or False Boolean value upon 
#       counting the amount of exes and ohs and comparing their values
# - Note the use of lower() function to make all the x's a value that can be counted by the count() functionality
# Otherwise, clerical errors will arise because X does not equal x, and, similarly, Y does not equal y

def xo(s):
    return s.lower().count("x") is s.lower().count("o")


# Call your function here
xo('xylophone')


####################################################################################################





import re

# - Using regex, the number of x's and o's are extracted from the test string
#       and returned as a tuple.
def get_amounts(test):
    return(len(re.findall("[Xx]", test)), len(re.findall("[Oo]", test)))

# - The results passed to this function will evaluate to True if they are equal
#       and False if they are not.
def eval_results(results):
    if results[0] == results[1]:

        return True
    else:

        return False

# - Call the get_amounts( ... ) and eval_results( ... ) functions and return the
#       result.
def xo(test):
    result = get_amounts(test)
    return eval_results(result)


# Call your function here
xo('xylophone')



####################################################################################################



def xo(s):
    
    # Set our X count to 0
    countX = 0
    
    # Set our O count to 0
    countO = 0
    
    for i in s:
        
        
        # the '|' operator means OR
        # Thus, if either statement is satisfied then countX will increment by 1
        if (i == 'X') | (i == 'x'):
            countX = countX + 1
            
        elif (i == 'O') | (i == 'o'):
            countO = countO + 1
            
    
    # Compare our changed countX and countO, respectively, and see if their values are equal
    if countX == countO:     
        return True
    else:
        return False

# Call your function here
xo('xylophone')



####################################################################################################





# A clever solution that adds a increments a count by 1 from the base value 0 if it is an 'x' or 'X'
#       and subtracts 1 if it is an 'o' or 'O'
# Thusly, you will always be able to know if a string has an equal amount of exes and ohs

def xo(s):
    count = 0
    for i in s:
        if i in 'Xx':
            count += 1
        elif i in 'Oo':
            count -= 1
    return count == 0



# Call your function here
xo('xylophone')






####################################################################################################


# Example of a lambda function using the '==' operator to return a Boolean value of either True of False depending on the argument called
# We wrap the expression with a print() function so that we can see the Boolean value that tells us if there are equal amount of exes and ohs

xo = lambda s: print(s.lower().count('x') == s.lower().count('o'))




# Call your function here
xo('xylophone')







####################################################################################################



# This pandas Python library is become my scope at the moment and additional updates must be brought in the future
# So far this function may not work properly
# Please check back for updates


def xo(s):
    
    # - pandas is a fast, powerful, flexible and easy to use open source data analysis 
    #       and manipulation tool, built on top of the Python programming language. 
    import pandas as pd
    
    # - By use of a Ternary Operator we utilize a for loop to iterate through ever 
    #       character in the string and turn it into lowercase by use of lower()
    words = [i.lower() for i in s]
    
    # Assign a dataframe pandas function to the variable 'data' that indexes the range as big as the length of the argument called
    data = pd.DataFrame(index = range(len(words)))
    
    
    for i,j in enumerate(words):
        data.loc[i,j] = 1
    
    tem = list(data.columns)
    
    tem1 = [i for i in tem]
    
    print(tem1)
    
    
    if 'x' not in tem1 and 'o' not in tem1:
        return True
    if 'x' in tem1 and 'o' in tem1:
        if data['x'].sum() == data['o'].sum():
            return True
    return False


# Call your function here
xo('xylophone')






####################################################################################################



# __import__() is a built-in function in Python that is used to dynamically import modules
# We import the 'collections' library and assign the Counter() function with the lower case functionality inside of it to the 'c' variable
# We then return 'c' as an integer that has counted the amount of specified letters in the string with the Counter() functionality
# The result should return a Boolean value that is either False or True 

def xo(s):
    c = __import__('collections').Counter(s.lower())
    return c['x'] == c['o']

# Call your function here
xo('xylophone')


####################################################################################################



# Ternary operator inside of a for loop that iterates through the argument called in the function call
# A sum() function is used here to add all the returned values inside of the sum() function
# At the end of the expression in the sum it says 'for c in s'
# This 'for c in s' iterates through every letter in the argument and finds either Xx's or Oo's
# For every 'X or x' we return a '-1' and for every 'O or o' we return a '1'
# Once the loop has gone through every letter in the string it will add all the values together with the sum() functionality
# For an imbalance of exes and ohs in a word, the value returned will not equal to 0 thus 'False' will be returned
# False tells us that there are either a higher or lower number or exes and/or ohs in the word
# Whereas, True will tell us that the word has an equal amount of exes and ohs
# While this may not us exactly how many exes or ohs there are in the word, still, it can tell us whether the word has equal amount of exes and ohs

def xo(s):
    return 0 == sum((-1 if c in 'Xx' else 1 if c in 'Oo' else 0) for c in s)

# Call your function here
xo('xylophone')


####################################################################################################




def xo(s):

    # We assign the variable 's' to the lower() function to make all the characters in the string lower case
    s = s.lower()
    
    # Set the x count to 0
    countx = 0
    
    # Set the y count to 0
    county = 0
    
    # We utilize a for loop that iterates for as long as the length aka 'len()' or the amount of letters in the string
    for i in range(len(s)):
    
        # This if statement will target the character and make sure it is lower case then see if it equals 'x'
        # If it does equal 'x' then countx will increment by + 1
        if s[i] == "x":
            countx = countx + 1
        
        # This if statement will target the character and make sure it is lower case then see if it equals 'o'
        # If it does equal 'o' then county will increment by + 1
        elif s[i] == "o":
            county = county + 1
    
    
    
    
    # This if statement will compare the changed values of the variables countx and county 
    # If countx does equal county then the if statement will be satisfied and 'return True' will fire
    if countx == county:
        return True
    
    
    # This is more of an enforcement line of code making sure that no bugs will arise
    # Sometimes code can run and the variables dont change after the iterations in the for loop
    # Even though countx and county might equal eachother, there is no statement definitively saying countx = county
    # It is only by the '==' operator that we can compare the values and realize their relationship
    # Thus, we make sure that if the variables are unchanged or equate both to 0 that they do indeed equal eachother
    # For example, in higher level classes of Mathematics 0 never quite always equals 0, and this is the case for every number
    # In a perfect world, whole numbers surely would exist but that is not the case
    # On top of that, another problem that might occur is that no exes or ohs were found so the program will return False
    # For this exercise, if no exes or ohs are found then we want the program to return True
    elif countx == 0 and county == 0:
        return True
    else:
        return False

# Call your function here
xo('xylophone')




####################################################################################################





def xo(s):

    # Lets get the variable 'x' assigned to the integer 0
    x=0
    
    # Lets get the variable 'y' assigned to the integer 0
    y=0
    
    # This for loop will iterate through every character in the string of the argument called in the function call
    for string in s:
        
        # This if statement will check if the current instance's text character is equal to 'x', 'X', 'o', or 'O'
        # If the current instance's character is equal to any of the x's then the variable x will increment by 1
        
        if string == "x":
            x += 1
        if string == "X":
            x += 1
        
        # If the current instance's character is equal to any of the y's then the variable y will increment by 1
        if string == "o":
            y += 1
        if string == "O":
            y += 1
    
    
    
    # - Once the for loop has iterated through all characters in the string then, 
    #       depending on the argument, your x and y variables will have changed
    # - This if statement will compare the new values of x and y to see if they equal eachother
    # - If x = y then the if statement will be satisfied and the Boolean value 'True' will be returned
    # - Otherwise, if the statement is not satisfied then the code block inside the statement will not fire
    # - And if the code block inside the if statement does not fire then that means we return 'False'abs
    # - In other words, if we do not satisfy the if statement then that means the argument called does not 
    #       have an equal amount of exes and ohs
    if x==y:
        return True
    return False

# Call your function here
xo('xylophone')




####################################################################################################








# this works in Visual Studio Code
# make sure to create a virtual environment with pip
# visit pip website and install pip
# once you have pip open up your terminal(CTRL + `) and make sure you are at the main directory to your folder
# use the 'pipenv install' to create your virtual environment files for pipenv in your directory folder
# once it is done use the 'pipenv shell' to activate your shell
# make sure you are using the right environment by using the 'pipenv --venv' command
# if all is going well then use the 'pip install termcolor' to install terminal coloring
# make sure to import os aka operating system commands functionality
# after that make sure to launch this code with the 'py test.py' command instead of firing it off in your editor as errors can arise
from termcolor import colored
import os

# This line of code allows for color to be used when using the print() function in the terminal
os.system('color')



def xo(s):

    # - For this line below we will assign the variable named string to the entire argument in lower case 
    #       letters by use of lower() functionality
    string = s.lower()
    
    # We assign dct to dictionary brackets which means that this is an empty dictionary at the moment
    dct = {}

    # - for loop will iterate through every character in the array saved in the 'string' variable that is all 
    #       lower case because of the lower() functionality
    for i in string:
        
        # - if statement that asks in the specific iteration if the specific letter 'i' in the array is equal to 'x'
        if i == 'x':
            
            # - The get() method returns the value of the item with the specified key
            # - Dictionaries contain 'key: value' pairs
            # - For the 'key' called 'x' we assign this to the functionality of the get() functionality
            #       returning the following: 'x: 0' then we add + 1 because the if statement analyzed the 
            #           letter in this iteration and said it was an 'x'
            # - Thusly, the key 'x' in the dct dictionary has changed from 'x: 0' to 'x: 1' for this iteration
            # - If on the next iteration there is another x then 'x: 2'
            dct['x'] = dct.get('x', 0) + 1
            
        
        elif i == 'o':
            
            dct['o'] = dct.get('o', 0) + 1
            
    # - If any characters from the argument are NOT in the string variable, or, 
    #       if the amount of 'x' or 'o' 'key: value' pairs are equal then return True
    if not string or dct.get('x', 0) == dct.get('o', 0):
        
        # We utilize these print() functions to see what is actually going on behind the scenes
        print('')
        print(f"The amount of 'x's found in {colored(string.upper(), 'blue')} were {dct.get('x', 0)}")
        print(f"The amount of 'o's found in {colored(string.upper(), 'blue')} were {dct.get('o', 0)}")
        print(f"The 'not string' condition for {colored(string.upper(), 'blue')} returned as {not string}")
        print(f"The 'dct.get('x', 0) == dct.get('o', 0)' condition for {colored(string.upper(), 'blue')} returned as {dct.get('x', 0) == dct.get('o', 0)}")
        print('')
        
        # return True if any of the if statement conditions are met by utilization of the 'or' operator for either condition to be met
        return True
    
    
    
    # We utilize these print() functions to see what is actually going on behind the scenes
    print('')
    print(f"The amount of 'x's found in {colored(string.upper(), 'red')} were {dct.get('x', 0)}")
    print(f"The amount of 'o's found in {colored(string.upper(), 'red')} were {dct.get('o', 0)}")
    print(f"The 'not string' condition for {colored(string.upper(), 'red')} returned as {not string}")
    print(f"The 'dct.get('x', 0) == dct.get('o', 0)' condition for {colored(string.upper(), 'red')} returned as {dct.get('x', 0) == dct.get('o', 0)}")
    print('')
    
    # returns false when the only if statement in this program is not satisfied
    # in other words, the argument passed into a function call, the word, does not have equal exes and ohs
    return False

# Call your function here
xo('xylophone')
xo('xylophonx')

# Please remember if you fire this code in your editor it may return a 'missing module' error
# make sure to use the 'py test.py' command if you have navigated by changing directory to the folder with the test.py file
# If 'py test.py' does not work then use 'python test.py'
# If none of this is working then change every {colored(string.upper(), 'red')} inside all 8 formatted strings to (string.upper()} <-- copy and paste






####################################################################################################


# - We import the Regular Expression library to utilize the findall() functionality to return all 'X or x's
#       and 'O or o's in the argument that was called in the function call
# - Once we have assigned the 'x_string' and 'o_string' variables, respectively, to the returned array of 'xX' or 'oO' replications, then,
#       we insert the 'x_string' and 'o_string' variables that contain an array of possibly repetitive 'xX's or 'oO's into len() functions, and,
#           use the '==' operator to compare the two integer values the len() function returned from counting the amount of letters in each variable
# - That functionality will tell us whether the word has equal amount of exes or ohs
# - Python built in functions shows to already be able to solve this Kata without importing any library, however, these type of solutions
#       can be utilized in the right situations where Python built ins might not be able to



import re


def xo(s):

    x_string = re.findall(r'[xX]', s)
    print(x_string)
    
    o_string = re.findall(r'[oO]', s)
    print(o_string)
    
    
    print(len(x_string) == len(o_string))
    return len(x_string) == len(o_string)


# Call your function here
xo('xylophone')




####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################

                                                                                                    '''

