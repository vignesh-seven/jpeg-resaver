if __name__ == "__main__":
    from tkinter import *
    from TkinterDnD2 import *
    import jpegResaver

    window_width = 600
    window_height = 500

    # triggered on drag n drop
    def convert(event):
        if event.data.endswith(".jpeg") or event.data.endswith(".jpg"):
            print("the file is valid!\n" + event.data + "\n Sending data to resaver")
            files = ws.tk.splitlist(event.data)
            for filename in files:
                print(filename)
                jpegResaver.main(filename)
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
    area.dnd_bind('<<Drop>>', convert)


    ws.mainloop()

