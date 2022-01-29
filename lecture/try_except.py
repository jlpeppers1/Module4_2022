x = 5
print('Hello world')
input_value = input('please enter a number: ')
try:
    as_int = int(input_value)
    if (as_int >= 0):
        print('input is good')
    else:
        raise ValueError('Bad Input')
except:
    print('You did not input a valid number')
finally:
    print('We are done with the try except')
print('This resumes the rest of the program')
print(str(x))
