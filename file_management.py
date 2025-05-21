import os
import time

sprs = "/Users/lenovo/Pictures/Saved Pictures"

list_of_files = os.scandir(sprs)
list_of_imges = []

for file in list_of_files:
    if ".jpg" in str(file) or ".png" in str(file):
        list_of_imges.append(file)


for file in list_of_imges :
    creation_time = os.path.getctime(file)
    readable_time = time.ctime(creation_time)

    month = str(readable_time[4]) + str(readable_time[5]) + str(readable_time[6])
    year = str(readable_time[-4]) + str(readable_time[-3]) + str(readable_time[-2]) + str(readable_time[-1])



