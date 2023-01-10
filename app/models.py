from django.db import models


class Contact(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Subject=models.CharField(max_length=100)
    Message=models.TextField()
    
    def __str__(self):
        return self.Name

class Image(models.Model):
    pro_title=models.CharField(max_length=30)
    pro_image=models.ImageField(upload_to='media')
    pro_desc=models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)