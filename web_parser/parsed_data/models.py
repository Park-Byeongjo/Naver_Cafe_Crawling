from django.db import models

# Create your models here.
class CafeData(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    time = models.TimeField()

    #django admin page title overloading
    def __str__(self):
        return self.title

