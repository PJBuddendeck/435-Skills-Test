import os
import shutil
from PIL import Image, ImageDraw

directPath = os.path.dirname(os.path.realpath(__file__))    # Find the path to this file (Python wasn't playing nice with relative paths) 

fileName = input("Please enter the file name as specified in the README: ") # Take a string input, concatenate for file path
filePath = directPath+"/Programming-Assignment-Data/"+fileName

try:
    file = open(filePath+".xml",'r')   # Open the file, read the lines
    text = file.readlines()

    shutil.copy(filePath+".png", directPath+"/Output/")   # Prepare a PNG copy for output modification
    copyPath = directPath+"/Output/"+fileName+".png"
    img = Image.open(copyPath)
    draw = ImageDraw.Draw(img)

    boundList = [] # List to store all boundary coordinates
    
    for line in text:   # Isolate node bounds, add to list
        copy = line.split('<')
        for i in copy:
            if "/>" in i and "bounds=" in i:
                boundList.append(i)

    for j in boundList: # For every coordinate, format for parsing
        j = j[j.find("bounds=")+7:]
        coord = j.split('][')
        
        coord[0] = coord[0][2:]
        coord[1] = coord[1][:coord[1].rfind(']')]
        
        coord[0] = coord[0].split(',')  # Turn coordinate points into 2D array for ease of access
        coord[1] = coord[1].split(',')

        draw.rectangle((float(coord[0][0]), float(coord[0][1]), float(coord[1][0]), float(coord[1][1])), fill=None, outline='yellow', width=10)
        img.save(copyPath) # Draw rectangles using the parsed coordinates, save the image

except:
    print("File could not be opened") # Error catching in case a file name is incorrectly inputted