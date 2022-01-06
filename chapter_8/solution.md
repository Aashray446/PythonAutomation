1. Does PyInputPlus come with the Python Standard Library?
No, it is a third-party module


2. Why is PyInputPlus commonly imported with import pyinputplus as pyip?
so that it can be called as pyip which makes it sorter than pyinputplus

3. What is the difference between inputInt() and inputFloat()?
inputInt() returns int and where as inputFloat returns float value

4. How can you ensure that the user enters a whole number between 0 and 99 using PyInputPlus?
By supllying two more optional parameters i.e min and max

5. What is passed to the allowRegexes and blockRegexes keyword arguments?
A list of regex strings

6. What does inputStr(limit=3) do if blank input is entered three times?
will raise RetryLimitException

7. What does inputStr(limit=3, default='hello') do if blank input is entered three times?
It will take return the default value i.e hello