from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length = 50)
    publishedDate = models.DateTimeField(blank=True, null=True)
    modifiedDate = models.DateTimeField(blank=True, null=True)
    content = models.TextField()
    locate = models.TextField(null=True)
    phone = models.TextField(null=True)
    insta = models.TextField(null=True)
    
    def __str__(self):
        return self.name