from django.db import models
from django.db.models import DEFERRED

# Create your models here.
class ImageDetails(models.Model):
    filename = models.CharField(max_length=200)
    color1R = models.IntegerField(default = 500)
    color1G = models.IntegerField(default = 500)
    color1B = models.IntegerField(default = 500)
    color2R = models.IntegerField(default = 500)
    color2G = models.IntegerField(default = 500)
    color2B = models.IntegerField(default = 500)
    color3G = models.IntegerField(default = 500)
    color3R = models.IntegerField(default = 500)
    color3B = models.IntegerField(default = 500)
    human = models.BooleanField(default = False)

    #@property


    #@classmethod
    #def addImage(cls, filename):
    #    image = cls(filename=filename)
    #def __init__(self, filename, colors):
        #self.filename = filename
        #self.color1R = colors[0][2]
        #self.color1G = colors[0][1]
        #self.color1B = colors[0][0]
        #self.color2R = colors[1][2]
        #self.color2B = colors[1][1]
        #self.color2G = colors[1][0]
        #self.color3R = colors[2][2]
        #self.color3B = colors[2][1]
        #self.color3G = colors[2][0]
