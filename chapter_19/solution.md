1. What is an RGBA value?
-> RGBA value stands for Red ,  Green , Blue and Alpha and is used to specify colors

2. How can you get the RGBA value of 'CornflowerBlue' from the Pillow module?
ImageColor.getcolor('CornflowerBlue', 'RGBA')

3. What is a box tuple?
A box tuple is a tuple value of four integers

4. What function returns an Image object for, say, an image file named zophie.png?
Image.open("zophie.png")

5. How can you find out the width and height of an Image object’s image?
img_object.size() will give the tuple that contains it's height and width

6. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?
imgobj.crop((0,50,50,50))

7. After making changes to an Image object, how could you save it as an image file?
imgobj.save('file_name.imageextension')

8. What module contains Pillow’s shape-drawing code?
ImageDraw

9. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?
ImageDraw objects have drawing methods