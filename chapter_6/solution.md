1. What are escape characters?

Escapre characters are special characters or spaces that can't be type directly in the "" or ''


2. What do the \n and \t escape characters represent?

\n represent new line and \t represent tab space

3. How can you put a \ backslash character in a string?

\\

4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?

=>Because " ", i.e double quote is used 

5. If you don’t want to put \n in your string, how can you write a string with newlines in it?

=>Using Multline strings


6. What do the following expressions evaluate to?
'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]

"e"
"Hello"
"Hello"
"lo, world!"

7. What do the following expressions evaluate to?

'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()

"HELLO"
True
"hello"

8. What do the following expressions evaluate to?

'Remember, remember, the fifth of November.'.split()
'-'.join('There can be only one.'.split())

['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']
"There-can-be-only-one."

9. What string methods can you use to right-justify, left-justify, and center a string?

=>rjust(), ljust(), center()

10. How can you trim whitespace characters from the beginning or end of a string?
lstrip() and rstrip()