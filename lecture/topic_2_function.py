
def ask_user_for_name_and_say_hello():
    """Prompts the user for name, and then
    prints hello to their name"""
    user_name = input("Please enter your name: ")
    print("Hello " + user_name + "!")

#Driver (where our code runs or executes)
if __name__ == "__main__":
    print('we are in the driver section')
    #how I call the function
    ask_user_for_name_and_say_hello()

    #This wont work it is undefined; can't be referenced outside the function code
    #print(user_name)

    print('our code is done')
