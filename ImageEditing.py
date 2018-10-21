#! /usr/bin/python
from PIL import Image
import os

# Ask the user for the image and store it
image_file = raw_input("Enter the file name: ")
type(image_file)

#Open the file
try:
	photo = Image.open(image_file)
	# get the size of the original image
	width,height = photo.size

	# Choose the lessser of two as the dimension for width and height
	x = height if height > width else width
	y = height if height > width else width

	# best down-sizing filter
	square_image = photo.resize((x,y), Image.ANTIALIAS)

	# Get the File Name and Extension And add _Squared to the name and save it
	name, ext = os.path.splitext(image_file)
	newfilename = name+"_squared"+ext
	square_image.save(newfilename)

	#Notifies that the file has been resized
	print("The file has been saved as: %s" % newfilename)

except Exception as e:
	print(str(e))

