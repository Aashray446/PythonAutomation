import re
import pyperclip
# Strong Password Regexes

pass_length_regex = re.compile(r'.{8,}')      
pass_upper_regex = re.compile(r'[A-Z]')      
pass_lower_regex = re.compile(r'[a-z]')      
pass_digit_regex = re.compile(r'[0-9]')      

def pass_strength_checker(text):
    """Check if a password is strong."""
    if pass_length_regex.search(text) is None:
        return False
    if pass_upper_regex.search(text) is None:
        return False
    if pass_lower_regex.search(text) is None:
        return False
    if pass_digit_regex.search(text) is None:
        return False
    else:
        return True


password = str(pyperclip.paste())


if pass_strength_checker(password) is True:
    print('That\'s a strong password. Remember to use it for one site only.')
else:
    print('That\'s a weak password. I wouldn\'t recommend using it')