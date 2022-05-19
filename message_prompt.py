from tkinter import messagebox
from os.path import getsize


class MessageBox:

    def __init__(self, deleted_files: list):
        self.deleted_files = deleted_files

    def popup(self):
        size = 0
        for file in self.deleted_files:
            size = size + getsize(file)

        messagebox.showinfo("Recycle Bin Cleaner",
                            "{} files have been deleted from Recycle Bin\n"
                            "with a total size of {} KB"
                            .format(len(self.deleted_files), int(size/1000)))
