from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
'''
    - title
    - author
    - content
    - image
    - publish_data
    - tags
'''
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=50000)
    publish_date = models.DateTimeField()
    tags = TaggableManager()
    
    def __str__(self):
       return self.title