1. What are the two values of the Boolean data type? How do you write them?
The two types of Boolean date type are True and False. We have to write it's first letter capital and then all other lowercase
2. What are the three Boolean operators?
NOT, OR, AND
3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

4. What do the following expressions evaluate to?
(5 > 4) and (3 == 5) --> False
not (5 > 4) --> False
(5 > 4) or (3 == 5) --> True
not ((5 > 4) or (3 == 5)) --> False
(True and True) and (True == False) --> False
(not False) or (not True) --> True

5. What are the six comparison operators?
<, >, ==, !=, <=, +>

6. What is the difference between the equal to operator and the assignment operator?
"==" operator do a comparison where are the "=" operator assigns values to the variables

7. Explain what a condition is and where you would use one.
When we need to compare any two values and return the boolean value then we use "==" where as when we need to store something in a variable we use "="

8. Identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')

9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')

10. What keys can you press if your program is stuck in an infinite loop?
We can press Ctrl + C

11. What is the difference between break and continue?
Break will move out of the current block of loop and continue keyword will move the execution to start of the loop

12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
range(10) means it will take numbers from 0 to 9, range(0,10) just specify the starting point 0 and does the same work as the range(10). Same goes for range(0,10,1), it just specifiy one the extra i.e increment by 1

13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
    FOR LOOP
for i in range(1, 11):
    print(i)
    WHILE LOOP
i = 1
while i <= 10:
    print(i)
    i = i + 1

14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
spam.bacon()