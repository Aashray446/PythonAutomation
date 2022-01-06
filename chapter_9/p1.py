import os
import re

print(os.getcwd())
os.chdir(os.getcwd() + '\PythonAutomation\chapter_9')

text = open('book.txt', 'r')
get_text = text.read()
print(get_text)

adjective_regex = re.compile('ADJECTIVE')
noun_regex = re.compile('NOUN')
adverb_regex = re.compile('ADVERB')
verb_regex = re.compile('VERB')

while (adjective_regex.search(get_text) != None):
    adj = input("Enter the adjecitve ")
    get_text = adjective_regex.sub(adj, get_text, 1)
while (noun_regex.search(get_text) != None):
    noun = input("Enter the noun ")
    get_text = noun_regex.sub(noun, get_text, 1)
while (adverb_regex.search(get_text) != None):
    adverb = input("Enter the adverb ")
    get_text = adverb_regex.sub(adverb, get_text, 1)
while (verb_regex.search(get_text) != None):
    verb = input("Enter the verb ")
    get_text = verb_regex.sub(verb, get_text, 1)
text.close()
text = open('book.txt', 'w')
text.write(get_text)
text.close()