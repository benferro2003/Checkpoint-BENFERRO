#!/usr/bin/env python3
def password_checker(password):
    from string import ascii_letters as letters, digits, punctuation

    has_letter = has_digit = has_punc = False

    for character in password:
        if character in letters:
            has_letter = True
        elif character in digits:
            has_digit = True
        elif character in punctuation:
            has_punc = True

    if has_letter == True and has_digit == True and has_punc == True:
        print("The password is acceptable")
    else:
        print('The password is unacceptable')


if __name__ == '__main__':
    print('Checkpoint task 4 - BEN FERRO')
    password_checker('Ben0!')
    password_checker('password')
