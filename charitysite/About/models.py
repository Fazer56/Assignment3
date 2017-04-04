from django.db import models

# Create your models here.
# database with classes

class Post(models.Model):
    title = models.CharField(max_length= 140) 
    body = models.TextField()
    date = models.DateTimeFiels()

    #for meta data purposes if you want to list out all post titles
    # reference post.title won't work need to create a function to access the title

    def __str__(self):
        return self.title
    
