def convert(img_input):
    # for img_input in img_inputs:
    # Read image
    im = Image.open( img_input ).convert("RGBA")

    just_filename = os.path.splitext(os.path.basename(img_input))[0]
           
    # make a new background
    background = Image.new("RGBA", im.size, (255,255,255))

    # composite the image on the background
    alpha_composite = Image.alpha_composite(background, im)

    # convert the image back to RGB
    final_image = alpha_composite.convert("RGB")

    # save the composite as a jpg
    final_image.save(os.path.abspath(os.path.join(new_dirname, just_filename) + "_resaved.jpg"), "JPEG")
    print("saved: " + os.path.abspath(os.path.join(new_dirname, just_filename) + "_resaved.jpg"))

def change_info_text():
    #threading.Timer(3.0, change_info_text)
    time.sleep(3)
    info_text = "Drag files here"
    area.itemconfig(text_on_canvas, text=info_text)

    
# triggered on drag n drop
def start(event):   
    files = ws.tk.splitlist(event.data)
    # print(files)
    # some path variables related to the image (for future features)    
    dirname = os.path.dirname(files[0])

    basename = os.path.basename(files[0])

    global just_filename
       
    just_dirname = os.path.basename(dirname)

    global new_dirname
    new_dirname = dirname

    
    

    if (makeAFolder.get() == 1):
        full_new_dirname = os.path.join(dirname, just_dirname + "_resaved")
        os.mkdir(os.path.abspath(full_new_dirname))
        # print("make folder is CHECKED\n" + full_new_dirname)
        new_dirname = os.path.abspath(full_new_dirname)

    for filename in files:
        kind = filetype.guess(filename)
        #print(kind.mime)
        if kind.mime == "image/jpeg":
        #if filename.endswith(".jpeg") or filename.endswith(".jpg"):
            print("The file is valid!")
            convert(filename)
            if (deleteInputImages.get() == 1):
                os.remove(filename)
        else:
            print("INVALID FILE TYPE: " + kind.mime)
            info_text = "Invalid File Type!"
            area.itemconfig(text_on_canvas, text=info_text)
            change_info_text()
            
            
        #print("The file path: " + filename)

    print("All Done!")
        
if __name__ == "__main__":
    from tkinter import *
    from tkinter.tix import *
    from TkinterDnD2 import *
    import sys
    import os
    import time
    import threading
    from PIL import Image, ImageFilter
    import filetype
    
    global window_width
    global window_height
    window_width = 400
    window_height = 350

    # Window config
    ws = TkinterDnD.Tk()
    ws.title("JPEG Resaver")
    ws.geometry(str(window_width) + "x" + str(window_height) + "+500+50")
    # ws.pack()
    ws.resizable(True, False)
    
    frameForDrag = Frame(ws)
    frameForDrag.pack()

    frameForOptions = Frame(ws, height=window_height*0.15, bg = "green")
    frameForOptions.pack(side=tkinter.BOTTOM, fill=tkinter.Y)

    # Drop area config
    global info_text
    info_text = "Drag files here"
    
    area = Canvas(frameForDrag,
                  width=window_width,
                  height=window_height*0.85,
                  bg="#cccccc")
    text_on_canvas = area.create_text(window_width / 2,
                     window_height / 2,
                     fill="#303030",
                     font="Arial 18 italic", text=info_text)
    area.pack(side=LEFT)
    area.drop_target_register(DND_FILES)
    area.dnd_bind('<<Drop>>', start)
    area.pack()

    #area.itemconfig(text_on_canvas, text=status_text)

    global makeAFolder
    makeAFolder = IntVar() 
    FolderCheckBox = Checkbutton(frameForOptions, text = "Make a folder", 
                          variable = makeAFolder,
                          #height = int(window_height*0.15),
                          width = 25,

                          #expand=True
                                 )
    FolderCheckBox.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False)

    global deleteInputImages
    deleteInputImages = IntVar() 
    DeleteSourceCheckBox = Checkbutton(frameForOptions, text = "Delete input files", 
                          variable = deleteInputImages,
                          height = int(window_height*0.1),
                          width = 25,
                          #bg = "blue"
                          #expand=True
                                 )
    DeleteSourceCheckBox.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False)

    
    ws.mainloop()







    # the jpeg converter function
    
    



    

        
    
  
