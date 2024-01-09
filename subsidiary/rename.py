import os
from pathlib import Path
from uuid import uuid4

from madutchgroup_site import settings
import random


# def rename_file(file_path, file_name):

#     # path = os.path.join(settings.MEDIA_ROOT, file_path)
#     path = os.chdir(file_path)

#     filename = file_name

#     i = 1

#     for file in os.listdir(path):
#         new_file_name = filename + "_{}.jpg".format(i)
#         os.rename(file, new_file_name)

#         i = i + 1

#     return

def rename_file(path, image_name, number):

    def wrapper(instance, filename):
        
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = image_name + '_{}.{}'.format(number, ext)
        else:
            # set filename as random string
            id_list = [2, 3, 4, 5]
            instance.pk = random.choice(id_list)
            filename = '{}.{}'.format(instance.pk, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper
