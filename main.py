# the jpeg converter function
def convert(img_input):
    im = Image.open( img_input ).convert("RGBA")

    just_filename = os.path.splitext(os.path.basename(img_input))[0]
           
    background = Image.new("RGBA", im.size, (255,255,255))

    alpha_composite = Image.alpha_composite(background, im)

    final_image = alpha_composite.convert("RGB")

    # save the image as a jpg
    final_image.save(os.path.abspath(os.path.join(new_dirname, just_filename) + "_resaved.jpg"), "JPEG")
    print("saved: " + os.path.abspath(os.path.join(new_dirname, just_filename) + "_resaved.jpg"))

def change_info_text():
    info_text = "Drag files here"
    drag_area.configure(text=info_text, fg="black")

def show_error():
    print("INVALID FILE TYPE")# + kind.mime)
    info_text = "File not valid!"
    drag_area.configure(text=info_text, fg="red")
    drag_area.after(3000, change_info_text)
    
# triggered on drag n drop
def start(event):   
    files = root.tk.splitlist(event.data)

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
        #print(kind.mime)
        #print(type(kind))
        if kind == None:
            show_error()
            continue
        elif kind.mime=="image/jpeg" or kind.mime=="image/png" or kind.mime=="image/tiff":
            drag_area.configure(text=f"Processing\n{index + 1} of {len(files)}", fg="blue")
            print("The file is valid!")
            convert(filename)
            if (deleteInputImages.get() == 1):
                os.remove(filename)
            drag_area.after(500, change_info_text)
        else:
            show_error()
            
        index += 1
        #print("The file path: " + filename)

    #print("All Done!")
        
if __name__ == "__main__":
    from tkinter import *
    from tkinter.tix import *
    from TkinterDnD2 import *
    import os
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
    
    # Drop drag_area config
    global info_text
    info_text = "Drag files here"
    
    drag_area = Label(root,
                  text = info_text,
                  font = "Arial 18 italic",
                  justify="center",
                  bg="#cccccc")
    
    drag_area.pack(side=LEFT)
    drag_area.drop_target_register(DND_FILES)
    drag_area.dnd_bind('<<Drop>>', start)
    drag_area.grid(column=0, row=0, columnspan=2, rowspan=1, sticky="EWNS")
    
    # make a folder button
    global makeAFolder
    makeAFolder = IntVar() 
    FolderCheckBox = Checkbutton(root, text = "Make a folder", 
                          variable = makeAFolder,
                          #bg = "red",
                          justify="center",
                          )
    FolderCheckBox.grid(column=0, row=1, columnspan=1, rowspan=1, sticky="EWNS")

    #delete input files button
    global deleteInputImages
    deleteInputImages = IntVar() 
    DeleteSourceCheckBox = Checkbutton(root, text = "Delete input files", 
                          variable = deleteInputImages,
                          #bg = "blue",
                          justify="center"
                          )
    DeleteSourceCheckBox.grid(column=1, row=1, columnspan=1, rowspan=1, sticky="EWNS")

    root.mainloop()

