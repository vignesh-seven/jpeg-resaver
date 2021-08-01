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
    info_text = "Drag files here"
    drag_area.configure(text=info_text, fg="black")

    
# triggered on drag n drop
def start(event):   
    files = root.tk.splitlist(event.data)
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
    index = 0
    for filename in files:
        kind = filetype.guess(filename)
        print(kind.mime)
        if kind.mime == "image/jpeg" or "image/png" or "image/tiff":
            drag_area.configure(text=f"Processing\n{index + 1} of {len(files)}", fg="blue")
        #if filename.endswith(".jpeg") or filename.endswith(".jpg"):
            print("The file is valid!")
            convert(filename)
            if (deleteInputImages.get() == 1):
                os.remove(filename)
            drag_area.after(500, change_info_text)
        else:
            print("INVALID FILE TYPE: " + kind.mime)
            info_text = "File not valid!"
            drag_area.configure(text=info_text, fg="red")
            drag_area.after(3000, change_info_text)
        index += 1
            
            
        #print("The file path: " + filename)

    print("All Done!")
    #change_text_info()
        
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
    root = TkinterDnD.Tk()
    root.title("JPEG Resaver")
    #setting window size
    width=400
    height=350
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    #root.resizable(width=False, height=False)
    root.rowconfigure(0, weight=10)
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    
    #frameForDrag = Frame(root, width=window_width, height=window_height*0.85)
    #frameForDrag.pack()

    #frameForOptions = Frame(root, height=window_height*0.15, bg = "green")
    #frameForOptions.pack(side=tkinter.BOTTOM, fill=tkinter.Y)

    # Drop drag_area config
    global info_text
    info_text = "Drag files here"
    
    drag_area = Label(root,
                  text = info_text,
                  font = "Arial 18 italic",
                  justify="center",
                  bg="#cccccc")
    #text_on_canvas = drag_area.create_text(window_width / 2,
    #                 window_height / 2,
    #                 fill="#303030",
    #                 font="Arial 18 italic", text=info_text)
    drag_area.pack(side=LEFT)
    drag_area.drop_target_register(DND_FILES)
    drag_area.dnd_bind('<<Drop>>', start)
    #drag_area.pack(fill=BOTH, expand=True)
    drag_area.grid(column=0, row=0, columnspan=2, rowspan=1, sticky="EWNS")
    
    
    #drag_area.itemconfig(text_on_canvas, text=status_text)

    global makeAFolder
    makeAFolder = IntVar() 
    FolderCheckBox = Checkbutton(root, text = "Make a folder", 
                          variable = makeAFolder,
                          #bg = "red",
                          justify="center",
                          )
    FolderCheckBox.grid(column=0, row=1, columnspan=1, rowspan=1, sticky="EWNS")

    global deleteInputImages
    deleteInputImages = IntVar() 
    DeleteSourceCheckBox = Checkbutton(root, text = "Delete input files", 
                          variable = deleteInputImages,
                          #bg = "blue",
                          justify="center"
                          )
    DeleteSourceCheckBox.grid(column=1, row=1, columnspan=1, rowspan=1, sticky="EWNS")

    
    root.mainloop()







    # the jpeg converter function
    
    



    

        
    
  
