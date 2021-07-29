if __name__ == "__main__":
    from tkinter import *
    from TkinterDnD2 import *
    import sys
    import os
    from PIL import Image, ImageFilter
    
    window_width = 600
    window_height = 500
    
    # the jpeg converter function
    def convert(img_input):
        #for img_input in img_inputs:
            # Read image
            im = Image.open( img_input ).convert("RGBA")
              
            # some path variables related to the image (for future features)            
            dirname = os.path.dirname(img_input)
            
            basename = os.path.basename(img_input)

            just_filename = os.path.splitext(basename)[0]
            
            file_ext = os.path.splitext(basename)[1]

            new_dirname = dirname
            
            # make a new background
            background = Image.new("RGBA", im.size, (255,255,255))

            # composite the image on the background
            alpha_composite = Image.alpha_composite(background, im)

            # convert the image back to RGB
            final_image = alpha_composite.convert("RGB")

            # save the composite as a jpg
            final_image.save(os.path.abspath(os.path.join(new_dirname, just_filename) + "_resaved" + file_ext), "JPEG")



    # triggered on drag n drop
    def start(event):
        if event.data.endswith(".jpeg") or event.data.endswith(".jpg"):
            print("the file is valid!\n" + event.data + "\n Sending data to resaver")
            files = ws.tk.splitlist(event.data)
            for filename in files:
                print("Processing: " + filename)
                convert(filename)
                print("Saved " + filename)
            print("All Done!")
        else:
            print("the file is INVALID")

    # Window config
    ws = TkinterDnD.Tk()
    ws.title('JPEG Resaver')
    ws.geometry(str(window_width) + "x" + str(window_height) + "+500+50")

    frame = Frame(ws)
    frame.pack()

    # Canvas config
    area = Canvas(frame, width=window_width, height=window_height)
    area.pack(side=LEFT)
    area.drop_target_register(DND_FILES)
    area.dnd_bind('<<Drop>>', start)


    ws.mainloop()

  
