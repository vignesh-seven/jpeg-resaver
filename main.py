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
    # print("saved: " + os.path.abspath(os.path.join(new_dirname, just_filename) + "_resaved.jpg"))


if __name__ == "__main__":
    from tkinter import *
    from tkinter.tix import *
    from TkinterDnD2 import *
    import sys
    import os
    import time
    from PIL import Image, ImageFilter
    
    global window_width
    global window_height
    window_width = 400
    window_height = 350
    
    
    # the jpeg converter function
    


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
            # print("Processing: " + filename)
            if filename.endswith(".jpeg") or filename.endswith(".jpg"):
                print("The file is valid!")
                convert(filename)
            print("The file path: " + filename)
        print("All Done!")

        
    # Window config
    ws = TkinterDnD.Tk()
    ws.title("JPEG Resaver")
    ws.geometry(str(window_width) + "x" + str(window_height) + "+500+50")
    # ws.pack()
    
    frameForDrag = Frame(ws)
    frameForDrag.pack()

    frameForOptions = Frame(ws)
    frameForOptions.pack()

    # Drop area config
    area = Canvas(frameForDrag,
                  width=window_width,
                  height=window_height*0.85,
                  bg="#cccccc")
    area.create_text(window_width / 2,
                     window_height / 2,
                     fill="#303030",
                     font="Arial 18 italic", text="Drag files here")
    area.pack(side=LEFT)
    area.drop_target_register(DND_FILES)
    area.dnd_bind('<<Drop>>', start)
    area.pack()

    global makeAFolder
    makeAFolder = IntVar() 
    FolderCheckBox = Checkbutton(frameForOptions, text = "Make a folder", 
                          variable = makeAFolder,
                          height = int(window_height*0.15),
                          width = window_width)
    FolderCheckBox.pack()

    
    ws.mainloop()

  
