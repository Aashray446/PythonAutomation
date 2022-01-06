import os 
import re 
import pprint

print(os.getcwd())
os.chdir(os.getcwd() + '\PythonAutomation\chapter_9')

files = []
for file in os.listdir('.'):
    if file.endswith('.txt'):
        files.append(file)
user_reg = input("Enter what your are searching for ")
search_regex = re.compile(user_reg)

file_list = []
for filename in files:
    open_file = open(filename)
    read_file = open_file.read()
    if search_regex.search(read_file):
        file_list.append(filename)

pprint.pprint(file_list)