<p align="center">
  <img src="https://user-images.githubusercontent.com/59286418/127771463-83c7e022-107d-402f-9a1b-d75d20b57995.png" />
</p>

# JPEG Resaver  
*A little program to save you from "JPEG marker is missing" hell (for images downloaded from Whatsapp)*  

A tool to re-encode JPEG/JPG files to JPG.  

## How to use  
Just drag the images you want to convert to .jpg  

## Features  
 - Can output files to a new folder.
 - Works with TIFF/PNG/JPG files (Flattens the image in case of TIFF).
 - Can delete input images after converting.

## Why is this?
There are already a lot of ways to solve this issue, so why did I make this?  

Because the other methods take a lot of time and effort for what they do, and involve moving all image files to a seperate folder and/or collecting output images from another folder. But it's way too much work if you want to use it for a few images frequently (like >5 images each time more than 5 times a day). 

This program allows you to quickly drag & drop your images and it handles the rest.
And it has a GUI (cool, i guess).  

## A few things to note...
If you want to mess with it:  
```  
This program is written in Python 3.9.6 (32-bit)  
```
### Dependencies:  
```  
pip install -r requirements.txt
```  
This will install the following Python Modules  
 - Pillow  
 - Tkinter  
 - TkinterDnD2
 - filetype
