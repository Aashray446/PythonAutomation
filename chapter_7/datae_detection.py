import re

def detect_date():
    date_pattern  = re.compile(r'(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/([1-9][0-9]{3})')
    a = date_pattern.findall("Tge word is 01/12/2005 ")
    print(a)
detect_date()