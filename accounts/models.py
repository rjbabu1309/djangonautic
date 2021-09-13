from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profiles(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    dob = models.DateTimeField()
    address = models.TextField()
    #username = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    #thumb = models.ImageField(default='default.png', blank=True)
    #author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstName + self.lastName
    #def snippet(self):
        #return self.body[:50] + '...'
