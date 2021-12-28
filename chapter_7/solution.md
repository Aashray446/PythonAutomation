1. What is the function that creates Regex objects?
re.compile()

2. Why are raw strings often used when creating Regex objects?
because raw strings treat 'blackslash' as a literal character and not as a escape character


3. What does the search() method return?
The search() method will return the first part of string that is matched with that pattern in the form of Match object

4. How do you get the actual strings that match the pattern from a Match object?
.group() method

5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?
Group 0 is the entire match, group 1 covers the first set of parentheses, and group 2 covers the second set of parentheses

6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?
=> They can be escaped with a backslash , i.e : \. , \( , \) 

7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?
=>If the string has no groups then a list of strings is returned else if the string has groups then a list of tuples of strings will be returned

8. What does the | character signify in regular expressions?
=>

9. What two things does the ? character signify in regular expressions?
=>

10. What is the difference between the + and * characters in regular expressions?
=>

11. What is the difference between {3} and {3,5} in regular expressions?
=>

12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?
=>

13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?
=>

14. What is the difference between .* and .*??
=>

15. What is the character class syntax to match all numbers and lowercase letters?
=>

16. How do you make a regular expression case-insensitive?
=>

17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?
=>
18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?
=>
19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?
=>

20. How would you write a regex that matches a number with commas for every three digits? It must match the following:

'42'
'1,234'
'6,368,745'
but not the following:

'12,34,567' (which has only two digits between the commas)
'1234' (which lacks commas)
=>
21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:

'Haruto Watanabe'
'Alice Watanabe'
'RoboCop Watanabe'
but not the following:

'haruto Watanabe' (where the first name is not capitalized)
'Mr. Watanabe' (where the preceding word has a nonletter character)
'Watanabe' (which has no first name)
'Haruto watanabe' (where Watanabe is not capitalized)
=>
22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:

'Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'
but not the following:

'RoboCop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.'

=>