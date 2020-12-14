# python script to resize images
# overwrites all the images in the same

from PIL import Image
import os
import sys

# set path to directory here
directory = "Path"

for file_name in os.listdir(directory):
    print("Processing %s" % file_name)
    try:
        image = Image.open(os.path.join(directory, file_name))

        x,y = image.size
        new_dimensions = (250, 250)
        output = image.resize(new_dimensions, Image.ANTIALIAS)

        output_file_name = os.path.join(directory, file_name)
        output.save(output_file_name, "JPEG", quality = 95)
    except:
        print(file_name + "image could not be resized")

print("All done")
