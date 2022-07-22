import newshutil_2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

src_dir = filedialog.askdirectory()

dst_dir = filedialog.askdirectory()

#src_dir ="C:/Users/omer.sahin/Desktop/srcFolder"
#dst_dir ="C:/Users/omer.sahin/Desktop/dstFolder"

newshutil_2.copytree(src_dir,dst_dir,dirs_exist_ok=True)
            

     



          