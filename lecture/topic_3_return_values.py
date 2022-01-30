def this_returns_nothing():
    """Don't forget a function docstring"""
    print('Nothing to return')

def get_user_age_in_5_years():
    """Don't forget a function docstring"""
    age = input("please enter your age: ")
    try:
        five_from_age = 5 + int(age)
    except:
        print('Bad Age')
        raise ValueError #I know this seems weird for now, will make custom exceptions later
    else:
        return "In 5 years you will be age " + str(five_from_age) + "."

if __name__ == "__main__":
    #this is none because the formula returned nothing
    returned_value = this_returns_nothing()
    print(type(returned_value))
    print(returned_value)

    age_in_5_years = get_user_age_in_5_years()
    print(age_in_5_years)
