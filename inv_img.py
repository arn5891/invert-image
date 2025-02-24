import cv2
import re
import os

def brt(p):  #returns whether rgb is closer to black or white
  avg = 0.299 * p[2] + 0.587 * p[1] + 0.114 * p[0]#everything will be in GBR format
  return avg

def invert(img):
    img = re.split('\"(.*?)\"', img)[1]
    img = cv2.imread(img)
    for scnln in img:
        for pix in range(len(scnln)):
            scnln[pix]= [255-scnln[pix][0],255-scnln[pix][1],255-scnln[pix][2]]
    filename = input("please name your file, make sure to specify file type:")
    cv2.imwrite(filename, img)
    
filepath = input("enter a filepath: ")
directory = r"C:\Users\gohal\OneDrive\Documents\Aaron Digital Learning\2021-2022 year\Semester 2\Art\Aaron's Game Sprites\mario game\test"
os.chdir(directory)
print(f"file will be saved in {directory}")
print("Loading...")
invert(filepath)