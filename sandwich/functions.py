import os
import random
import string
import sys
import uuid
from io import BytesIO

from PIL import Image
from ckeditor.fields import RichTextField
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.html import format_html
from django_resized import ResizedImageField
from pytils.translit import slugify


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    if ext == 'png' or ext == 'jpg' or ext == 'jpeg' or ext == 'svg':
        dir = 'images/'
    else:
        dir = 'files/'
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(dir, filename)


def resize_img(f1, f2, fs):
    f1 = f2
    image1 = f1
    img1 = Image.open(image1)
    new_img1 = img1.convert('RGB')
    ratio_current = new_img1.size[1] / new_img1.size[0]
    ratio_new = fs[1] / fs[0]
    if ratio_current <= ratio_new:
        new_width = (fs[1] * new_img1.size[0]) / new_img1.size[1]
        new_height = fs[1]
        resized_new_img1 = new_img1.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        box = ((resized_new_img1.size[0] - fs[0]) / 2, 0, resized_new_img1.size[0] - (resized_new_img1.size[0] - fs[0]) / 2, resized_new_img1.size[1])
        resized_new_img1 = resized_new_img1.crop(box)
    else:
        new_width = fs[0]
        new_height = (new_img1.size[1] * fs[0]) / new_img1.size[0]
        resized_new_img1 = new_img1.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
        box = (0, (resized_new_img1.size[1] - fs[1]) / 2, resized_new_img1.size[0], resized_new_img1.size[1] - (resized_new_img1.size[1] - fs[1]) / 2)
        resized_new_img1 = resized_new_img1.crop(box)
    filestream1 = BytesIO()
    resized_new_img1.save(filestream1, 'JPEG', quality=80)
    filestream1.seek(0)
    name1 = f"{f1.name}"
    return InMemoryUploadedFile(
        filestream1, 'ImageField', name1, 'jpeg/image',
        sys.getsizeof(filestream1), None
    )



intro_image = [804, 918]