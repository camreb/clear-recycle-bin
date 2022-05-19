import os, time


class Cleaner:

    def __init__(self, disc):
        self.disc = disc
        self.path = os.path.join(self.disc, "\$RECYCLE.BIN")

#Function returns list with all files' paths to be deleted
    def pathing(self):
        files_to_delete = []

        for (root, dirs, files) in os.walk(self.path):
            for name in files:
                path = os.path.join(root, name)
                diff = time.time() - os.lstat(path).st_atime
                if diff > 1:
                    files_to_delete.append(path)
        return files_to_delete

#Function removes suitable files from Recycle Bin and creates raport.txt file.
    def remover(self, lista):
        if os.path.exists("raport.txt"):
            os.remove("raport.txt")
        for i in lista:
            os.remove(i)
            with open("raport.txt", "a+") as file:
                file.write("Usunieto {}\n".format(i))


