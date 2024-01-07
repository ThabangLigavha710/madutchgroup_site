import os
from pathlib import Path

from madutchgroup_site.settings import BASE_DIR


path = os.chdir("media/cleaning_images")

i = 0

for file in os.listdir(path):
    new_file_name = "cleaning_image{}.jpg".format(i)
    os.rename(file, new_file_name)

    i = i + 1