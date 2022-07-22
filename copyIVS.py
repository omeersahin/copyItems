import newshutil
import os
import tkinter as tk
from tkinter import filedialog




root = tk.Tk()
root.withdraw()

src_dir = filedialog.askdirectory()

dst_dir = filedialog.askdirectory()

#src_dir ="C:/Users/omer.sahin/Desktop/imageDataSet"
#dst_dir = "C:/Users/omer.sahin/Desktop/copyFolder"

newshutil.copytree(src_dir,dst_dir,dirs_exist_ok=True)
            

     



          