from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=20)
    blog_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    blog_text = models.CharField(max_length=300)
    blog_image = models.ImageField(upload_to='blog_images/')

