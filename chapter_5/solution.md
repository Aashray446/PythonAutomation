1. What does the code for an empty dictionary look like?
dict = {}
2. What does a dictionary value with a key 'foo' and a value 42 look like?
dict = {'foo' : 42}

3. What is the main difference between a dictionary and a list?
Dictionary can store in terms of Key ,value pair where key can be a string. Thus it is an unordered where list stores items in a order way where we can acess the data using the index of that value

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
We will get an error stating KeyError

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.

6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.

7. What is a shortcut for the following code?

if 'color' not in spam:
    spam['color'] = 'black'

=> spam.setdefault('color', 'black')

8. What module and function can be used to “pretty print” dictionary values?
We need to import pprint and then call a function name pprint()