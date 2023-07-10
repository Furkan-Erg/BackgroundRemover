import webbrowser
from tkinter import filedialog, Label

from PIL import Image as PILImage, ImageTk
from rembg import remove
from tkinter import *

root = Tk()
input_path = 'assets/placeholder.png'
image = ImageTk.PhotoImage(file=input_path)
image_label: Label = Label(root, image=image)


def choose_file():
    global input_path
    input_path = filedialog.askopenfilename(initialdir="/>", title="Select a File",
                                            filetypes=(("all files", "*.*"),))
    global image
    image = ImageTk.PhotoImage(file=input_path)
    image_label.configure(image=image)


def remove_background():
    input_image = PILImage.open(input_path)
    output_path = filedialog.asksaveasfilename(initialdir="/>", title="Choose a Destination",
                                               filetypes=(("png files", "*.png"),))

    output = remove(input_image)
    output.save(fp=output_path + '.png')


def open_easter_egg_dialog():
    new_window = Toplevel(root)
    new_window.title("Congratulations! You found easter egg!")
    new_window.iconbitmap('assets/favicon.ico')

    text = Label(new_window, text="This app made by Furkan Ergüldürenler")
    text.config(width=50, height=50, )
    text.pack()

    text_info = Label(new_window, text="Do not google 'broke my back mean in slang '")
    text_info.config(width=55, height=55, font=("Courier", 20), fg="red")
    text_info.pack()

    new_window.geometry("600x400")
    new_window.mainloop()


def init_gui():
    root.title("Broke my Back")
    root.iconbitmap('assets/favicon.ico')

    root.geometry("600x400")

    choose_image_button = Button(root, text="Choose Image", command=choose_file)
    button = Button(root, text="Remove Background", command=remove_background)

    choose_image_button.grid(row=0, column=0, sticky="nsew", pady=10)
    button.grid(row=0, column=1, sticky="nsew", pady=10)
    image_label.grid(row=1, column=0, columnspan=2, sticky="nsew")

    menu = Menu(root)
    root.config(menu=menu)
    menu.add_command(label="Linkedin",
                     command=(lambda: webbrowser.open_new("https://www.linkedin.com/in/furkanerguldurenler")))
    menu.add_command(label="GitHub", command=(lambda: webbrowser.open_new("https://github.com/Furkan-Erg")))
    menu.add_command(label="Web Page", command=(lambda: webbrowser.open_new("https://www.furkanerg.me")))
    menu.add_command(label=" ", command=open_easter_egg_dialog)

    root.mainloop()


init_gui()

