#!/usr/bin/python3
# date		    2023-03-09
# author	    Alexander Mueller
# email		    amueller@doctorcrank.de
# version	    1.0
# description	Testing graphical stuff with python
# YT video:     https://www.youtube.com/watch?v=jE-SpRI3K5g

import tkinter as tk
from tkinter import filedialog, Text, messagebox
import os

def create_app_list():
    global path_file_apps
    path_file = filedialog.askopenfilename(initialdir="/", title="Select File",
                                           filetypes=(
                                               ("Executable", "*.exe"),
                                               ("All Files", "*")
                                               )
                                           )
    if path_file in path_file_apps:
        messagebox.showerror("Warning!", "Path already added!")
    else:
        path_file_apps.append(path_file)

    list_apps(path_file_apps)

def create_window_main() -> tk.Tk:
    global bg_box
    window_root = tk.Tk()
    window_root.geometry("1920x1080")
    window_root.resizable(False, False)
    window_root.title("graphicalTest.py")

    #canvas = tk.Canvas(window_root, height=1080, width=1920, bg="#255255")
    #canvas.pack()

    bg_box = tk.Frame(window_root, bg="#FFFFFF")
    bg_box.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    button_openFile = tk.Button(
        window_root,
        text="Open file",
        #padx=10,
        #pady=5,
        #fg="#FFFFFF",
        #bg="#666666",
        command=create_app_list
        )
    button_openFile.pack()

    button_runApps = tk.Button(window_root, text="Run Apps", padx=10, pady=5, fg="#FFF000", bg="#666000", command=execute_app)
    button_runApps.pack()

    window_root.mainloop()

def execute_app():
    for app in path_file_apps:
        print("Executed " + app + ", trust me!")

def list_apps(path_file_apps: list):
    global bg_box
    for app in path_file_apps:
        list_app_paths = tk.Label(bg_box, text=app)
    list_app_paths.pack()

def create_window_warn(message: str):
    window_warn = tk.Tk()
    window_warn.geometry("200x100")
    window_warn.resizable(False,False)
    window_warn.title("Warning!")

    textBox = Text(window_warn, )


if __name__ == '__main__':
    path_file_apps = list()
    window_main = create_window_main()
