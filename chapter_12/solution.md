1. Briefly describe the differences between the webbrowser, requests, bs4, and selenium modules.
Webbrowser is used to open a specific Url in web browser, requests is used to handle http requests , bs4 is a HTML parser and Selenium a module which can launch web browser and can control it same as a user does

2. What type of object is returned by requests.get()? How can you access the downloaded content as a string value?
It will return Response object
The response object has a text property that we can use

3. What requests method checks that the download worked?
raise_for_status() check wether there any error during download

4. How can you get the HTTP status code of a requests response?
Using status_code attribute

5. How do you save a requests response to a file?
After opening the new file on your computer in 'wb' “write binary” mode, use a for loop that iterates over the Response object’s iter_content() method to write out chunks to the file

6. What is the keyboard shortcut for opening a browser’s developer tools?
F12 in chrome

7. How can you view (in the developer tools) the HTML of a specific element on a web page?
Right click on that and select inspect

8. What is the CSS selector string that would find the element with an id attribute of main?
#main

9. What is the CSS selector string that would find the elements with a CSS class of highlight?
'.highlight'

10. What is the CSS selector string that would find all the <div> elements inside another <div> element?
'div div'

11. What is the CSS selector string that would find the <button> element with a value attribute set to favorite?
'button[value="favorite"]'

12. Say you have a Beautiful Soup Tag object stored in the variable spam for the element <div>Hello, world!</div>. How could you get a string 'Hello, world!' from the Tag object?
spam.getText()

13. How would you store all the attributes of a Beautiful Soup Tag object in a variable named linkElem?
linkElem.attrs

14. Running import selenium doesn’t work. How do you properly import the selenium module?
We use , from selenium import webdriver

15. What’s the difference between the find_element_* and find_elements_* methods?
find_element_* will find and return only one element where as find_elements_* returns a list of all matching elements

16. What methods do Selenium’s WebElement objects have for simulating mouse clicks and keyboard keys?
click() and send_keys() respectively

17. You could call send_keys(Keys.ENTER) on the Submit button’s WebElement object, but what is an easier way to submit a form with selenium?
We can call submit() instead

18. How can you simulate clicking a browser’s Forward, Back, and Refresh buttons with selenium?
using forward(), back() and refresh() methods