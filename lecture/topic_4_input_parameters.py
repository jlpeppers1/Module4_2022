def get_user_age_in_5_years(age_in_function):
    """Don't forget a function docstring"""
    try:
        five_from_age = 5 + int(age_in_function)
        return five_from_age
    except:
        print('Bad Age!')
        raise ValueError #I know this seems weird for now, will make custom exceptions later

def print_name(first_name, middle_name,last_name):
    """Don't forget a function docstring"""
    print(first_name)
    print(middle_name)
    print(last_name)


#driver
if __name__ == "__main__":
    age_in_driver = input("please enter your age: ")
    age_in_5_years = get_user_age_in_5_years(age_in_driver)
    print('Age in 5 years is: ' + str(age_in_5_years))
    print('Drive age is unchanged: ' + age_in_driver)

    print_name('John', 'Jason', 'Smith')
    print_name(middle_name='Jason', last_name='Smith',first_name='John')
