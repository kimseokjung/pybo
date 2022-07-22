from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User


class Products(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_product')
    objects = models.Manager()
    product_name = models.CharField(max_length=200)
    product_price = models.CharField(max_length=200)
    product_size = models.CharField(max_length=200)
    product_board = RichTextUploadingField(null=True)
    upload_date = models.DateTimeField()

    def __str__(self):
        return self.product_name


class Images(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False)
    img = models.ImageField(upload_to='images/', null=False)
# product_thumb = ImageSpecField(source='image', processors=[ResizeToFill(200, 100)], format='JPEG')
