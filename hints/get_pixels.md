finding jpgs
============

a simple way to check whether a file is a jpg is using endswith

  "picture.jpg".endswith(".jpg")  # True
  "picture.png".endswith(".jpg")  # False
  
modifying images (lists of lists)
=================================

in this function you need to take an image represented as a list of lists
and modify every element.  one way to do it is one row at a time:

    output = []
    for row in image:
        # create a modified version of the row
        new_row = [modified(element) for element in row]
        # and append it to the output
        output.append(new_row)
        
A slicker way to do it is with nested list comprehensions:

    output = [[modified(element) for element in row]
              for row in image]
