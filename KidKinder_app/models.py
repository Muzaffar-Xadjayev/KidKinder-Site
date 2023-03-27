from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class About(models.Model):
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='about_image/')
    # description = models.TextField(blank=True)
    description = RichTextUploadingField()
    # context = RichTextUploadingField()


    def __str__(self):
        return self.title


class Classes(models.Model):
    picture = models.ImageField(upload_to='classes_image/')
    title = models.CharField(max_length=50)
    description = models.TextField()
    yoshi = models.CharField(max_length=50)
    jami = models.CharField(max_length=50)
    vaqti = models.CharField(max_length=100)
    harajat = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Teachers(models.Model):
    picture = models.ImageField(upload_to='teachers_image/')
    name = models.CharField(max_length=50)
    kasb = models.CharField(max_length=100)
    twitter = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.name
    
class Parents(models.Model):
    picture = models.ImageField(upload_to='parents_image/')
    name = models.CharField(max_length=50)
    kasb = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Gallery(models.Model):
    picture = models.ImageField(upload_to='gallery_image/')


class Blog(models.Model):
    slug = models.SlugField()
    picture = models.ImageField(upload_to='blog_image/')
    title = models.CharField(max_length=50)
    description = models.TextField()


    def __str__(self):
        return self.title


class Contact(models.Model):
    address= models.CharField(max_length=200, null=True, blank=True)
    email= models.EmailField(max_length=50, null=True, blank=True)
    phone= models.CharField(max_length=20, null=True, blank=True)
    kun= models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.email


