1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.
assert spam >= 10, 'The spam variable is less than 10'

2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
assert eggs.lower() != bacon.lower(), 'The eggs and bacon variables are the same!' or assert eggs.upper() != bacon.upper(), 'The eggs and bacon variables are the same!'


3. Write an assert statement that always triggers an AssertionError.
asser False, 'Always triggers'

4. What are the two lines that your program must have in order to be able to call logging.debug()?
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -
%(levelname)s -  %(message)s')

5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?
import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG,
format=' %(asctime)s -  %(levelname)s -  %(message)s')

6. What are the five logging levels?
Debug, Info , Warning, Error , Critical

7. What line of code can you add to disable all logging messages in your program?
logging.disable(logging.CRITICAL)

8. Why is using logging messages better than using print() to display the same message?
Because when later after debugging we can use logging.disable() to disable all the logging messages at once instead of removing every single as same in print.

9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?
Step In == Execute Next Statement and the pause again
Step Over == Execute the Next Statement and if the next line is a function call than it just step over that function
Step Out == It will cause the debugger to run the statements in function at full speed until it returns

10. After you click Continue, when will the debugger stop?
When the program ends

11. What is a breakpoint?
Breakpoint is the point from where we want the debugger to start debugging

12. How do you set a breakpoint on a line of code in Mu?
Right-click line and Set Breakpoint