import os
import time

path = "C:/Users/tibbu/Documents/Agendas"
now = time.time()
dirs = os.listdir(path)
for filename in os.listdir(path):
    # if os.stat(os.path.join(path, filename)).st_mtime < now - 7 * 86400:
    if os.path.getmtime(os.path.join(path, filename)) < now - 2 * 86400:
        if os.path.isfile(os.path.join(path, filename)):
            print(filename)
            os.remove(os.path.join(path, filename))

