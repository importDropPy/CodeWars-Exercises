



# _____/\\\\\\\\\\\____/\\\\____________/\\\\_____/\\\\\\\\\_____/\\\______________/\\\______________/\\\\\\\\\\\\\\\_____/\\\\\\\\\\\____/\\\\\\\\\\\\\\\_        
#  ___/\\\/////////\\\_\/\\\\\\________/\\\\\\___/\\\\\\\\\\\\\__\/\\\_____________\/\\\_____________\/\\\///////////____/\\\/////////\\\_\///////\\\/////__       
#   __\//\\\______\///__\/\\\//\\\____/\\\//\\\__/\\\/////////\\\_\/\\\_____________\/\\\_____________\/\\\______________\//\\\______\///________\/\\\_______      
#    ___\////\\\_________\/\\\\///\\\/\\\/_\/\\\_\/\\\_______\/\\\_\/\\\_____________\/\\\_____________\/\\\\\\\\\\\_______\////\\\_______________\/\\\_______     
#     ______\////\\\______\/\\\__\///\\\/___\/\\\_\/\\\\\\\\\\\\\\\_\/\\\_____________\/\\\_____________\/\\\///////___________\////\\\____________\/\\\_______    
#      _________\////\\\___\/\\\____\///_____\/\\\_\/\\\/////////\\\_\/\\\_____________\/\\\_____________\/\\\_____________________\////\\\_________\/\\\_______   
#       __/\\\______\//\\\__\/\\\_____________\/\\\_\/\\\_______\/\\\_\/\\\_____________\/\\\_____________\/\\\______________/\\\______\//\\\________\/\\\_______  
#        _\///\\\\\\\\\\\/___\/\\\_____________\/\\\_\/\\\_______\/\\\_\/\\\\\\\\\\\\\\\_\/\\\\\\\\\\\\\\\_\/\\\\\\\\\\\\\\\_\///\\\\\\\\\\\/_________\/\\\_______ 
#         ___\///////////_____\///______________\///__\///________\///__\///////////////__\///////////////__\///////////////____\///////////___________\///________





# __/\\\\\\\\\\\__/\\\\\_____/\\\__/\\\\\\\\\\\\\\\__/\\\\\\\\\\\\\\\_____/\\\\\\\\\\\\__/\\\\\\\\\\\\\\\____/\\\\\\\\\_____                                       
#  _\/////\\\///__\/\\\\\\___\/\\\_\///////\\\/////__\/\\\///////////____/\\\//////////__\/\\\///////////___/\\\///////\\\___                                      
#   _____\/\\\_____\/\\\/\\\__\/\\\_______\/\\\_______\/\\\______________/\\\_____________\/\\\_____________\/\\\_____\/\\\___                                     
#    _____\/\\\_____\/\\\//\\\_\/\\\_______\/\\\_______\/\\\\\\\\\\\_____\/\\\____/\\\\\\\_\/\\\\\\\\\\\_____\/\\\\\\\\\\\/____                                    
#     _____\/\\\_____\/\\\\//\\\\/\\\_______\/\\\_______\/\\\///////______\/\\\___\/////\\\_\/\\\///////______\/\\\//////\\\____                                   
#      _____\/\\\_____\/\\\_\//\\\/\\\_______\/\\\_______\/\\\_____________\/\\\_______\/\\\_\/\\\_____________\/\\\____\//\\\___                                  
#       _____\/\\\_____\/\\\__\//\\\\\\_______\/\\\_______\/\\\_____________\/\\\_______\/\\\_\/\\\_____________\/\\\_____\//\\\__                                 
#        __/\\\\\\\\\\\_\/\\\___\//\\\\\_______\/\\\_______\/\\\\\\\\\\\\\\\_\//\\\\\\\\\\\\/__\/\\\\\\\\\\\\\\\_\/\\\______\//\\\_                                
#         _\///////////__\///_____\/////________\///________\///////////////___\////////////____\///////////////__\///________\///__                               





# __/\\\\\\\\\\\__/\\\\\_____/\\\_                                                                                                                                 
#  _\/////\\\///__\/\\\\\\___\/\\\_                                                                                                                                
#   _____\/\\\_____\/\\\/\\\__\/\\\_                                                                                                                               
#    _____\/\\\_____\/\\\//\\\_\/\\\_                                                                                                                              
#     _____\/\\\_____\/\\\\//\\\\/\\\_                                                                                                                             
#      _____\/\\\_____\/\\\_\//\\\/\\\_                                                                                                                            
#       _____\/\\\_____\/\\\__\//\\\\\\_                                                                                                                           
#        __/\\\\\\\\\\\_\/\\\___\//\\\\\_                                                                                                                          
#         _\///////////__\///_____\/////__                                                                                                                         





# _____/\\\\\\\\\_____/\\\\\_____/\\\_                                                                                                                             
#  ___/\\\\\\\\\\\\\__\/\\\\\\___\/\\\_                                                                                                                            
#   __/\\\/////////\\\_\/\\\/\\\__\/\\\_                                                                                                                           
#    _\/\\\_______\/\\\_\/\\\//\\\_\/\\\_                                                                                                                          
#     _\/\\\\\\\\\\\\\\\_\/\\\\//\\\\/\\\_                                                                                                                         
#      _\/\\\/////////\\\_\/\\\_\//\\\/\\\_                                                                                                                        
#       _\/\\\_______\/\\\_\/\\\__\//\\\\\\_                                                                                                                       
#        _\/\\\_______\/\\\_\/\\\___\//\\\\\_                                                                                                                      
#         _\///________\///__\///_____\/////__                                                                                                                     





# _____/\\\\\\\\\_______/\\\\\\\\\________/\\\\\\\\\_________/\\\\\\\\\_____/\\\________/\\\_                                                                      
#  ___/\\\\\\\\\\\\\___/\\\///////\\\____/\\\///////\\\_____/\\\\\\\\\\\\\__\///\\\____/\\\/__                                                                     
#   __/\\\/////////\\\_\/\\\_____\/\\\___\/\\\_____\/\\\____/\\\/////////\\\___\///\\\/\\\/____                                                                    
#    _\/\\\_______\/\\\_\/\\\\\\\\\\\/____\/\\\\\\\\\\\/____\/\\\_______\/\\\_____\///\\\/______                                                                   
#     _\/\\\\\\\\\\\\\\\_\/\\\//////\\\____\/\\\//////\\\____\/\\\\\\\\\\\\\\\_______\/\\\_______                                                                  
#      _\/\\\/////////\\\_\/\\\____\//\\\___\/\\\____\//\\\___\/\\\/////////\\\_______\/\\\_______                                                                 
#       _\/\\\_______\/\\\_\/\\\_____\//\\\__\/\\\_____\//\\\__\/\\\_______\/\\\_______\/\\\_______                                                                
#        _\/\\\_______\/\\\_\/\\\______\//\\\_\/\\\______\//\\\_\/\\\_______\/\\\_______\/\\\_______                                                               
#         _\///________\///__\///________\///__\///________\///__\///________\///________\///________






'''

SOLVE:

    Given an array of integers your solution should find the smallest integer.
                                                                                                    


EXAMPLES:

    Given [34, 15, 88, 2] then your solution will return 2
    Given [34, -345, -1, 100] then your solution will return -345
    You can assume, for the purpose of this kata, that the supplied array will not be empty.
                                                                                                    




'''





# There are many more solutions but this one is the one I used firstly
# However, learning the different types of solutions is vital as you come across harder Python exercises

# first define your function and put a place holder name like 'arr' to mean array but also just to input any argument when you call the function
def find_smallest_int(arr):

    # assign the function min() to getmin and apply the 'arr' argument inside the min paranthesis functionality
    # we dont have to assign min(arr) to a variable but for the sake of seeing a result in the console we want to do this
    getmin = min(arr)

    # print() your getmin variable so that we can see the result in console
    print(getmin)

    # always return your variable
    # return min(arr) works just the same but we utilize the variable in this example
    return getmin

# call your function here with an argument of your choosing
find_smallest_int([23,45,1,-2,7,8])










'''
THESE ARE OTHER VIABLE AND WORKING SOLUTIONS FOR THIS EXERCISE
PLEASE MAKE SURE TO CHECK FOR SPELLING OR SYNTAX ERRORS
SO FAR I DID NOT FIND ANY MISTAKES BUT FEEL FREE TO HAVE A FIELD DAY 

**ANYTHING WITH A HASHTAG BEFORE THE IT IS A ONE LINE COMMENT IN PYTHON
ANYTHING WITH THREE ' <--IS A MULTIPLE LINE COMMENT, CLOSE MULTIPLE LINE COMMENT WITH AN ADDITIONAL THREE ' <--
####################################################################################################



# CLEVER SOLUTION
# sort function in this case sorts the numbers from minimum to maximum



def findSmallestInt(arr):
    
    #sort array
    arr.sort()
    
    # assign a variable to a desired expression
    arraySorted = arr.sort()
    # print the variable so that you can see it
    print(arraySorted)

    # assign the answer or result to the desired expression
    result = arr[0]
    # print the result to see it
    print(result)

    # return the result
    return arr[0]

# call your function with a desired argument which can be any array of integers
findSmallestInt([23,45,1,-2,7,8])


####################################################################################################


# this one operates by comparing the two integers by use of '<' (less than operator),
#     and, then, replaces the smallest number in the array 'smallest' before returning its value, after 
#     it has iterated through the entire array by use of a for loop 'for i in range(0,len(arr)):


def findSmallestInt(arr):
    smallest = []
    for i in range(0,len(arr)):
        if (arr[i] < smallest):
            smallest = arr[i]
            # put a print() function here if you like to see every iteration's result
    
    # print(smallest) if you want to see what your function is doing
    # or assign smallest to a variable with the assignment operator '=' to reduce spaghetti code
    return smallest


# call your function below and give it an argument



####################################################################################################


# this script simply does the same thing with the sort function but before that checks if it is an integer with 'assert'


def findSmallestInt(arr):
    """
    input: arr, a list of integers
    output: smallest integer in arr
    """
    
    # check that each element is an int
    for num in arr:
        assert type(num) == int
    
    # sort array
    arr.sort()
    
    # return smallest value
    return arr[0]

# call your function here and put print() functions wherever you like to see what is going on inside your script




####################################################################################################




# Clever use of our original min() function but in a different way


def findSmallestInt(arr):
    min = arr[0]
    for item in arr:
        if min > item:
            min = item
    return min

# call your function here





####################################################################################################





# Clever solution

def find_smallest_int(arr):
    return sorted(arr)[0]

# call your function here




####################################################################################################



# utilizing a lambda function 
# and using the reduce() function

def findSmallestInt(arr):
    #Code here
    return reduce(lambda x,y: x if x<y else y, arr) 

# call your function here




####################################################################################################



# Ternary lambda function utilizing sort() function


findSmallestInt = lambda a: sorted(a)[0] and print(sorted(a)[0])



# call your function here



####################################################################################################


# A proposed advanced solution to obtaining minimum numbers in a huge data payload most likely
# this script has not been met with scrutiny so please use this script at your own damage


class IntArr():
    def __init__(self, arr = []): # initialize
        self.arr = arr
        
    def Length(self): # find length of arr
        c = 0
        
        for i in self.arr:
            c += 1
        
        return c
        
    def checkArr(self): # checks array 
        c = 0
        
        for i in self.arr:
            if type(i) != type(0):
                raise Exception("Are you stupid????????? The class called IntArr!!!!!!!!!!!! Array of INTEGERS!!!!!!!!!!!")
            else:
                c += 1
                
        if c != len(self.arr):
            raise Exception("WTF??????????")
    
    def summArr(self):
        self.checkArr()
        
        summ = 0
        
        for i in self.arr:
            summ += i
            
        return summ # returns integer ([] => 0)
    
    def findMax(self, n):
        self.checkArr()
        
        arr = self.arr
        
        if n < 1:
            print("Why are you so stupid?????????")
            return []
        
        maxes = [0] * n
        max = -1e100
        
        for _ in range(n-1, -1, -1): # find the maximum vulue
            for i in arr:
                if max < i:
                    max = i
            maxes[_] = max
            del arr[arr.index(max)]
            max = -1e100
            
        return maxes # returns sorted array of n max values (if n < 1 returns [])
    
    def findMin(self, n):
        self.checkArr()
        
        arr = self.arr
        
        if n < 1:
            print("Why are you so stupid?????????")
            return []
        
        mins = [0] * n
        min = 1e100
        
        for _ in range(n): # find the maximum vulue
            for i in arr:
                if min > i:
                    min = i
            mins[_] = min
            del arr[arr.index(min)]
            min = 1e100
            
        return mins # returns sorted array of n min values (if n < 1 returns [])
    
    def Sort(self): # sorts with no changing of main array
        self.checkArr()
        
        # I can use sorted() or .sort(), but it's not interesting
        array = self.arr
        
        # If the input array contains fewer than two elements,
        # then return it as the result of the function
        if len(array) < 2:
            return array
        
        low, same, high = [], [], []
        
        # Select your `pivot` element randomly
        pivot = array[randint(0, len(array) - 1)]
        
        for i in array:
            # Elements that are smaller than the `pivot` go to
            # the `low` list. Elements that are larger than
            # `pivot` go to the `high` list. Elements that are
            # equal to `pivot` go to the `same` list.
            
            if i < pivot:
                low.append(i)
            elif i == pivot:
                same.append(i)
            elif i > pivot:
                high.append(i)
                
            # The final result combines the sorted `low` list
            # with the `same` list and the sorted `high` list
            
        return self.Sort(low) + same + self.Sort(high)
    
def find_smallest_int(a):
    # I can use many ways: 1) sorted_array[0]; 2) arr.findMin() and etc., but it doesn't interesting
    # It is my favourite :)
    intarr = IntArr() 
    intarr.arr = a;
    
    length = intarr.Length()
    summ = intarr.summArr()
    maxes = intarr.findMax(length-1)
    ans = 0
    ans += summ
    
    for i in maxes:
        ans -= i
    
    return ans




# call your function here




####################################################################################################



# pop() function removes an element of an array at a specified position
# since the specified position is not said here then we rely on assigning the specific iteration of the for loop we are in to be equal to element which is equal to pop()
# by use of less than '<' operator we can evaluate whether an integer is higher or lower

def find_smallest_int(arr):
    element = arr.pop()
    for e in arr:
        if e < element:
            element = e
           
    return element and print(element)

# call your function here
find_smallest_int([3,4,5,65,3,6,73])







####################################################################################################




# can import system to use the sys.maxsize functionality
# in certain cases this may prove to be useful


import sys

def find_smallest_int(arr):
    my_int = sys.maxsize
    for integer in arr:
        if integer < my_int:
            my_int = integer
    return my_int


# call your function here





####################################################################################################


# using the less than operator to identify in a for loop the minimum by comparing every number to the last iterations number and saving it to x if it is lower than the last one
# on the final iteration you will achieve the smallest integer and then return it



def find_smallest_int(arr):
    x = None
    for i in arr:
        if x == None or i < x:
            x = i
    return x


# call your function here



####################################################################################################




# how to import this functionality into other files with a shorter name
# put the below line at the top of your python file to use 
from find_smallest_int.py import YourFunctionName as YourFunctionsNameButShorter








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

