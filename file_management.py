import os
import time

def month_to_hebrue(the_month):
    if the_month == "01":
        return "ינואר"
    elif the_month == "02":
        return "פברואר"
    elif the_month == "03":
        return "מרץ"
    elif the_month == "04":
        return "אפריל"
    elif the_month == "05":
        return "מאי"
    elif the_month == "06":
        return "יוני"
    elif the_month == "07":
        return "יולי"
    elif the_month == "08":
        return "אוגוסט"
    elif the_month == "09":
        return "ספטמבר"
    elif the_month == "10":
        return "אוקטובר"
    elif the_month == "11":
        return "נובמבר"
    elif the_month == "12":
        return "דצמבר"



get_imges_from = str(input("input a folder with imges: "))
organized_img = "/Users/lenovo/Pictures/תמונות לפי שנים וחודשים"
videos_path = r"C:\Users\lenovo\Pictures\סרטונים מכל השנים"

list_of_files = os.scandir(get_imges_from)
list_of_imges = []
list_of_folders = []

start_time = time.perf_counter()

for file in list_of_files:
    if file.name.endswith(".jpg") or file.name.endswith(".png") or file.name.endswith(".jpeg"):
        list_of_imges.append(file)
    elif file.name.endswith(".mp4"):
        if not os.path.exists(videos_path):
            os.mkdir(videos_path)
        destination_videos = os.path.join(videos_path, file.name)
        os.replace(file.path , destination_videos)



for file in list_of_imges:

    name = file.name

    if not name[0].isdigit():
        year = name[4:8]
        month = name[8:10]
    else:
        year = name[0:4]
        month = name[4:6]

    month = month_to_hebrue(month)

    check_file_year = os.path.join(organized_img, year)
    check_file_month = os.path.join(check_file_year, month)

    if not os.path.exists(check_file_year):
        os.mkdir(check_file_year)
    if not os.path.exists(check_file_month):
        os.mkdir(check_file_month)

    destination = os.path.join(check_file_month, file.name)
    os.replace(file.path, destination)

print("הסתיים הכל עבר בהצלחה")

end_time = time.perf_counter()

print(str(end_time - start_time) + "sec")