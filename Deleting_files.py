import os
import time

path = "/Users/sameer/Downloads/Landchecks/Delete"
now = time.time()
dirs = os.listdir(path)
for filename in os.listdir(path):
    # use os.path.join, to join the folder name with filename
    if os.path.getmtime(os.path.join(path, filename)) < now - 7 * 86400:
        if os.path.isfile(os.path.join(path, filename)):
            print(filename)
            os.remove(os.path.join(path, filename))
