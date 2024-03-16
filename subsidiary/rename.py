import os
from pathlib import Path
from uuid import uuid4

from madutchgroup_site import settings
import random



def rename_file(path, image_name, number):

    # wrapper_return = False
    wrapper_return = True

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
    
    # Return the function without "wrapper" when doing migrations
    if wrapper_return:
        return wrapper
    else:
        return
