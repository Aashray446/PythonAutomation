import re

def detect_date():
    date_pattern  = re.compile(r'[0-2]\d]|(31)\/\d{2}\/\d{4}')
    a = date_pattern.findall("Tge word is 01/12/2005 ")
    print(a)
detect_date()