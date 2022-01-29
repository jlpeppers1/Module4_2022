def ask_user_for_name_and_age_then_say_hello():
    """Prompts the user for name and age; then
    prints hello to their name"""
    user_name = input("Please enter your name: ")
    print("Hello " + user_name + "!")
    user_age = input("Please enter your age: ")
    try:
        age_in_5_years = int(user_age) + 5
        if (age_in_5_years < 5  or age_in_5_years > 120):
            raise ValueError
    except ValueError:
        print("You did not enter a proper age!")
    else:
        print('In 5 years you will be age: ' + str(age_in_5_years))

#Driver (where our code runs or executes)
if __name__ == "__main__":
    ask_user_for_name_and_age_then_say_hello()
